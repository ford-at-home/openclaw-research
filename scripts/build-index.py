#!/usr/bin/env python3
"""
Build index.json and README.md from research markdown files.

Parses YAML frontmatter from every .md file in the repo (excluding
templates, index, and readme), then writes:
  - index.json: machine-readable corpus for OpenClaw librarian
  - README.md: human-browsable listing with recent entries
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
EXCLUDE_DIRS = {"_templates", ".git", ".github", ".claude", "scripts"}
EXCLUDE_FILES = {"index.json", "INDEX.md", "README.md", "TAXONOMY.md"}
GITHUB_REPO = "ford-at-home/openclaw-research"
GITHUB_BASE = f"https://github.com/{GITHUB_REPO}/blob/main"
RAW_BASE = f"https://raw.githubusercontent.com/{GITHUB_REPO}/main"


def parse_frontmatter(path: Path) -> dict:
    """Extract YAML frontmatter from a markdown file. Returns {} if none."""
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}

    fm = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip().strip('"')
        fm[key] = val

    # Parse tags — handles both YAML list and inline string forms
    raw_tags = fm.get("tags", "")
    if isinstance(raw_tags, str):
        raw_tags = raw_tags.strip("[]")
        fm["tags"] = [t.strip().strip('"') for t in raw_tags.split(",") if t.strip()]
    return fm


def extract_summary(path: Path, max_chars: int = 250) -> str:
    """
    Extract a summary from the document body.
    Prefers a TL;DR section if present; falls back to first non-empty paragraph.
    """
    text = path.read_text(encoding="utf-8")
    # Strip frontmatter
    text = re.sub(r"^---\s*\n.*?\n---\s*\n", "", text, flags=re.DOTALL).strip()

    # Look for explicit TL;DR section
    tldr = re.search(r"##\s*TL;?DR\s*\n+(.*?)(?=\n##|\Z)", text, re.DOTALL | re.IGNORECASE)
    if tldr:
        summary = tldr.group(1).strip()
        # Remove HTML comments
        summary = re.sub(r"<!--.*?-->", "", summary, flags=re.DOTALL).strip()
        if summary:
            return summary[:max_chars]

    # Fall back to first non-empty paragraph
    for para in text.split("\n\n"):
        para = para.strip()
        if para and not para.startswith("#") and not para.startswith("<!--"):
            return para[:max_chars]

    return ""


def collect_entries() -> list[dict]:
    """Walk the repo and collect metadata for every research file."""
    entries = []

    for md_file in sorted(REPO_ROOT.rglob("*.md")):
        # Skip excluded directories
        if any(part in EXCLUDE_DIRS for part in md_file.parts):
            continue
        if md_file.name in EXCLUDE_FILES:
            continue

        rel = md_file.relative_to(REPO_ROOT)
        fm = parse_frontmatter(md_file)
        summary = extract_summary(md_file)

        # Determine title: prefer frontmatter, then derive from filename
        title = fm.get("title") or fm.get("query") or rel.stem.replace("-", " ").title()

        # Normalize date — accepts "YYYY-MM-DD" and "YYYY-MM-DD HH:MM UTC"
        raw_date = fm.get("date", "")
        date_str = raw_date[:10] if raw_date else "unknown"

        tags = fm.get("tags", [])
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.split(",") if t.strip()]

        entries.append({
            "filename": str(rel),
            "title": title,
            "query": fm.get("query", title),
            "processor": fm.get("processor", "unknown"),
            "date": date_str,
            "category": fm.get("category", str(rel.parts[0]) if len(rel.parts) > 1 else "uncategorized"),
            "subcategory": fm.get("subcategory", str(rel.parts[1]) if len(rel.parts) > 2 else ""),
            "status": fm.get("status", "draft"),
            "confidence": fm.get("confidence", "unknown"),
            "run_id": fm.get("run_id", ""),
            "summary": summary or fm.get("query", ""),
            "tags": tags,
            "github_url": f"{GITHUB_BASE}/{rel}",
            "raw_url": f"{RAW_BASE}/{rel}",
        })

    # Sort newest first
    entries.sort(key=lambda e: e["date"], reverse=True)
    return entries


def write_index(entries: list[dict]) -> None:
    """Write index.json to the repo root."""
    manifest = {
        "version": "1.0.0",
        "last_synchronized": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total": len(entries),
        "corpus": entries,
    }
    out = REPO_ROOT / "index.json"
    out.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote index.json ({len(entries)} entries)")


def write_readme(entries: list[dict]) -> None:
    """Rebuild README.md with a human-browsable listing."""
    # Group by category
    by_cat: dict[str, list[dict]] = {}
    for e in entries:
        by_cat.setdefault(e["category"], []).append(e)

    recent = entries[:10]
    all_tags = sorted({t for e in entries for t in e["tags"]})

    lines = [
        "# openclaw-research",
        "",
        "Research library for the OpenClaw AI assistant. Published automatically via `research-and-publish.sh` and the `/research` slash command.",
        "",
        "**Agent commands:**",
        "| Command | What it does |",
        "|---------|-------------|",
        "| `/research <query>` | Research a topic and publish to this repo |",
        "| `/research:add-research <topic>` | Agent-curated research with taxonomy |",
        "| `/research:find-research <query>` | Search the library |",
        "| `/research:update-index` | Rebuild INDEX.md manually |",
        "",
        f"**Last indexed:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}  ",
        f"**Total documents:** {len(entries)}",
        "",
    ]

    if recent:
        lines += ["## Recent Research", ""]
        for e in recent:
            lines.append(f"- [{e['title']}]({e['github_url']}) — {e['summary'][:120] if e['summary'] else e['date']}")
        lines.append("")

    if by_cat:
        lines += ["## By Category", ""]
        for cat in sorted(by_cat):
            cat_entries = by_cat[cat]
            lines.append(f"### {cat} ({len(cat_entries)})")
            lines.append("")
            for e in cat_entries:
                date = f"`{e['date']}`" if e["date"] != "unknown" else ""
                lines.append(f"- [{e['title']}]({e['github_url']}) {date}")
            lines.append("")

    if all_tags:
        lines += ["## Tags", ""]
        for tag in all_tags:
            tagged = [e for e in entries if tag in e["tags"]]
            links = ", ".join(f"[{e['title']}]({e['github_url']})" for e in tagged[:5])
            lines.append(f"**{tag}** — {links}")
        lines.append("")

    lines += [
        "## Structure",
        "",
        "```",
        "openclaw-research/",
        "  index.json          # Machine-readable corpus (auto-generated)",
        "  README.md           # This file (auto-generated)",
        "  TAXONOMY.md         # Category/subcategory definitions",
        "  _templates/         # Document templates",
        "  .claude/commands/   # Claude Code slash commands",
        "  ai-ml/              # AI & Machine Learning",
        "  cloud-infrastructure/",
        "  software-engineering/",
        "  web-development/",
        "  business-strategy/",
        "  community-building/",
        "  data-science/",
        "  security/",
        "  hardware-iot/",
        "```",
        "",
        "_Auto-generated by `.github/workflows/index.yml`. Do not edit manually._",
    ]

    out = REPO_ROOT / "README.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote README.md ({len(entries)} entries, {len(by_cat)} categories)")


if __name__ == "__main__":
    entries = collect_entries()
    write_index(entries)
    write_readme(entries)
    if not entries:
        print("Warning: no research files found", file=sys.stderr)
    sys.exit(0)
