# /research:update-index

Rebuild INDEX.md by scanning all research documents in the library.

**Usage:** `/research:update-index`

## Instructions

You are rebuilding the research index at `/Users/williamprior/Development/GitHub/openclaw-research/INDEX.md`.

### Step 1: Scan All Documents

1. Use `Glob` with pattern `**/*.md` to find all markdown files.
2. Exclude: `INDEX.md`, `TAXONOMY.md`, `_templates/**`, `README.md`

### Step 2: Parse Each Document

For each document, read the first 20 lines to extract YAML frontmatter:
- `title`
- `date`
- `category`
- `subcategory`
- `tags`
- `status`
- `confidence`

If frontmatter is missing, still list the file but mark fields as "unknown".

### Step 3: Build the Index

Write a new `INDEX.md` with these sections in order:

#### Section 1: Header + Stats
```markdown
# Research Library Index

*Auto-generated. Run `/research:update-index` to rebuild.*

**Last updated:** YYYY-MM-DD
**Total documents:** N
**Categories with content:** N
**Unique tags:** N
```

#### Section 2: By Category

For each category that has at least one document, create a subsection:
```markdown
## Category Name

| Title | Date | Subcategory | Confidence | Status |
|-------|------|-------------|------------|--------|
| [Title](path/to/file.md) | YYYY-MM-DD | subcategory | medium | draft |
```

Sort documents within each category by date descending (newest first).

#### Section 3: Recent Additions

List the 10 most recently dated documents across all categories:
```markdown
## Recent Additions

| Title | Category | Date |
|-------|----------|------|
| [Title](path) | ai-ml/agents | YYYY-MM-DD |
```

#### Section 4: Tag Index

List all unique tags alphabetically, each with links to documents that use it:
```markdown
## Tag Index

**agent** — [Doc Title](path), [Doc Title 2](path2)
**rag** — [Doc Title](path)
```

### Step 4: Confirm

Output:
```
Index rebuilt:
  Documents scanned: N
  Documents indexed: N
  Categories with content: N
  Unique tags: N
  File: INDEX.md
```

## Rules

- Relative paths in the index must work from the library root directory.
- Never modify any research documents during index rebuild.
- If a document has no frontmatter, still list it but mark fields as "unknown".
- Sort is always date descending (newest first) unless stated otherwise.
- The index is read-only output — never add commentary or opinions.
