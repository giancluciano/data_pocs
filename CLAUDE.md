# data_pocs — instructions for Claude

This is the user's personal data engineering study repo (roadmap.sh Data Engineer roadmap).

## Hard rule: no AI-generated code or study content

- Do NOT write code in `pocs/` (no scripts, SQL, DAGs, notebooks, tests) and do NOT write the learning notes in `docs/`. The user writes these themselves.
- Do NOT apply the global TDD / code-review / agent workflows here — they don't apply to this repo.
- Allowed: organizing topics, folder structure, templates, `README.md` checklist/POC index, environment setup help (explaining how to install/run tools), answering questions and explaining concepts in chat.
- If asked to "do" a POC, explain/guide instead of writing the code, unless the user explicitly overrides this rule for that request.

## Conventions

- Phase-numbered names: `docs/NN-topic.md`, `pocs/NN-topic/` (phases listed in `README.md`).
- Templates: `docs/_template.md`, `pocs/_template/`.
- When a topic/POC is added, update the checklist and POC index in `README.md`.
