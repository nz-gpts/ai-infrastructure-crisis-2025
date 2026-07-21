# Reproducibility Manifest

Machine-readable parameters for reproducing the **high-level** methodology (commit timelines, burst detection, cross-repo date overlap). This does not include the proprietary `deep_pattern_engines` / EcosystemRadar backend.

## Upstream repositories

| Label | URL | Branch / note | Role in this study |
| ----- | --- | ------------- | ------------------ |
| Transformers | https://github.com/huggingface/transformers | `main` | Primary — transformer stack infrastructure |
| nanoGPT | https://github.com/karpathy/nanoGPT | `master` | Primary — minimal PyTorch GPT reference |
| MuJoCo | https://github.com/google-deepmind/mujoco | `main` | Comparative — physics engine release activity |
| LLaMA (legacy) | https://github.com/meta-llama/llama | deprecated | Excluded from Aug–Sep 2025 convergence; README-only Jan 2025 activity in harvest |

**LLaMA replacement (not yet analysed in this repo):** use Meta’s current Llama distribution and active recipe repositories when rebuilding the LLaMA leg of any convergence claim.

## Collection parameters

| Parameter | Value |
| --------- | ----- |
| Analysis window (primary) | 2025-08-01 → 2025-12-31 |
| Data type | Public `git log`, `git log -p` (selected paths), commit messages |
| Clone depth | Shallow clones (exact `--depth` per run not stored in all exports) |
| Author metadata | Email addresses redacted in public `data/` exports; see `data/redaction_mapping.csv` |
| Harvest location | Derived files under `timelines/`, `logs/`, `diffs/`, `data/` |

## Inclusion rules (infrastructure-related commits)

A commit is tagged **infrastructure-related** for cross-repo comparison when **any** of the following hold (keyword / path heuristic used in internal pipelines):

1. **dtype / precision:** message or diff touches `dtype`, `torch_dtype`, `fp16`, `bf16`, `fp8`, casting
2. **Attention:** `attention`, `flash_attn`, `sdpa`, `scaled_dot_product`
3. **Quantization:** `quant`, `bitsandbytes`, `awq`, `gguf`, `dequant`
4. **Config schema:** `config`, `generation`, `PretrainedConfig`, removal of config fields
5. **Excluded by default:** pure README, i18n-only, unrelated test-only churn unless paired with above signals

These rules are **heuristic**, not exhaustive. Competing explanations (release cadence, CI fixes, new model additions) were not fully eliminated in early drafts.

## Baselines and statistical testing

**Not yet published in this repository:**

- Null-model commit-rate baselines per repo
- Permutation tests for cross-repo same-day overlap
- Pre-registered inclusion/exclusion adjudication log

Temporal clustering alone is **necessary but not sufficient** for shared causation (`technical-note.md`).

## Reproduction steps (minimal)

```bash
# 1. Shallow clone a target repo
git clone --depth=500 https://github.com/huggingface/transformers /tmp/transformers

# 2. Daily commit burst CSV
./examples/analyze-commit-bursts.sh /tmp/transformers /tmp/transformers_bursts.csv

# 3. Filter infrastructure-related messages (example)
git -C /tmp/transformers log --since=2025-08-01 --until=2025-12-31 \
  --grep='dtype\|attention\|quant' -i --oneline

# 4. Compare date overlap with second repo (manual or script)
./examples/analyze-commit-bursts.sh /tmp/nanogpt /tmp/nanogpt_bursts.csv
```

## Published evidence pointers

| Artifact | Path |
| -------- | ---- |
| Per-repo timelines | `timelines/*.txt` |
| Synchronization notes | `metadata_notes/sync_matrix.txt` |
| Extracted diffs | `diffs/` |
| Assumption maps | `assumption_maps/` |
| Scope corrections | `LIMITATIONS.md` |

## Verification checklist for reviewers

- [ ] Confirm cited commit hashes exist at upstream URLs
- [ ] Confirm commit dates match upstream `git show -s --format=%ci <hash>`
- [ ] Separate Transformers/nanoGPT infrastructure signal from MuJoCo release work
- [ ] Confirm LLaMA timeline lacks Aug–Sep 2025 infrastructure commits before accepting four-way claims
- [ ] Read `LIMITATIONS.md` before interpreting strong causal language in older exports

## Licence

Documentation and analysis: CC-BY-4.0. Upstream code remains under respective project licences (`ATTRIBUTION.md`).
