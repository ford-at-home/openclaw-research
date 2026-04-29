#!/usr/bin/env python3
"""
Build index.json and README.md from every markdown file in the repo.

Three content systems coexist (see CLAUDE.md):
  - Research library (taxonomy dirs: ai-ml/, cloud-infrastructure/, ...)
  - Personal wiki (wiki/source|concept|entity|synthesis|value|goal/)
  - Personal KB (personal/) plus side dirs (richmond/, writing/)

The index labels each entry with a `content_type` so an agent can
filter the corpus by system without re-deriving it from the path.

Outputs:
  - index.json: machine-readable corpus + by_type map for O(1) filtering
  - README.md: human-browsable listing grouped by content_type
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent

# Directories whose contents are never indexed.
EXCLUDE_DIRS = {"_templates", ".git", ".github", ".claude", "scripts", "raw"}

# Top-level meta files describing the repo itself, not corpus content.
EXCLUDE_FILES = {"index.json", "INDEX.md", "README.md", "TAXONOMY.md", "CLAUDE.md"}

# Canonical research taxonomy (mirrors TAXONOMY.md). Anything filed under one
# of these top-level dirs is treated as research-library content.
RESEARCH_CATEGORIES = {
    "ai-ml",
    "cloud-infrastructure",
    "software-engineering",
    "web-development",
    "business-strategy",
    "community-building",
    "data-science",
    "security",
    "hardware-iot",
}

GITHUB_REPO = "ford-at-home/openclaw-research"
GITHUB_BASE = f"https://github.com/{GITHUB_REPO}/blob/main"
RAW_BASE = f"https://raw.githubusercontent.com/{GITHUB_REPO}/main"


def parse_frontmatter(path: Path) -> dict:
    """Extract YAML frontmatter. Handles inline values and multi-line list tags."""
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}

    fm: dict = {}
    block = match.group(1)
    lines = block.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        if ":" not in line:
            i += 1
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        # Multi-line YAML list ("tags:" followed by "  - item" lines).
        if val == "":
            items: list[str] = []
            j = i + 1
            while j < len(lines) and lines[j].lstrip().startswith("- "):
                items.append(lines[j].lstrip()[2:].strip().strip('"'))
                j += 1
            if items:
                fm[key] = items
                i = j
                continue
            i += 1
            continue
        fm[key] = val.strip('"')
        i += 1

    # Normalize tags to a list regardless of source format.
    raw_tags = fm.get("tags", [])
    if isinstance(raw_tags, str):
        raw_tags = raw_tags.strip("[]")
        fm["tags"] = [t.strip().strip('"') for t in raw_tags.split(",") if t.strip()]
    elif not isinstance(raw_tags, list):
        fm["tags"] = []
    return fm


def extract_summary(path: Path, max_chars: int = 250) -> str:
    """Prefer an explicit TL;DR section; fall back to first non-heading paragraph."""
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"^---\s*\n.*?\n---\s*\n", "", text, flags=re.DOTALL).strip()

    tldr = re.search(r"##\s*TL;?DR\s*\n+(.*?)(?=\n##|\Z)", text, re.DOTALL | re.IGNORECASE)
    if tldr:
        summary = re.sub(r"<!--.*?-->", "", tldr.group(1), flags=re.DOTALL).strip()
        if summary:
            return summary[:max_chars]

    for para in text.split("\n\n"):
        para = para.strip()
        if para and not para.startswith("#") and not para.startswith("<!--"):
            return para[:max_chars]
    return ""


def classify(rel: Path, fm: dict) -> tuple[str, str, str]:
    """
    Return (content_type, category, subcategory).

    content_type is the agent's primary filter axis. category/subcategory
    keep their existing meaning for research; for wiki/personal they reflect
    the page_type / domain so the index is uniform.
    """
    parts = rel.parts
    top = parts[0] if parts else ""

    # Wiki: page_type drives content_type.
    if top == "wiki":
        page_type = fm.get("page_type") or (parts[1] if len(parts) > 1 else "page")
        return (
            f"wiki-{page_type}",
            fm.get("domain") or (parts[1] if len(parts) > 1 else "wiki"),
            fm.get("subdomain", ""),
        )

    if top == "personal":
        return ("personal", "personal", fm.get("category", ""))

    if top == "writing":
        return ("writing", "writing", fm.get("category", ""))

    if top == "voice-notes":
        return ("voice-notes", "voice-notes", "")

    if top in RESEARCH_CATEGORIES:
        sub = fm.get("subcategory") or (parts[1] if len(parts) > 2 else "")
        return ("research", fm.get("category") or top, sub)

    # Anything else (richmond/, etc.) is local/topical research.
    return ("local-research", fm.get("category") or top, fm.get("subcategory", ""))


def normalize_date(fm: dict, path: Path) -> str:
    """Return YYYY-MM-DD using frontmatter signals, falling back to file mtime."""
    for key in ("date", "last_updated", "ingest_timestamp"):
        raw = fm.get(key)
        if isinstance(raw, str) and len(raw) >= 10:
            return raw[:10]
    mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
    return mtime.strftime("%Y-%m-%d")


def derive_title(fm: dict, rel: Path) -> str:
    return (
        fm.get("title")
        or fm.get("query")
        or rel.stem.replace("-", " ").replace("_", " ").title()
    )


def collect_entries() -> list[dict]:
    entries: list[dict] = []

    for md_file in sorted(REPO_ROOT.rglob("*.md")):
        if any(part in EXCLUDE_DIRS for part in md_file.parts):
            continue
        if md_file.name in EXCLUDE_FILES:
            continue

        rel = md_file.relative_to(REPO_ROOT)
        fm = parse_frontmatter(md_file)
        content_type, category, subcategory = classify(rel, fm)

        # Skip the wiki's own auto-generated index (it's a meta file like README).
        if rel.as_posix() == "wiki/index.md":
            continue

        tags = fm.get("tags", [])
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.split(",") if t.strip()]

        entries.append({
            "filename": str(rel),
            "title": derive_title(fm, rel),
            "content_type": content_type,
            "category": category,
            "subcategory": subcategory,
            "date": normalize_date(fm, md_file),
            "query": fm.get("query", ""),
            "processor": fm.get("processor", ""),
            "status": fm.get("status", ""),
            "confidence": fm.get("confidence", ""),
            "run_id": fm.get("run_id", ""),
            "page_type": fm.get("page_type", ""),
            "summary": extract_summary(md_file) or fm.get("query", ""),
            "tags": tags,
            "github_url": f"{GITHUB_BASE}/{rel}",
            "raw_url": f"{RAW_BASE}/{rel}",
        })

    entries.sort(key=lambda e: e["date"], reverse=True)
    return entries


def build_by_type(entries: list[dict]) -> dict[str, list[str]]:
    """Map content_type -> list of filenames, for O(1) agent filtering."""
    out: dict[str, list[str]] = {}
    for e in entries:
        out.setdefault(e["content_type"], []).append(e["filename"])
    return out


def write_index(entries: list[dict]) -> None:
    manifest = {
        "version": "2.0.0",
        "last_synchronized": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total": len(entries),
        "content_types": sorted({e["content_type"] for e in entries}),
        "by_type": build_by_type(entries),
        "corpus": entries,
    }
    out = REPO_ROOT / "index.json"
    out.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote index.json ({len(entries)} entries, {len(manifest['content_types'])} types)")


# Human-friendly labels for content_type buckets in the README.
TYPE_LABEL = {
    "research": "Research Library",
    "wiki-source": "Wiki — Sources (voice memos / messages)",
    "wiki-concept": "Wiki — Concepts",
    "wiki-entity": "Wiki — Entities",
    "wiki-synthesis": "Wiki — Syntheses",
    "wiki-value": "Wiki — Values",
    "wiki-goal": "Wiki — Goals",
    "personal": "Personal KB",
    "writing": "Writing",
    "voice-notes": "Voice notes (legacy)",
    "local-research": "Local / Topical Research",
}


def write_readme(entries: list[dict]) -> None:
    by_type: dict[str, list[dict]] = {}
    for e in entries:
        by_type.setdefault(e["content_type"], []).append(e)

    recent = entries[:10]
    all_tags = sorted({t for e in entries for t in e["tags"]})

    lines = [
        "# openclaw-research",
        "",
        "Knowledge repository for the OpenClaw AI assistant. Three content systems live here: the **research library** (deep async publications, taxonomy-organized), the **personal wiki** (voice-memo-driven knowledge graph), and the **personal KB** (bot-managed profiles). See `CLAUDE.md` for the architecture and `TAXONOMY.md` for research categories.",
        "",
        "**Agent commands:**",
        "",
        "| Command | What it does |",
        "|---------|-------------|",
        "| `/research <query>` | Deep research a topic and publish to the library |",
        "| `/research:add-research <topic>` | Agent-curated research with taxonomy |",
        "| `/research:find-research <query>` | Search the library |",
        "| `/research:update-index` | Rebuild this file via `scripts/build-index.py` |",
        "",
        f"**Last indexed:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}  ",
        f"**Total documents:** {len(entries)}  ",
        f"**Content types:** {', '.join(sorted(by_type))}",
        "",
    ]

    if recent:
        lines += ["## Recent additions", ""]
        for e in recent:
            label = TYPE_LABEL.get(e["content_type"], e["content_type"])
            lines.append(f"- `{e['date']}` **[{e['title']}]({e['github_url']})** — _{label}_")
        lines.append("")

    # One section per content_type, in a stable display order.
    type_order = [
        "research",
        "local-research",
        "wiki-concept",
        "wiki-entity",
        "wiki-synthesis",
        "wiki-value",
        "wiki-goal",
        "wiki-source",
        "personal",
        "writing",
        "voice-notes",
    ]
    seen = set()
    for ct in type_order + sorted(by_type):
        if ct in seen or ct not in by_type:
            continue
        seen.add(ct)
        items = by_type[ct]
        lines += [f"## {TYPE_LABEL.get(ct, ct)} ({len(items)})", ""]
        # Within research, group by category for readability.
        if ct == "research":
            by_cat: dict[str, list[dict]] = {}
            for e in items:
                by_cat.setdefault(e["category"], []).append(e)
            for cat in sorted(by_cat):
                lines.append(f"### {cat}")
                lines.append("")
                for e in by_cat[cat]:
                    sub = f" / {e['subcategory']}" if e["subcategory"] else ""
                    lines.append(f"- `{e['date']}` [{e['title']}]({e['github_url']}){sub}")
                lines.append("")
        else:
            for e in items:
                lines.append(f"- `{e['date']}` [{e['title']}]({e['github_url']})")
            lines.append("")

    if all_tags:
        lines += ["## Tag index", ""]
        for tag in all_tags:
            tagged = [e for e in entries if tag in e["tags"]]
            links = ", ".join(f"[{e['title']}]({e['github_url']})" for e in tagged[:5])
            more = f" _+{len(tagged) - 5} more_" if len(tagged) > 5 else ""
            lines.append(f"- **{tag}** — {links}{more}")
        lines.append("")

    lines += [
        "## Layout",
        "",
        "```",
        "openclaw-research/",
        "  index.json              # Machine-readable corpus (auto-generated)",
        "  README.md               # This file (auto-generated)",
        "  TAXONOMY.md             # Research category definitions",
        "  CLAUDE.md               # Architecture + conventions",
        "  _templates/             # Document templates",
        "  .claude/commands/       # Claude Code slash commands",
        "  scripts/build-index.py  # Index builder",
        "",
        "  # Research library (taxonomy)",
        "  ai-ml/  cloud-infrastructure/  software-engineering/  web-development/",
        "  business-strategy/  community-building/  data-science/  security/  hardware-iot/",
        "",
        "  # Personal wiki",
        "  wiki/source|concept|entity|synthesis|value|goal/",
        "",
        "  # Other",
        "  personal/  writing/  richmond/  voice-notes/  raw/",
        "```",
        "",
        "_Auto-generated by `.github/workflows/index.yml` (or run `python scripts/build-index.py` locally). Do not edit manually._",
    ]

    out = REPO_ROOT / "README.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote README.md ({len(entries)} entries, {len(by_type)} content types)")


if __name__ == "__main__":
    entries = collect_entries()
    write_index(entries)
    write_readme(entries)
    if not entries:
        print("Warning: no content files found", file=sys.stderr)
    sys.exit(0)
