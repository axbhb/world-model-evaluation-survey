# A Survey of World Model Benchmarks

[![Project Page](https://img.shields.io/badge/Project-Page-5965d8)](https://axbhb.github.io/world-model-evaluation-survey/) [![Benchmarks](https://img.shields.io/badge/Benchmarks-82-2f8f63)](https://axbhb.github.io/world-model-evaluation-survey/#benchmarks)

This repository accompanies **A Survey of World Model Benchmarks**. The latest manuscript covers **82 representative benchmarks** published from **2018–2026**; **43** span more than one evaluation-target category. The corpus was last checked in July 2026.

The repository and project page follow the paper’s four-dimensional taxonomy: **Evaluation Target × Evaluation Protocol × Evaluation Metrics × Evaluation Data**.

## Coding conventions

| Dimension | Codes |
|:--|:--|
| Evaluation Target | `T1` Visual & Temporal Quality; `T2` Spatial & State Consistency; `T3` Long-Horizon Memory & State Persistence; `T4` Physical Plausibility; `T5` Causal & Counterfactual Reasoning; `T6` Control Fidelity & Interactive Dynamics; `T7` Functional Utility |
| Evaluation Protocol | `OL` Open-Loop Evaluation; `CL` Closed-Loop Interaction |
| Evaluation Metrics | `P` Prediction-Level Metrics; `O` Downstream Outcome Metrics |
| Evaluation Data | `RWD` Real-World Data Collection; `SBG` Simulation-Based Generation; `SPTC` Scenario, Prompt, and Task Curation; `HCP` Hybrid Construction Pipelines |

`OL+CL`, `P+O`, and multi-target codes indicate suites that span both levels or multiple targets.

## Canonical 82-benchmark corpus

| Benchmark | Year | Domain | Target(s) | Protocol | Metrics | Data |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|
| **IntPhys** | 2018 | video | T4 | OL | P | SBG |
| **PHYRE** | 2019 | video | T4 | CL | O | SBG |
| **CATER** | 2020 | video | T5 | OL | P | SBG |
| **CLEVRER △** | 2020 | video | T4+T5 | OL | P | SBG |
| **CoPhy △** | 2020 | video | T4+T5 | OL | P | SBG |
| **NExT-QA** | 2021 | video | T5 | OL | P | RWD |
| **Physion △** | 2021 | video | T4+T5 | OL | P | SBG |
| **Causal-VidQA** | 2022 | video | T5 | OL | P | RWD |
| **ComPhy △** | 2022 | video | T4+T5 | OL | P | SBG |
| **CRAFT △** | 2022 | video | T4+T5 | OL | P | SBG |
| **ACQUIRED** | 2023 | video | T5 | OL | P | RWD |
| **FETV** | 2023 | video | T1 | OL | P | SPTC |
| **IntentQA** | 2023 | video | T5 | OL | P | RWD |
| **Physion++** | 2023 | video | T4 | OL | P | SBG |
| **ACT-Bench** | 2024 | driving | T6 | OL | P | RWD |
| **ChronoMagic-Bench** | 2024 | video | T1 | OL | P | SPTC |
| **ContPhy** | 2024 | video | T4 | OL | P | SBG |
| **EVA-Bench** | 2024 | embodied | T7 | OL | O | HCP |
| **EvalCrafter** | 2024 | video | T1 | OL | P | SPTC |
| **PhyGenBench △** | 2024 | video | T4+T6 | OL | P | SPTC |
| **StoryEval** | 2024 | video | T6 | OL | P | SPTC |
| **TC-Bench △** | 2024 | video | T1+T6 | OL | P | HCP |
| **VBench △** | 2024 | video | T1+T2 | OL | P | SPTC |
| **VBench++ △** | 2024 | video | T1+T2 | OL | P | SPTC |
| **VideoPhy △** | 2024 | video | T4+T6 | OL | P | SPTC |
| **WorldSimBench △** | 2024 | game+driving+embodied | T6+T7 | OL+CL | P+O | HCP |
| **4DWorldBench △** | 2025 | video | T1+T2+T4+T6 | OL | P | HCP |
| **CausalVQA** | 2025 | video | T5 | OL | P | RWD |
| **DreamGen Bench △** | 2025 | embodied | T4+T6 | OL | P | HCP |
| **EWMBench △** | 2025 | embodied | T1+T2 | OL | P | HCP |
| **GameWorld Score △** | 2025 | game | T1+T2+T4 | OL | P | SBG |
| **Gen-ViRe** | 2025 | video | T1 | OL | P | HCP |
| **IntPhys 2** | 2025 | video | T4 | OL | P | SBG |
| **LoopNav** | 2025 | game | T2 | OL | P | SBG |
| **MagicBench** | 2025 | video | T6 | OL | P | RWD |
| **MMWorld** | 2025 | video | T5 | OL | P | HCP |
| **Morpheus** | 2025 | video | T4 | OL | P | RWD |
| **MoveBench** | 2025 | video | T6 | OL | P | RWD |
| **PEDRA** | 2025 | video | T1 | OL | P | RWD |
| **PhyCoBench** | 2025 | video | T4 | OL | P | SPTC |
| **Physics-IQ △** | 2025 | video | T4+T5 | OL | P | RWD |
| **PhyWorldBench △** | 2025 | video | T4+T6 | OL | P | SPTC |
| **SmallWorlds** | 2025 | video | T3 | OL | P | SBG |
| **T2V-CompBench** | 2025 | video | T6 | OL | P | SPTC |
| **T2VPhysBench** | 2025 | video | T4 | OL | P | SPTC |
| **T2VWorldBench △** | 2025 | video | T4+T5 | OL | P | SPTC |
| **VACT △** | 2025 | video | T4+T5 | OL | P | SPTC |
| **VBench-2.0 △** | 2025 | video | T4+T6 | OL | P | SPTC |
| **VCRBench** | 2025 | video | T5 | OL | P | RWD |
| **VideoPhy-2 △** | 2025 | video | T4+T6 | OL | P | SPTC |
| **VMBench** | 2025 | video | T1 | OL | P | SPTC |
| **World-in-World** | 2025 | embodied | T7 | CL | O | HCP |
| **WorldModelBench △** | 2025 | video | T4+T6 | OL | P | SPTC |
| **WorldPrediction △** | 2025 | video | T3+T5 | OL | P | RWD |
| **WorldScore △** | 2025 | video | T1+T2+T6 | OL | P | HCP |
| **ACWM-Phys △** | 2026 | video | T4+T6 | OL | P | SBG |
| **CausalSpatial △** | 2026 | image | T2+T5 | OL | P | SBG |
| **CRONOS △** | 2026 | video | T4+T5 | OL | P | HCP |
| **DrivingGen △** | 2026 | driving | T1+T2+T6 | OL | P | RWD |
| **HOCA-Bench △** | 2026 | video | T2+T4+T5 | OL | P | HCP |
| **HTEWorld** | 2026 | embodied | T3 | OL | P | SBG |
| **iWorld-Bench △** | 2026 | video | T1+T3+T6 | OL | P | HCP |
| **MBench △** | 2026 | video | T2+T3 | OL | P | RWD |
| **MIND △** | 2026 | video | T2+T3+T6 | OL | P | SBG |
| **Omni-WorldBench** | 2026 | video | T6 | OL | P | HCP |
| **OSCBench** | 2026 | video | T6 | OL | P | SPTC |
| **PDI-Bench △** | 2026 | video | T2+T4 | OL | P | HCP |
| **PhyGround** | 2026 | video | T4 | OL | P | SPTC |
| **PhysicsMind** | 2026 | video | T4 | OL | P | HCP |
| **Physion-Eval** | 2026 | video | T4 | OL | P | HCP |
| **RigidBench** | 2026 | video | T4 | OL | P | SBG |
| **RoboWM-Bench △** | 2026 | embodied | T3+T4+T6+T7 | OL | O | HCP |
| **STEVO-Bench △** | 2026 | video | T2+T4 | OL | P | HCP |
| **WBench △** | 2026 | video | T1+T3+T6 | OL | P | HCP |
| **What-If World △** | 2026 | driving+embodied | T2+T4+T5+T6 | OL | P | RWD |
| **WorldArena △** | 2026 | embodied | T1+T2+T7 | OL+CL | P+O | SBG |
| **WorldArena 2.0 △** | 2026 | embodied | T1+T6+T7 | OL+CL | P+O | HCP |
| **WorldBench** | 2026 | video | T4 | OL | P | HCP |
| **WorldLens △** | 2026 | driving | T1+T2+T4+T7 | OL+CL | P+O | HCP |
| **WorldMark △** | 2026 | game+video | T1+T2+T3+T6 | OL | P | HCP |
| **WorldOlympiad △** | 2026 | video | T2+T3+T4+T6 | OL | P | HCP |
| **WR-Arena △** | 2026 | driving+embodied | T3+T5+T6+T7 | OL | P | HCP |

## Coverage summary

| Evaluation target | Benchmarks |
|:--|--:|
| Visual & Temporal Quality (`T1`) | 20 |
| Spatial & State Consistency (`T2`) | 19 |
| Long-Horizon Memory & State Persistence (`T3`) | 11 |
| Physical Plausibility (`T4`) | 39 |
| Causal & Counterfactual Reasoning (`T5`) | 22 |
| Control Fidelity & Interactive Dynamics (`T6`) | 29 |
| Functional Utility (`T7`) | 8 |

Counts overlap because cross-category benchmarks appear under more than one target. The latest Figure 4 adds **WR-Arena** to the Functional Utility → Planner branch.

## Machine-readable data

- [Interactive benchmark explorer](https://axbhb.github.io/world-model-evaluation-survey/#benchmarks)
- [`docs/assets/benchmarks.json`](docs/assets/benchmarks.json): canonical record and sub-target manifest
- [`docs/assets/metadata.json`](docs/assets/metadata.json): taxonomy labels and release-window definitions
