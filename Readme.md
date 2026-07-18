# A Survey of World Model Benchmarks

[![Project Page](https://img.shields.io/badge/Project-Page-5965d8)](https://axbhb.github.io/world-model-evaluation-survey/) [![Benchmarks](https://img.shields.io/badge/Benchmarks-82-2f8f63)](https://axbhb.github.io/world-model-evaluation-survey/#benchmarks)

This repository accompanies **A Survey of World Model Benchmarks**. The latest manuscript covers **82 representative benchmarks** published from **2018–2026**; **43** span more than one evaluation-target category. The corpus was last checked in July 2026.

The repository and project page follow the paper’s four-dimensional taxonomy:

> **Evaluation Target × Evaluation Protocol × Evaluation Metrics × Evaluation Data**

## Latest taxonomy

| Dimension | Current coding |
|:--|:--|
| Evaluation Target | Seven categories listed below |
| Evaluation Protocol | `OL` = Open-Loop Evaluation; `CL` = Closed-Loop Interaction |
| Evaluation Metrics | `P` = Prediction-Level Metrics; `O` = Downstream Outcome Metrics |
| Evaluation Data | `RWD` = Real-World Data Collection; `SBG` = Simulation-Based Generation; `SPTC` = Scenario, Prompt, and Task Curation; `HCP` = Hybrid Construction Pipelines |

`OL+CL` and `P+O` indicate benchmark suites with tracks at both levels. `△` on the project page marks a cross-category benchmark.

## Evaluation-target coverage

| Evaluation target | Benchmarks |
|:--|--:|
| Visual & Temporal Quality | 20 |
| Spatial & State Consistency | 19 |
| Long-Horizon Memory & State Persistence | 11 |
| Physical Plausibility | 39 |
| Causal & Counterfactual Reasoning | 22 |
| Control Fidelity & Interactive Dynamics | 29 |
| Functional Utility | 8 |

Counts overlap because a benchmark may support more than one evaluation target. The latest Figure 4 adds **WR-Arena** to the Functional Utility → Planner branch. The corpus still contains 82 unique benchmarks and 43 cross-category benchmarks.

## Release timeline

| Release window | New benchmarks | Cumulative |
|:--|--:|--:|
| 2018–2021 | 7 | 7 |
| 2022–2023 | 7 | 14 |
| 2024 | 12 | 26 |
| 2025 | 29 | 55 |
| 2026 | 27 | 82 |

## Canonical benchmark data

To prevent the README, website, and manuscript tables from drifting apart, benchmark-level metadata is maintained in one canonical manifest rather than duplicated across hand-edited Markdown tables:

- [Interactive benchmark explorer](https://axbhb.github.io/world-model-evaluation-survey/#benchmarks)
- [`docs/assets/benchmarks.json`](docs/assets/benchmarks.json): all 82 benchmark records, target and sub-target memberships, protocol, metric level, data source, year, and domain
- [`docs/assets/metadata.json`](docs/assets/metadata.json): taxonomy labels and release-window definitions

The project page derives its filters, Target × Protocol matrix, timeline, target-by-period breakdown, and benchmark cards from these files.
