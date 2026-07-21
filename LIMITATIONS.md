# Known Limitations and Scope Corrections

This document records methodological defects identified in external review and the corrections applied in this repository. Read this before treating any finding document as formal evidence.

## Repository name vs. current scope

The GitHub repository slug **`ai-infrastructure-crisis-2025`** is historical. The moderated analysis title is **AI Ecosystem Transition 2025: Cross-Repository Forensic Analysis**.

The repository documents **correlated infrastructure-related changes in public Git histories**. It does **not** currently substantiate a proven cross-ecosystem collapse, coordinated failure, or independently confirmed upstream cause.

## What the evidence supports

- Public commit histories were collected and compared across selected upstream repositories.
- Transformers shows sustained late-2025 activity in dtype, attention, quantization, and configuration areas.
- Temporal clustering of commits can be observed in some windows (see `timelines/` and `metadata_notes/sync_matrix.txt`).
- A monitoring methodology (commit bursts, bisection windows, schema drift) is demonstrated in `examples/` and `technical-note.md`.

## What the evidence does not currently support

- That four repositories experienced the **same failure** simultaneously in August–September 2025.
- That the probability of coincidence is negligible without formal statistical testing.
- That a specific PyTorch/CUDA transition **caused** all observed changes (causation is hypothesised, not confirmed).
- That the analysis meets forensic, legal, or scientific proof standards.
- That maintainers or upstream vendors have validated the dependency interpretation.

## Repository-specific corrections

### LLaMA (`meta-llama/llama`)

- The analysed repository is **deprecated** and superseded by Meta’s active Llama distribution channels.
- The included timeline’s newest entry is **2025-01-26** (README rename: “Llama Recipes” → “Llama Cookbook”) — not dtype, attention, or quantization infrastructure work.
- **LLaMA is excluded from the August–September 2025 convergence claim** unless analysis is rebuilt against the current active upstream repository with matching commit evidence.

### MuJoCo (`google-deepmind/mujoco`)

- MuJoCo is a **physics simulation engine** (C/C++ core, separate GPU paths). It is **not** a downstream consumer of Hugging Face Transformers.
- MuJoCo activity in this dataset largely reflects renderer, WASM, documentation, API, and **v3.4.0 release preparation** — a different domain from transformer dtype/attention/quantization pressure.
- MuJoCo may show **parallel temporal clustering** with other repos during release windows; that is **not** evidence of a shared Transformers failure mode unless a documented dependency path is shown.

### Primary convergence pair

For infrastructure-stack claims (dtype, attention, quantization, config schema), the defensible primary pair in the published timelines is:

1. **Transformers** (Hugging Face)
2. **nanoGPT** (minimal PyTorch GPT reference)

MuJoCo and deprecated LLaMA are retained as **comparative case studies**, not as equal participants in a four-way synchronized failure narrative.

## Language and document hierarchy

Earlier drafts used terms such as “proves,” “undeniable,” “unmistakable,” “collapse,” and “forensic-quality proof.” Those terms **overstate** what commit-history correlation alone can establish.

| Document | Role |
| -------- | ---- |
| `README.md`, `technical-note.md` | Moderated scope and methodology |
| `LIMITATIONS.md` (this file) | Explicit defects and exclusions |
| `docs/findings/*.md` | Working analysis with interpretive framing — check against timelines |
| `data/*`, `logs/*` | Derived exports; may contain duplicated or superseded narrative text |

## Incomplete reproducibility artefacts

The following items were flagged as unfinished and are **not** sufficient for independent replication on their own:

- `logs/*_PLACEHOLDER.txt` — snapshot slots; see `logs/README.md`
- `metadata_notes/sync_matrix.txt` — contained an unfilled `YYYY-MM-DD` template (removed)
- Malformed or concatenated rows in some timeline exports — treat as raw harvest artefacts

Use `reproducibility/MANIFEST.md` for upstream URLs, collection parameters, and inclusion rules.

## External validation

As of the last review pass, the public repository had limited external replication, review, or maintainer endorsement. Findings should be treated as **exploratory open-source intelligence**, not validated forensic study, until independently reproduced.

## Contact

For questions about scope, redacted exports, or reproduction parameters: see `README.md` (Author section) and `ATTRIBUTION.md`.
