# A Survey of World Model Benchmarks

[![Project Page](https://img.shields.io/badge/Project-Page-5965d8)](https://axbhb.github.io/world-model-evaluation-survey/) [![Benchmarks](https://img.shields.io/badge/Benchmarks-82-2f8f63)](https://axbhb.github.io/world-model-evaluation-survey/#benchmarks)

This repository accompanies **A Survey of World Model Benchmarks**. The latest manuscript contains **82 representative benchmarks** from **2018–2026**; **43** span multiple evaluation-target categories.

The project page follows the paper’s four-dimensional taxonomy: **Evaluation Target × Evaluation Protocol × Evaluation Metrics × Evaluation Data**.

Rows are intentionally repeated across target tables. `△` marks a cross-category benchmark. The corpus was last checked in July 2026.

## Contents
- [Visual and Temporal Quality](#visual-and-temporal-quality)
- [Spatial and State Consistency](#spatial-and-state-consistency)
- [Long-Horizon Memory and State Persistence](#long-horizon-memory-and-state-persistence)
- [Physical Plausibility](#physical-plausibility)
- [Causal and Counterfactual Reasoning](#causal-and-counterfactual-reasoning)
- [Control Fidelity and Interactive Dynamics](#control-fidelity-and-interactive-dynamics)
- [Functional Utility](#functional-utility)

## Column conventions

| Dimension | Codes | Meaning |
|:--|:--|:--|
| Protocol | `OL` / `CR` / `CL` | Open-Loop Prediction / Controlled Rollout / Closed-Loop Interaction |
| Metrics | `A` / `J` / `O` | Automatic / Judge-Based / Outcome-Grounded Metrics |
| Data | `RWD` / `SBG` / `SPTC` / `HCP` | Real-World Data Collection / Simulation-Based Generation / Scenario, Prompt, and Task Curation / Hybrid Construction Pipelines |

## Visual and Temporal Quality

_Aligned with Figure 4 and Tables 3–9 of the latest manuscript._

| Benchmark | Year | Domain | Protocol | Metrics | Data |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**FETV**](https://scholar.google.com/scholar?q=FETV%3A%20A%20benchmark%20for%20fine-grained%20evaluation%20of%20open-domain%20text-to-video%20generation) | 2023 | video | OL | A+J | SPTC |
| [**VBench △**](https://scholar.google.com/scholar?q=VBench%3A%20Comprehensive%20benchmark%20suite%20for%20video%20generative%20models) | 2024 | video | OL | A | SPTC |
| [**VBench++ △**](https://arxiv.org/abs/2411.13503) | 2024 | video | OL | A | SPTC |
| [**EvalCrafter**](https://scholar.google.com/scholar?q=EvalCrafter%3A%20Benchmarking%20and%20evaluating%20large%20video%20generation%20models) | 2024 | video | OL | A+J | SPTC |
| [**ChronoMagic-Bench**](https://scholar.google.com/scholar?q=ChronoMagic-Bench%3A%20A%20benchmark%20for%20metamorphic%20evaluation%20of%20text-to-time-lapse%20video%20generation) | 2024 | video | OL | A+J | SPTC |
| [**WorldScore △**](https://scholar.google.com/scholar?q=WorldScore%3A%20A%20unified%20evaluation%20benchmark%20for%20world%20generation) | 2025 | video | CR | A+J | HCP |
| [**VMBench**](https://arxiv.org/abs/2503.10076) | 2025 | video | OL | A | SPTC |
| [**EWMBench △**](https://arxiv.org/abs/2505.09694) | 2025 | embodied | CR | A+J | HCP |
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | embodied | OL+CL | A+J+O | SBG |
| [**GameWorld Score △**](https://arxiv.org/abs/2506.18701) | 2025 | game | CL | A+J | SBG |
| [**WorldMark △**](https://arxiv.org/abs/2604.21686) | 2026 | game+video | OL+CL | A+J | SBG |
| [**4DWorldBench △**](https://arxiv.org/abs/2511.19836) | 2025 | video | CR | A+J | HCP |
| [**TC-Bench △**](https://arxiv.org/abs/2406.08656) | 2024 | video | CR | A+J | HCP |
| [**WorldLens △**](https://arxiv.org/abs/2512.10958) | 2026 | driving | OL+CL | A+J+O | HCP |
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | embodied | OL+CL | A+J+O | HCP |
| [**DrivingGen △**](https://arxiv.org/abs/2601.01528) | 2026 | driving | CR | A+J | RWD |
| [**WBench △**](https://arxiv.org/abs/2605.25874) | 2026 | video | CL | A+J | HCP |
| [**Pedestrian sim.**](https://arxiv.org/abs/2510.20182) | 2025 | video | OL | A | RWD |
| [**Gen-ViRe**](https://arxiv.org/abs/2511.13853) | 2025 | video | OL | J | HCP |
| [**iWorld-Bench △**](https://arxiv.org/abs/2605.03941) | 2026 | video | CR | A | HCP |

## Spatial and State Consistency

_Aligned with Figure 4 and Tables 3–9 of the latest manuscript._

| Benchmark | Year | Domain | Protocol | Metrics | Data |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**VBench △**](https://scholar.google.com/scholar?q=VBench%3A%20Comprehensive%20benchmark%20suite%20for%20video%20generative%20models) | 2024 | video | OL | A | SPTC |
| [**VBench++ △**](https://arxiv.org/abs/2411.13503) | 2024 | video | OL | A | SPTC |
| [**WorldMark △**](https://arxiv.org/abs/2604.21686) | 2026 | game+video | OL+CL | A+J | SBG |
| [**WorldLens △**](https://arxiv.org/abs/2512.10958) | 2026 | driving | OL+CL | A+J+O | HCP |
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | embodied | OL+CL | A+J+O | SBG |
| [**WorldScore △**](https://scholar.google.com/scholar?q=WorldScore%3A%20A%20unified%20evaluation%20benchmark%20for%20world%20generation) | 2025 | video | CR | A+J | HCP |
| [**DrivingGen △**](https://arxiv.org/abs/2601.01528) | 2026 | driving | CR | A+J | RWD |
| [**EWMBench △**](https://arxiv.org/abs/2505.09694) | 2025 | embodied | CR | A+J | HCP |
| [**What-If World △**](https://arxiv.org/abs/2605.27589) | 2026 | driving+embodied | CR | J | RWD |
| [**4DWorldBench △**](https://arxiv.org/abs/2511.19836) | 2025 | video | CR | A+J | HCP |
| [**GameWorld Score △**](https://arxiv.org/abs/2506.18701) | 2025 | game | CL | A+J | SBG |
| [**LoopNav**](https://arxiv.org/abs/2505.22976) | 2025 | game | CR | A | SBG |
| [**MIND △**](https://arxiv.org/abs/2602.08025) | 2026 | video | OL+CL | A | SBG |
| [**MBench △**](https://arxiv.org/abs/2606.00793) | 2026 | video | OL | A+J | RWD |
| [**STEVO-Bench △**](https://arxiv.org/abs/2603.13215) | 2026 | video | CR | J | HCP |
| [**CausalSpatial △**](https://arxiv.org/abs/2601.13304) | 2026 | image | CR | A | SBG |
| [**PDI-Bench △**](https://arxiv.org/abs/2605.15185) | 2026 | video | OL | A | HCP |
| [**WorldOlympiad △**](https://arxiv.org/abs/2606.11129) | 2026 | video | OL+CR | A+J | HCP |
| [**HOCA-Bench △**](https://arxiv.org/abs/2602.19571) | 2026 | video | OL | J | HCP |

## Long-Horizon Memory and State Persistence

_Aligned with Figure 4 and Tables 3–9 of the latest manuscript._

| Benchmark | Year | Domain | Protocol | Metrics | Data |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**WorldPrediction △**](https://arxiv.org/abs/2506.04363) | 2025 | video | OL | A | RWD |
| [**SmallWorlds**](https://arxiv.org/abs/2511.23465) | 2025 | video | OL | A | SBG |
| [**WR-Arena △**](https://arxiv.org/abs/2603.25887) | 2026 | driving+embodied | CR+CL | A+J+O | RWD |
| [**WorldMark △**](https://arxiv.org/abs/2604.21686) | 2026 | game+video | OL+CL | A+J | SBG |
| [**MBench △**](https://arxiv.org/abs/2606.00793) | 2026 | video | OL | A+J | RWD |
| [**MIND △**](https://arxiv.org/abs/2602.08025) | 2026 | video | OL+CL | A | SBG |
| [**WBench △**](https://arxiv.org/abs/2605.25874) | 2026 | video | CL | A+J | HCP |
| [**WorldOlympiad △**](https://arxiv.org/abs/2606.11129) | 2026 | video | OL+CR | A+J | HCP |
| [**HTEWorld**](https://arxiv.org/abs/2605.19957) | 2026 | embodied | CR | A | SBG |
| [**RoboWM-Bench △**](https://arxiv.org/abs/2604.19092) | 2026 | embodied | CL | A+O | HCP |
| [**iWorld-Bench △**](https://arxiv.org/abs/2605.03941) | 2026 | video | CR | A | HCP |

## Physical Plausibility

_Aligned with Figure 4 and Tables 3–9 of the latest manuscript._

| Benchmark | Year | Domain | Protocol | Metrics | Data |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**IntPhys**](https://arxiv.org/abs/1803.07616) | 2018 | video | OL | A | SBG |
| [**IntPhys 2**](https://arxiv.org/abs/2506.09849) | 2025 | video | OL | A | SBG |
| [**CLEVRER △**](https://scholar.google.com/scholar?q=CLEVRER%3A%20Collision%20events%20for%20video%20representation%20and%20reasoning) | 2020 | video | OL | A | SBG |
| [**CoPhy △**](https://scholar.google.com/scholar?q=CoPhy%3A%20Counterfactual%20learning%20of%20physical%20dynamics) | 2020 | video | CR | A | SBG |
| [**PHYRE**](https://scholar.google.com/scholar?q=PHYRE%3A%20A%20new%20benchmark%20for%20physical%20reasoning) | 2019 | video | CL | A+O | SBG |
| [**CRAFT △**](https://scholar.google.com/scholar?q=CRAFT%3A%20A%20benchmark%20for%20causal%20reasoning%20about%20forces%20and%20interactions) | 2022 | video | CR | A | SBG |
| [**Physion △**](https://scholar.google.com/scholar?q=Physion%3A%20Evaluating%20physical%20prediction%20from%20vision%20in%20humans%20and%20machines) | 2021 | video | OL | A | SBG |
| [**Physion++**](https://scholar.google.com/scholar?q=Physion%2B%2B%3A%20Evaluating%20physical%20scene%20understanding%20that%20requires%20online%20inference%20of%20different%20physical%20properties) | 2023 | video | OL | A | SBG |
| [**ComPhy △**](https://scholar.google.com/scholar?q=ComPhy%3A%20Compositional%20physical%20reasoning%20of%20objects%20and%20events%20from%20videos) | 2022 | video | CR | A | SBG |
| [**ContPhy**](https://scholar.google.com/scholar?q=ContPhy%3A%20Continuum%20physical%20concept%20learning%20and%20reasoning%20from%20videos) | 2024 | video | OL | A | SBG |
| [**PhyCoBench**](https://arxiv.org/abs/2502.05503) | 2025 | video | OL | A+J | SPTC |
| [**VideoPhy △**](https://arxiv.org/abs/2406.03520) | 2024 | video | CR | J | SPTC |
| [**VideoPhy-2 △**](https://arxiv.org/abs/2503.06800) | 2025 | video | CR | J | SPTC |
| [**PhyGenBench △**](https://arxiv.org/abs/2410.05363) | 2024 | video | CR | J | SPTC |
| [**T2VPhysBench**](https://arxiv.org/abs/2505.00337) | 2025 | video | CR | J | SPTC |
| [**Physics-IQ △**](https://arxiv.org/abs/2501.09038) | 2025 | video | OL | A+J | RWD |
| [**WorldBench**](https://arxiv.org/abs/2601.21282) | 2026 | video | OL | A | HCP |
| [**PhyWorldBench △**](https://arxiv.org/abs/2507.13428) | 2025 | video | CR | J | SPTC |
| [**WorldOlympiad △**](https://arxiv.org/abs/2606.11129) | 2026 | video | OL+CR | A+J | HCP |
| [**ACWM-Phys △**](https://arxiv.org/abs/2605.08567) | 2026 | video | CR | A | SBG |
| [**WorldModelBench △**](https://arxiv.org/abs/2502.20694) | 2025 | video | OL | J | SPTC |
| [**VBench-2.0 △**](https://arxiv.org/abs/2503.21755) | 2025 | video | OL | A+J | SPTC |
| [**GameWorld Score △**](https://arxiv.org/abs/2506.18701) | 2025 | game | CL | A+J | SBG |
| [**T2VWorldBench △**](https://arxiv.org/abs/2507.18107) | 2025 | video | OL | J | SPTC |
| [**4DWorldBench △**](https://arxiv.org/abs/2511.19836) | 2025 | video | CR | A+J | HCP |
| [**RoboWM-Bench △**](https://arxiv.org/abs/2604.19092) | 2026 | embodied | CL | A+O | HCP |
| [**DreamGen Bench △**](https://arxiv.org/abs/2505.12705) | 2025 | embodied | OL | J | HCP |
| [**WorldLens △**](https://arxiv.org/abs/2512.10958) | 2026 | driving | OL+CL | A+J+O | HCP |
| [**RigidBench**](https://scholar.google.com/scholar?q=Rigidbench%3A%20Evaluating%20rigid-body%20physics%20in%20video%20generation%20models) | 2026 | video | OL | A | SBG |
| [**Morpheus**](https://arxiv.org/abs/2504.02918) | 2025 | video | OL | A | RWD |
| [**What-If World △**](https://arxiv.org/abs/2605.27589) | 2026 | driving+embodied | CR | J | RWD |
| [**PhyGround**](https://arxiv.org/abs/2605.10806) | 2026 | video | OL | J | SPTC |
| [**Physion-Eval**](https://arxiv.org/abs/2603.19607) | 2026 | video | OL | J | HCP |
| [**CRONOS △**](https://arxiv.org/abs/2605.23699) | 2026 | video | CR | A+J | HCP |
| [**VACT △**](https://arxiv.org/abs/2503.06163) | 2025 | video | CR | A+J | SPTC |
| [**STEVO-Bench △**](https://arxiv.org/abs/2603.13215) | 2026 | video | CR | J | HCP |
| [**PhysicsMind**](https://arxiv.org/abs/2601.16007) | 2026 | video | OL | A | HCP |
| [**PDI-Bench △**](https://arxiv.org/abs/2605.15185) | 2026 | video | OL | A | HCP |
| [**HOCA-Bench △**](https://arxiv.org/abs/2602.19571) | 2026 | video | OL | J | HCP |

## Causal and Counterfactual Reasoning

_Aligned with Figure 4 and Tables 3–9 of the latest manuscript._

### Causal Reasoning over Observed Worlds

| Benchmark | Year | Domain | Protocol | Metrics | Data |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**CLEVRER △**](https://scholar.google.com/scholar?q=CLEVRER%3A%20Collision%20events%20for%20video%20representation%20and%20reasoning) | 2020 | video | OL | A | SBG |
| [**CATER**](https://scholar.google.com/scholar?q=CATER%3A%20A%20diagnostic%20dataset%20for%20compositional%20actions%20and%20temporal%20reasoning) | 2020 | video | OL | A | SBG |
| [**NExT-QA**](https://arxiv.org/abs/2105.08276) | 2021 | video | OL | A | RWD |
| [**Causal-VidQA**](https://arxiv.org/abs/2205.14895) | 2022 | video | CR | A | RWD |
| [**CRAFT △**](https://scholar.google.com/scholar?q=CRAFT%3A%20A%20benchmark%20for%20causal%20reasoning%20about%20forces%20and%20interactions) | 2022 | video | CR | A | SBG |
| [**IntentQA**](https://scholar.google.com/scholar?q=IntentQA%3A%20Context-aware%20video%20intent%20reasoning) | 2023 | video | OL | A | RWD |
| [**MMWorld**](https://scholar.google.com/scholar?q=MMWorld%3A%20Towards%20multi-discipline%20multi-faceted%20world%20model%20evaluation%20in%20videos) | 2025 | video | CR | A+J | HCP |
| [**VCRBench**](https://arxiv.org/abs/2505.08455) | 2025 | video | OL | A | RWD |
| [**Physion △**](https://scholar.google.com/scholar?q=Physion%3A%20Evaluating%20physical%20prediction%20from%20vision%20in%20humans%20and%20machines) | 2021 | video | OL | A | SBG |
| [**Physics-IQ △**](https://arxiv.org/abs/2501.09038) | 2025 | video | OL | A+J | RWD |
| [**WorldPrediction △**](https://arxiv.org/abs/2506.04363) | 2025 | video | OL | A | RWD |
| [**WR-Arena △**](https://arxiv.org/abs/2603.25887) | 2026 | driving+embodied | CR+CL | A+J+O | RWD |
| [**CausalSpatial △**](https://arxiv.org/abs/2601.13304) | 2026 | image | CR | A | SBG |
| [**T2VWorldBench △**](https://arxiv.org/abs/2507.18107) | 2025 | video | OL | J | SPTC |
| [**VACT △**](https://arxiv.org/abs/2503.06163) | 2025 | video | CR | A+J | SPTC |
| [**HOCA-Bench △**](https://arxiv.org/abs/2602.19571) | 2026 | video | OL | J | HCP |

### Counterfactual Reasoning over Intervened Worlds

| Benchmark | Year | Domain | Protocol | Metrics | Data |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**CoPhy △**](https://scholar.google.com/scholar?q=CoPhy%3A%20Counterfactual%20learning%20of%20physical%20dynamics) | 2020 | video | CR | A | SBG |
| [**ComPhy △**](https://scholar.google.com/scholar?q=ComPhy%3A%20Compositional%20physical%20reasoning%20of%20objects%20and%20events%20from%20videos) | 2022 | video | CR | A | SBG |
| [**ACQUIRED**](https://arxiv.org/abs/2311.01620) | 2023 | video | CR | A | RWD |
| [**CausalVQA**](https://arxiv.org/abs/2506.09943) | 2025 | video | CR | A | RWD |
| [**What-If World △**](https://arxiv.org/abs/2605.27589) | 2026 | driving+embodied | CR | J | RWD |
| [**CRONOS △**](https://arxiv.org/abs/2605.23699) | 2026 | video | CR | A+J | HCP |

## Control Fidelity and Interactive Dynamics

_Aligned with Figure 4 and Tables 3–9 of the latest manuscript._

### Pre-specified Control Fidelity

| Benchmark | Year | Domain | Protocol | Metrics | Data |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**T2V-CompBench**](https://scholar.google.com/scholar?q=T2VCompBench%3A%20A%20comprehensive%20benchmark%20for%20compositional%20textto-video%20generation) | 2025 | video | CR | A+J | SPTC |
| [**TC-Bench △**](https://arxiv.org/abs/2406.08656) | 2024 | video | CR | A+J | HCP |
| [**StoryEval**](https://arxiv.org/abs/2412.16211) | 2024 | video | CR | J | SPTC |
| [**VideoPhy △**](https://arxiv.org/abs/2406.03520) | 2024 | video | CR | J | SPTC |
| [**VideoPhy-2 △**](https://arxiv.org/abs/2503.06800) | 2025 | video | CR | J | SPTC |
| [**PhyGenBench △**](https://arxiv.org/abs/2410.05363) | 2024 | video | CR | J | SPTC |
| [**PhyWorldBench △**](https://arxiv.org/abs/2507.13428) | 2025 | video | CR | J | SPTC |
| [**OSCBench**](https://arxiv.org/abs/2603.11698) | 2026 | video | CR | J | SPTC |
| [**MoveBench**](https://arxiv.org/abs/2512.08765) | 2025 | video | CR | A+J | RWD |
| [**MagicBench**](https://arxiv.org/abs/2503.16421) | 2025 | video | CR | A | RWD |
| [**WorldScore △**](https://scholar.google.com/scholar?q=WorldScore%3A%20A%20unified%20evaluation%20benchmark%20for%20world%20generation) | 2025 | video | CR | A+J | HCP |
| [**4DWorldBench △**](https://arxiv.org/abs/2511.19836) | 2025 | video | CR | A+J | HCP |
| [**DrivingGen △**](https://arxiv.org/abs/2601.01528) | 2026 | driving | CR | A+J | RWD |
| [**ACT-Bench**](https://arxiv.org/abs/2412.05337) | 2024 | driving | CR | A | RWD |
| [**What-If World △**](https://arxiv.org/abs/2605.27589) | 2026 | driving+embodied | CR | J | RWD |
| [**Omni-WorldBench**](https://arxiv.org/abs/2603.22212) | 2026 | video | CR | A+J | HCP |
| [**DreamGen Bench △**](https://arxiv.org/abs/2505.12705) | 2025 | embodied | OL | J | HCP |
| [**WorldModelBench △**](https://arxiv.org/abs/2502.20694) | 2025 | video | OL | J | SPTC |
| [**VBench-2.0 △**](https://arxiv.org/abs/2503.21755) | 2025 | video | OL | A+J | SPTC |

### Interactive Action Fidelity

| Benchmark | Year | Domain | Protocol | Metrics | Data |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**WorldMark △**](https://arxiv.org/abs/2604.21686) | 2026 | game+video | OL+CL | A+J | SBG |
| [**WR-Arena △**](https://arxiv.org/abs/2603.25887) | 2026 | driving+embodied | CR+CL | A+J+O | RWD |
| [**WorldSimBench △**](https://arxiv.org/abs/2410.18072) | 2024 | game+driving+embodied | OL+CL | A+J+O | HCP |
| [**WBench △**](https://arxiv.org/abs/2605.25874) | 2026 | video | CL | A+J | HCP |
| [**iWorld-Bench △**](https://arxiv.org/abs/2605.03941) | 2026 | video | CR | A | HCP |
| [**MIND △**](https://arxiv.org/abs/2602.08025) | 2026 | video | OL+CL | A | SBG |
| [**ACWM-Phys △**](https://arxiv.org/abs/2605.08567) | 2026 | video | CR | A | SBG |
| [**RoboWM-Bench △**](https://arxiv.org/abs/2604.19092) | 2026 | embodied | CL | A+O | HCP |
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | embodied | OL+CL | A+J+O | HCP |
| [**WorldOlympiad △**](https://arxiv.org/abs/2606.11129) | 2026 | video | OL+CR | A+J | HCP |

## Functional Utility

_Aligned with Figure 4 and Tables 3–9 of the latest manuscript._

### Data Engine

| Benchmark | Year | Domain | Protocol | Metrics | Data |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | embodied | OL+CL | A+J+O | SBG |
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | embodied | OL+CL | A+J+O | HCP |

### Policy Evaluator

| Benchmark | Year | Domain | Protocol | Metrics | Data |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | embodied | OL+CL | A+J+O | SBG |

### Planner

| Benchmark | Year | Domain | Protocol | Metrics | Data |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | embodied | OL+CL | A+J+O | SBG |
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | embodied | OL+CL | A+J+O | HCP |
| [**World-in-World**](https://arxiv.org/abs/2510.18135) | 2025 | embodied | CL | A+J+O | HCP |
| [**EVA-Bench**](https://arxiv.org/abs/2410.15461) | 2024 | embodied | OL | A+J | HCP |
| [**WorldLens △**](https://arxiv.org/abs/2512.10958) | 2026 | driving | OL+CL | A+J+O | HCP |
| [**RoboWM-Bench △**](https://arxiv.org/abs/2604.19092) | 2026 | embodied | CL | A+O | HCP |
| [**WorldSimBench △**](https://arxiv.org/abs/2410.18072) | 2024 | game+driving+embodied | OL+CL | A+J+O | HCP |

### Interactive Training Environment

| Benchmark | Year | Domain | Protocol | Metrics | Data |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | embodied | OL+CL | A+J+O | HCP |

## Machine-readable data

- [`docs/assets/benchmarks.json`](docs/assets/benchmarks.json): compact canonical manifest used by the explorer
- [Interactive project page](https://axbhb.github.io/world-model-evaluation-survey/)
