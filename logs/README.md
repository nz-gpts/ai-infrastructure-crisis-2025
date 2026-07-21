# Logs directory

This folder holds commit extracts and snapshot references used in the cross-repository analysis.

## Placeholder files

Files named `*_PLACEHOLDER.txt` mark **unpublished snapshot slots**. They are not evidence. Do not cite them in reproduction or external review.

| File | Intended content |
| ---- | ---------------- |
| `TRANSFORMERS_PLACEHOLDER.txt` | Frozen `git log` export for Hugging Face Transformers at collection time |
| `LLAMA_PLACEHOLDER.txt` | Frozen export for legacy `meta-llama/llama` |
| `MUJOCO_PLACEHOLDER.txt` | Frozen export for `google-deepmind/mujoco` |
| `NANOGPT_PLACEHOLDER.txt` | Frozen export for `karpathy/nanoGPT` |

Populated exports live under `timelines/` and `data/`. See `reproducibility/MANIFEST.md` for collection parameters.
