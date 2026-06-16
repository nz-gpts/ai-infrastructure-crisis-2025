Examples: minimal reproducibility recipes
======================================

This folder contains a small, non‑proprietary example that demonstrates the core pattern-detection primitive used in the analysis: measuring commit-frequency bursts from a shallow clone.

Files
- `analyze-commit-bursts.sh` — minimal Bash script that computes daily commit counts from a git repository and emits CSV (date,count).

Quickstart
1. Shallow-clone a public repository:

   git clone --depth 1 https://github.com/<owner>/<repo>.git

2. Run the script inside the cloned repo:

   cd <repo>
   ../examples/analyze-commit-bursts.sh . output.csv

3. Inspect `output.csv` to see daily commit counts. Use this time series to detect burst periods (sudden spikes in daily counts).

Notes
- This example is intentionally small and non‑proprietary. It demonstrates the low‑cost, Unix‑philosophy approach (git + awk + grep) used to build higher‑level metrics (burst detector, correlation windows) without publishing the internal telemetry engine.
- To reproduce the full investigation, run similar pipelines across all target repositories, align timestamps, and compute cross-repo correlation metrics.

