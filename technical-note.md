# Technical Note: Methodology and Scope

**Repository:** ai-infrastructure-crisis-2025  
**Author:** Amy Ferguson, NZGPTS  
**Licence:** CC-BY-4.0

---

## What This Investigation Does

This repository documents a forensic analysis of public Git commit histories across four major AI repositories during 2025. The goal is to determine whether correlated infrastructure changes across independent projects during the same time window are consistent with a shared upstream dependency transition, or attributable to coincidence or independent causes.

The four repositories analysed are:

- **Transformers** (Hugging Face) — model framework
- **LLaMA** (Meta) — language model implementation
- **MuJoCo** (Google DeepMind) — physics simulation engine
- **nanoGPT** (independent) — educational GPT implementation

---

## Data Sources

All data is derived from publicly accessible Git commit histories. No proprietary, internal, or non-public information was used.

Sources include:

- Commit hashes, timestamps, and author metadata
- Commit message text
- Diff content (what changed in each commit)
- Configuration file snapshots at selected commits

No access to internal issue trackers, private communications, or unpublished roadmaps was sought or used.

---

## Internal Analysis Tools

This investigation was conducted using **deep_pattern_engines**, an active telemetry microservice integrated into the NZGPTS Node.js backend. The radar is powered by custom Bash shell pipelines executed via child processes that parse Git clones of major upstream repositories.

While the proprietary execution pipeline is not hosted in this public repository to protect internal infrastructure, the analysis outputs, methodologies, and raw data are provided here. The internal suite includes:

- **Bisector Engine** – uses `git log` and `awk` to search backwards through git history to identify exact breakage points.
- **Burst Detector** – calculates daily commit frequency arrays to identify sudden spikes in commit density.
- **Correlation Matrix** – compares timestamps of infrastructure-related commit clusters across repositories to calculate temporal overlap.
- **Schema Analyzer** – uses `grep` pipelines across historical code diffs to track the velocity at which configuration files and APIs shrink.

---

## Methodology Constraints

Several design decisions were made to limit inference error:

- Only patterns directly observable in commit history are reported. Internal decisions, roadmaps, and intent are not inferred.
- Correlation is documented, not causation. The analysis identifies consistent patterns; it does not claim to identify which specific upstream change caused downstream adaptation.
- The nanoGPT inactivity finding is treated as a pattern datum, not a narrative conclusion. Absence of commits is noted as consistent with the observed pressure; alternative explanations are acknowledged.
- Commit message language is used as a secondary signal only, not primary evidence.

---

## Limitations

- Commit history reflects what was committed and when, not when problems were first identified internally.
- Public repositories may not reflect the full scope of activity (private forks, internal branches).
- Temporal clustering is a necessary but not sufficient condition for shared causation.
- The upstream dependency identified (PyTorch / CUDA stack evolution) is the most parsimonious explanation consistent with the evidence; it is not independently confirmed by the upstream maintainers.

---

## Replication

All analysis is reproducible from public repository data. While the custom forensic engines remain internal to NZGPTS, independent researchers can verify the claims by cross-referencing the public commit hashes provided in the `/logs/` directory against the official upstream repositories. The methodology described here can be applied to other repositories or time windows.

---

## Relevance to Infrastructure Operators

Organisations operating AI-dependent workloads on managed or sovereign infrastructure should note that upstream dependency transitions of this type are not announced in advance and do not follow coordinated release schedules. The 2025 event involved a four-month gap between the onset of instability (August) and public-facing stabilisation (December).

Monitoring commit activity across upstream dependencies — rather than relying solely on release notes or vendor announcements — provides earlier signal of ecosystem-level transitions.

This has direct implications for infrastructure resilience planning, dependency management policy, and AI workload continuity strategies.
