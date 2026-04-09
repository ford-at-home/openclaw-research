# /research:bulk-research

Research multiple topics in parallel and add all documents to the library.

**Usage:** `/research:bulk-research <topics>`

**Examples:**
- `/research:bulk-research "RAG architectures, agent memory systems, LLM evaluation frameworks"`
- `/research:bulk-research --category ai-ml --count 5` (research 5 topics across ai-ml)
- `/research:bulk-research "prompt chaining, fine-tuning LoRA, vector databases, embeddings"`

## Instructions

You are adding multiple research documents to the library at `/Users/williamprior/Development/GitHub/openclaw-research/`.

### Step 1: Parse Topics

From the user's input:
- **Comma-separated list**: split on commas, trim whitespace — each item is one research topic
- **Category + count**: if `--category X --count N` format, generate N topic suggestions from that category's scope (read `TAXONOMY.md` for scope descriptions), then confirm with user before researching
- Deduplicate topics if any overlap

List topics back to the user before starting:
```
Starting bulk research on N topics:
1. RAG architectures → ai-ml/rag
2. Agent memory systems → ai-ml/agents
3. LLM evaluation frameworks → ai-ml/benchmarks

Spawning parallel agents...
```

### Step 2: Classify Each Topic

For each topic:
1. Read `TAXONOMY.md` to determine the best category/subcategory
2. Assign a path: `<category>/<subcategory>/`
3. If no good fit exists, flag it: "[Topic] doesn't fit taxonomy cleanly — closest is `X`. Proceed? (y/n)"

### Step 3: Spawn Parallel Research Agents

Use the **Agent tool** to spawn parallel research agents, one per document. Each agent should:

1. Research the topic using available tools (WebSearch, deep-research, etc.)
2. Read the template from `_templates/research-template.md`
3. Write a complete research document following the template
4. Save to `<category>/<subcategory>/YYYY-MM-DD-kebab-title.md`

Spawn up to 5 agents concurrently. If >5 topics, batch in waves.

Wave structure:
- Wave 1: topics 1-5 (spawn all, wait for completion)
- Wave 2: topics 6-10
- etc.

### Step 4: Rebuild Index

After ALL documents are written, rebuild the index:
1. Glob `**/*.md` (exclude `_templates/`, `INDEX.md`, `TAXONOMY.md`, `README.md`)
2. Parse frontmatter from each
3. Rebuild `INDEX.md` with all sections (stats, by-category, by-tag, recent)

### Step 5: Report

Output a completion table:
```
Bulk research complete: N/N documents added

| # | Title | Path | Confidence |
|---|-------|------|------------|
| 1 | RAG Architectures | ai-ml/rag/2026-04-09-rag-architectures.md | medium |
| 2 | ... | ... | ... |

Index updated: N total documents, M unique tags.
```

If any agent failed, list failures separately:
```
Failed (N):
- "Topic name" — reason
```

## Rules

- Never spawn more than 5 agents simultaneously.
- Each agent must produce a complete document — no stubs or partial files.
- If a topic is too broad, the agent should narrow the scope and note it in the TL;DR.
- The index rebuild happens ONCE after all agents complete, not per document.
- Never overwrite an existing document with the same filename — append `-v2` if conflict.
