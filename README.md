# Research Library

A structured repository for research across all topics, designed for AI agents to contribute to and query from.

## Quick Start

| Command | What it does |
|---------|-------------|
| `/research:add-research <topic>` | Research a topic, write it up, file it, update the index |
| `/research:bulk-research <topics>` | Add multiple research docs in parallel |
| `/research:find-research <query>` | Search the library by keyword, tag, or category |
| `/research:update-index` | Rebuild INDEX.md from all documents |

## Structure

```
openclaw-research/
  INDEX.md              # Auto-generated searchable index
  TAXONOMY.md           # Category/subcategory definitions
  README.md             # This file
  _templates/           # Document templates
    research-template.md
  .claude/commands/research/  # Claude Code slash commands
    add-research.md
    bulk-research.md
    find-research.md
    update-index.md
  ai-ml/               # AI & Machine Learning
    agents/
    llms/
    benchmarks/
    ...
  cloud-infrastructure/ # Cloud & Infra
    aws/
    serverless/
    ...
  software-engineering/ # Software Engineering
  web-development/      # Web Dev
  blockchain-crypto/    # Blockchain
  business-strategy/    # Business
  community-building/   # Community & Events
  data-science/         # Data Science
  security/             # Cybersecurity
  hardware-iot/         # Hardware & IoT
```

## Document Format

Every research document uses the standard template with YAML frontmatter:

```yaml
---
title: "Document Title"
date: "YYYY-MM-DD"
category: "ai-ml"
subcategory: "agents"
tags: [agents, orchestration, multi-agent]
author: "agent-name or human"
status: "draft"        # draft | review | final
confidence: "medium"   # low | medium | high
sources_verified: false
---
```

## Adding New Categories

1. Edit `TAXONOMY.md` to add the category/subcategory
2. Create the directory: `mkdir -p research/<category>/<subcategory>`
3. Run `/research:update-index`

## Conventions

- **Filenames**: `YYYY-MM-DD-kebab-case-title.md`
- **One topic per doc**: Split broad topics into focused pieces
- **Primary filing**: File under the main category, use tags for cross-references
- **Sources**: Always cite. Mark unverifiable sources with `[Unverified]`
- **No stubs**: Every document must have substantive content in all sections
