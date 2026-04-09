# /research:find-research

Search the research library by keyword, tag, category, or topic.

**Usage:** `/research:find-research <query>`

**Examples:**
- `/research:find-research "RAG"`
- `/research:find-research --tag vector-db`
- `/research:find-research --category ai-ml`
- `/research:find-research --status draft`
- `/research:find-research "agent memory" --category ai-ml`

## Instructions

You are searching the research library at `/Users/williamprior/Development/GitHub/openclaw-research/`.

### Step 1: Parse the Query

Extract:
- **Free-text query**: words to search for in titles, tags, and body content
- `--tag <tag>`: filter by specific tag
- `--category <category>`: filter to a specific category
- `--subcategory <subcategory>`: filter to a specific subcategory
- `--status <status>`: filter by status (draft | review | final)
- `--confidence <level>`: filter by confidence (low | medium | high)

### Step 2: Determine Search Strategy

Based on the query, combine these approaches:

**By tag or category** (fast path):
- If `--tag` specified: Grep frontmatter for the tag across `**/*.md`
- If `--category` specified: Glob only within `<category>/`
- If `--status` specified: Grep for `status: "<status>"` in frontmatter

**By keyword** (content search):
- Grep for the keyword across all `.md` files (excluding `INDEX.md`, `TAXONOMY.md`, `_templates/`)
- Rank by relevance: title match > tag match > body match

**By topic** (semantic):
- Read `INDEX.md` first for a quick scan of all titles/tags
- Identify likely categories from `TAXONOMY.md`
- Grep within those categories for related terms

### Step 3: Return Results

Format results as:
```
Found N documents matching "<query>":

1. **[Title](path/to/file.md)**
   Category: ai-ml/agents | Date: YYYY-MM-DD | Confidence: medium | Status: draft
   Tags: agent, orchestration, memory
   Excerpt: "...relevant sentence from the document..."

2. **[Title 2](path/to/file2.md)**
   ...
```

If zero results:
```
No documents found matching "<query>".

Suggestions:
- Try broader terms
- Run `/research:add-research "<query>"` to create new research on this topic
- Browse INDEX.md for related topics
```

### Step 4: Offer Next Steps

After showing results, offer:
- "Run `/research:add-research <topic>` to add research on a related topic"
- "Run `/research:find-research <related-term>` to broaden the search"

## Rules

- Always check INDEX.md first for speed; fall back to full Grep if index is stale.
- Never modify any files during search.
- Show relative paths from the library root directory.
- If zero results, say so plainly and suggest running `/research:add-research <query>`.
- Excerpt length: 1-2 sentences max, capturing the most relevant passage.
