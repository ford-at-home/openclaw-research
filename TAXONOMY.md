# Research Taxonomy

This defines the canonical category/subcategory structure. All research documents must be filed into one of these paths. If a new subcategory is needed, add it here first, then create the directory.

## Categories

### `ai-ml/` - Artificial Intelligence & Machine Learning
| Subcategory | Scope |
|---|---|
| `agents` | AI agents, multi-agent systems, orchestration, tool use |
| `llms` | Large language models, foundation models, capabilities, evals |
| `benchmarks` | Evaluation frameworks, scoring systems, leaderboards |
| `prompt-engineering` | Prompting techniques, chains, templates, optimization |
| `fine-tuning` | Model customization, PEFT, LoRA, training data |
| `rag` | Retrieval-augmented generation, vector DBs, embeddings |
| `computer-vision` | Image/video models, OCR, generation |
| `nlp` | Text processing, classification, NER, sentiment |
| `robotics` | Physical AI, manipulation, navigation |
| `ethics` | AI safety, alignment, bias, governance, regulation |

### `cloud-infrastructure/` - Cloud & Infrastructure
| Subcategory | Scope |
|---|---|
| `aws` | AWS services, patterns, best practices |
| `gcp` | Google Cloud services and patterns |
| `azure` | Azure services and patterns |
| `serverless` | Lambda, Functions, event-driven architectures |
| `containers` | Docker, Kubernetes, ECS, orchestration |
| `networking` | VPCs, CDNs, DNS, load balancing |
| `security` | Cloud security, IAM, encryption, compliance |
| `iac` | Terraform, CDK, CloudFormation, Pulumi |
| `cost-optimization` | FinOps, right-sizing, reserved capacity |

### `software-engineering/` - Software Engineering
| Subcategory | Scope |
|---|---|
| `architecture` | System design, patterns, microservices, monoliths |
| `testing` | Test strategies, frameworks, TDD, property testing |
| `devops` | CI/CD, deployment, release management |
| `ci-cd` | Pipeline design, GitHub Actions, build systems |
| `databases` | SQL, NoSQL, graph, time-series, migrations |
| `apis` | REST, GraphQL, gRPC, API design |
| `performance` | Profiling, optimization, caching, scaling |
| `observability` | Logging, metrics, tracing, alerting |
| `languages` | Programming language comparisons, features, ecosystems |

### `web-development/` - Web Development
| Subcategory | Scope |
|---|---|
| `frontend` | React, Vue, Svelte, browser APIs |
| `backend` | Node, Python, Go, server frameworks |
| `fullstack` | End-to-end patterns, SSR, meta-frameworks |
| `frameworks` | Framework comparisons, evaluations |
| `design-systems` | Component libraries, tokens, theming |
| `accessibility` | WCAG, a11y patterns, assistive tech |
| `pwa` | Service workers, offline, installability |

### `business-strategy/` - Business & Strategy
| Subcategory | Scope |
|---|---|
| `startups` | Company building, operations, culture |
| `fundraising` | VC, grants, crowdfunding, pitch decks |
| `go-to-market` | Launch strategy, distribution, growth |
| `product-management` | Roadmaps, prioritization, user research |
| `pricing` | Pricing models, monetization, SaaS economics |
| `competitive-analysis` | Market landscape, competitor teardowns |

### `community-building/` - Community & Events
| Subcategory | Scope |
|---|---|
| `hackathons` | Event design, judging, logistics, platforms |
| `meetups` | Organizing, formats, engagement |
| `developer-relations` | DevRel strategy, advocacy, content |
| `open-source` | OSS governance, licensing, contribution |
| `education` | Workshops, curricula, mentorship |

### `data-science/` - Data Science
| Subcategory | Scope |
|---|---|
| `analytics` | Business intelligence, reporting, dashboards |
| `visualization` | Charts, maps, interactive viz |
| `pipelines` | ETL, streaming, data warehouses |
| `machine-learning` | Classical ML, sklearn, feature engineering |
| `statistics` | Statistical methods, experiment design, A/B testing |

### `security/` - Cybersecurity
| Subcategory | Scope |
|---|---|
| `appsec` | Application security, OWASP, SAST/DAST |
| `infrastructure` | Network security, hardening, firewalls |
| `compliance` | SOC2, HIPAA, GDPR, FedRAMP |
| `identity` | AuthN/AuthZ, SSO, MFA, zero trust |
| `threat-modeling` | Attack surfaces, risk assessment |

### `hardware-iot/` - Hardware & IoT
| Subcategory | Scope |
|---|---|
| `embedded` | Microcontrollers, firmware, RTOS |
| `sensors` | Sensor types, data collection |
| `edge-computing` | Edge inference, fog computing |
| `3d-printing` | Additive manufacturing, materials |
| `wearables` | Wearable tech, health sensors |

## Adding New Categories

1. Add the category and subcategories to this file
2. Create the directory: `mkdir -p <category>/<subcategory>`
3. Run `/research:update-index` to regenerate the index

## Cross-cutting Research

If research spans multiple categories, file it under the **primary** category and add tags for the secondary ones. The index and search skill handle cross-references via tags.

