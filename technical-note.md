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

Four purpose-built internal utilities (part of the proprietary NZGPTS platform) were used to conduct this research. While the tools themselves are not published in this repository, their functions are defined below:

**Bisector Engine** — performs backward search through commit history to identify the earliest commit associated with a class of changes. Analogous to `git bisect` but applied across repositories simultaneously.

**Burst Detector** — measures commit density over rolling time windows to identify periods of abnormal activity. Abnormality is defined relative to each repository's own baseline rate, not a fixed threshold.

**Correlation Matrix** — compares timestamps of infrastructure-related commit clusters across repositories to calculate temporal overlap. Used to assess whether clustering is consistent with shared causation.

**Schema Analyzer** — tracks configuration surface changes over time by counting exposed parameters in configuration files at defined snapshots. Used to quantify surface contraction as a defensive signal.

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
