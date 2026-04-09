# /research:add-research

Research a topic and add a structured document to the library.

**Usage:** `/research:add-research <topic>`

**Examples:**
- `/research:add-research "RAG architectures"`
- `/research:add-research "Kubernetes cost optimization"`
- `/research:add-research "agent memory systems" --category ai-ml --subcategory agents`

## Instructions

You are adding a research document to the research library at `/Users/williamprior/Development/GitHub/openclaw-research/`.

### Step 1: Parse Input

Extract from the user's input:
- **Topic**: the subject to research
- **Category** (optional): if specified with `--category`, use it; otherwise infer from TAXONOMY.md
- **Subcategory** (optional): if specified with `--subcategory`, use it; otherwise infer

### Step 2: Validate Taxonomy Path

1. Read `TAXONOMY.md` to confirm the category/subcategory exists.
2. If the subcategory doesn't exist:
   - Check if it fits an existing category under a different name.
   - If truly new, ask the user: "Subcategory `X` doesn't exist. Create it under `category/`? (y/n)"
3. Confirm the directory exists: `<category>/<subcategory>/`

### Step 3: Research the Topic

Use available tools to research the topic thoroughly:
- Use web search / deep research skills if available (`/parallel:deep-research` or `WebSearch`)
- Read any existing research in the same subcategory for context (use `Glob` on `<category>/<subcategory>/*.md`)
- Gather multiple sources and perspectives

### Step 4: Write the Document

1. Read the template from `_templates/research-template.md`
2. Generate a filename: `YYYY-MM-DD-kebab-case-title.md` (use today's date)
3. Fill in ALL template sections with substantive content:
   - **Frontmatter**: All fields populated. `status: "draft"`, `confidence` based on source quality.
   - **TL;DR**: 2-3 sentences, genuinely useful summary.
   - **Context**: Why this topic matters. What prompted research.
   - **Key Findings**: Minimum 3 concrete, specific findings — not platitudes.
   - **Analysis**: Comparisons, trade-offs, nuance.
   - **Implications**: What this means for our work.
   - **Open Questions**: Genuine unknowns, not filler.
   - **Sources**: Real, verifiable URLs/references. Mark `[Unverified]` if uncertain.
4. Write the file to `<category>/<subcategory>/<filename>.md`

### Step 5: Update the Index

After writing the document, run the index update procedure:

1. Use `Glob` to find ALL `*.md` files under the library root (excluding `_templates/`, `INDEX.md`, `TAXONOMY.md`)
2. Read the frontmatter of each file (first 15 lines is usually enough)
3. Rebuild `INDEX.md` with:
   - Updated statistics (total docs, categories with docs, tags)
   - Documents grouped by category, each showing: title, date, subcategory, confidence, link
   - Tag index: each tag with links to docs that use it
   - Recent additions section (last 5 docs by date)

### Step 6: Confirm

Output a summary:
```
Research added:
  File: <category>/<subcategory>/<filename>.md
  Title: <title>
  Tags: <tag1>, <tag2>, ...
  Confidence: <level>
  Index: updated (N total documents)
```

## Rules

- Never skip sections in the template. Every section must have substantive content.
- Never invent sources. Use `[Unverified]` when uncertain about a reference.
- Confidence levels: `high` = verified primary sources; `medium` = secondary sources; `low` = inference/speculation.
- If web search is unavailable, do your best with existing knowledge and mark `sources_verified: false`.
