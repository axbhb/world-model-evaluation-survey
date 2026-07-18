# A Survey of World Model Benchmarks

[![Project Page](https://img.shields.io/badge/Project-Page-5965d8)](https://axbhb.github.io/world-model-evaluation-survey/) [![Benchmarks](https://img.shields.io/badge/Benchmarks-82-2f8f63)](https://axbhb.github.io/world-model-evaluation-survey/#benchmarks)

This repository accompanies **A Survey of World Model Benchmarks**. The latest manuscript covers **82 representative benchmarks** published from **2018–2026**; **43** span more than one evaluation-target category. The corpus was last checked in July 2026.

The repository and project page follow the paper’s four-dimensional taxonomy: **Evaluation Target × Evaluation Protocol × Evaluation Metrics × Evaluation Data**.

Rows are intentionally repeated across evaluation-target and sub-target tables. `△` marks a benchmark assigned to more than one top-level evaluation target. Every benchmark name links to its paper.

## Contents

- [Visual and Temporal Quality](#visual-and-temporal-quality)
- [Spatial and State Consistency](#spatial-and-state-consistency)
- [Long-Horizon Memory and State Persistence](#long-horizon-memory-and-state-persistence)
- [Physical Plausibility](#physical-plausibility)
- [Causal and Counterfactual Reasoning](#causal-and-counterfactual-reasoning)
- [Control Fidelity and Interactive Dynamics](#control-fidelity-and-interactive-dynamics)
- [Functional Utility](#functional-utility)

## Column conventions

| Dimension | Codes and meaning |
|:--|:--|
| Evaluation Protocol | `OL` Open-Loop Evaluation; `CL` Closed-Loop Interaction; `OL+CL` includes both protocol tracks |
| Evaluation Metrics | `P` Prediction-Level Metrics; `O` Downstream Outcome Metrics; `P+O` reports evidence at both levels |
| Evaluation Data | `RWD` Real-World Data Collection; `SBG` Simulation-Based Generation; `SPTC` Scenario, Prompt, and Task Curation; `HCP` Hybrid Construction Pipelines |

## Evaluation-target coverage

| Evaluation target | Benchmarks |
|:--|--:|
| Visual & Temporal Quality (`T1`) | 20 |
| Spatial & State Consistency (`T2`) | 19 |
| Long-Horizon Memory & State Persistence (`T3`) | 11 |
| Physical Plausibility (`T4`) | 39 |
| Causal & Counterfactual Reasoning (`T5`) | 22 |
| Control Fidelity & Interactive Dynamics (`T6`) | 29 |
| Functional Utility (`T7`) | 8 |

Counts overlap because cross-category benchmarks appear in more than one top-level target.

## Visual and Temporal Quality

_Aligned with Figure 4 and Table 3 of the latest manuscript._

| Benchmark | Year | Domain | Protocol | Metrics | Data |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**FETV**](https://scholar.google.com/scholar?q=FETV%3A%20A%20benchmark%20for%20fine-grained%20evaluation%20of%20open-domain%20text-to-video%20generation) | 2023 | video | OL | P | SPTC |
| [**VBench △**](https://scholar.google.com/scholar?q=VBench%3A%20Comprehensive%20benchmark%20suite%20for%20video%20generative%20models) | 2024 | video | OL | P | SPTC |
| [**VBench++ △**](https://arxiv.org/abs/2411.13503) | 2024 | video | OL | P | SPTC |
| [**EvalCrafter**](https://scholar.google.com/scholar?q=EvalCrafter%3A%20Benchmarking%20and%20evaluating%20large%20video%20generation%20models) | 2024 | video | OL | P | SPTC |
| [**ChronoMagic-Bench**](https://scholar.google.com/scholar?q=ChronoMagic-Bench%3A%20A%20benchmark%20for%20metamorphic%20evaluation%20of%20text-to-time-lapse%20video%20generation) | 2024 | video | OL | P | SPTC |
| [**WorldScore △**](https://scholar.google.com/scholar?q=WorldScore%3A%20A%20unified%20evaluation%20benchmark%20for%20world%20generation) | 2025 | video | OL | P | HCP |
| [**VMBench**](https://arxiv.org/abs/2503.10076) | 2025 | video | OL | P | SPTC |
| [**EWMBench △**](https://arxiv.org/abs/2505.09694) | 2025 | embodied | OL | P | HCP |
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | embodied | OL | P | SBG |
| [**GameWorld Score △**](https://arxiv.org/abs/2506.18701) | 2025 | game | OL | P | SBG |
| [**WorldMark △**](https://arxiv.org/abs/2604.21686) | 2026 | game+video | OL | P | HCP |
| [**4DWorldBench △**](https://arxiv.org/abs/2511.19836) | 2025 | video | OL | P | HCP |
| [**TC-Bench △**](https://arxiv.org/abs/2406.08656) | 2024 | video | OL | P | HCP |
| [**WorldLens △**](https://arxiv.org/abs/2512.10958) | 2026 | driving | OL | P | HCP |
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | embodied | OL | P | HCP |
| [**DrivingGen △**](https://arxiv.org/abs/2601.01528) | 2026 | driving | OL | P | RWD |
| [**WBench △**](https://arxiv.org/abs/2605.25874) | 2026 | video | OL | P | HCP |
| [**PEDRA**](https://arxiv.org/abs/2510.20182) | 2025 | video | OL | P | RWD |
| [**Gen-ViRe**](https://arxiv.org/abs/2511.13853) | 2025 | video | OL | P | HCP |
| [**iWorld-Bench △**](https://arxiv.org/abs/2605.03941) | 2026 | video | OL | P | HCP |

## Spatial and State Consistency

_Aligned with Figure 4 and Table 4 of the latest manuscript._

| Benchmark | Year | Domain | Protocol | Metrics | Data |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**VBench △**](https://scholar.google.com/scholar?q=VBench%3A%20Comprehensive%20benchmark%20suite%20for%20video%20generative%20models) | 2024 | video | OL | P | SPTC |
| [**VBench++ △**](https://arxiv.org/abs/2411.13503) | 2024 | video | OL | P | SPTC |
| [**WorldMark △**](https://arxiv.org/abs/2604.21686) | 2026 | game+video | OL | P | HCP |
| [**GameWorld Score △**](https://arxiv.org/abs/2506.18701) | 2025 | game | OL | P | SBG |
| [**EWMBench △**](https://arxiv.org/abs/2505.09694) | 2025 | embodied | OL | P | HCP |
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | embodied | OL | P | SBG |
| [**WorldLens △**](https://arxiv.org/abs/2512.10958) | 2026 | driving | OL | P | HCP |
| [**DrivingGen △**](https://arxiv.org/abs/2601.01528) | 2026 | driving | OL | P | RWD |
| [**WorldScore △**](https://scholar.google.com/scholar?q=WorldScore%3A%20A%20unified%20evaluation%20benchmark%20for%20world%20generation) | 2025 | video | OL | P | HCP |
| [**4DWorldBench △**](https://arxiv.org/abs/2511.19836) | 2025 | video | OL | P | HCP |
| [**PDI-Bench △**](https://arxiv.org/abs/2605.15185) | 2026 | video | OL | P | HCP |
| [**LoopNav**](https://arxiv.org/abs/2505.22976) | 2025 | game | OL | P | SBG |
| [**MIND △**](https://arxiv.org/abs/2602.08025) | 2026 | video | OL | P | SBG |
| [**MBench △**](https://arxiv.org/abs/2606.00793) | 2026 | video | OL | P | RWD |
| [**STEVO-Bench △**](https://arxiv.org/abs/2603.13215) | 2026 | video | OL | P | HCP |
| [**CausalSpatial △**](https://arxiv.org/abs/2601.13304) | 2026 | image | OL | P | SBG |
| [**What-If World △**](https://arxiv.org/abs/2605.27589) | 2026 | driving+embodied | OL | P | RWD |
| [**WorldOlympiad △**](https://arxiv.org/abs/2606.11129) | 2026 | video | OL | P | HCP |
| [**HOCA-Bench △**](https://arxiv.org/abs/2602.19571) | 2026 | video | OL | P | HCP |

## Long-Horizon Memory and State Persistence

_Aligned with Figure 4 and Table 5 of the latest manuscript._

| Benchmark | Year | Domain | Protocol | Metrics | Data |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**WorldPrediction △**](https://arxiv.org/abs/2506.04363) | 2025 | video | OL | P | RWD |
| [**SmallWorlds**](https://arxiv.org/abs/2511.23465) | 2025 | video | OL | P | SBG |
| [**WR-Arena △**](https://arxiv.org/abs/2603.25887) | 2026 | driving+embodied | OL | P | HCP |
| [**WorldMark △**](https://arxiv.org/abs/2604.21686) | 2026 | game+video | OL | P | HCP |
| [**MBench △**](https://arxiv.org/abs/2606.00793) | 2026 | video | OL | P | RWD |
| [**MIND △**](https://arxiv.org/abs/2602.08025) | 2026 | video | OL | P | SBG |
| [**WBench △**](https://arxiv.org/abs/2605.25874) | 2026 | video | OL | P | HCP |
| [**WorldOlympiad △**](https://arxiv.org/abs/2606.11129) | 2026 | video | OL | P | HCP |
| [**HTEWorld**](https://arxiv.org/abs/2605.19957) | 2026 | embodied | OL | P | SBG |
| [**RoboWM-Bench △**](https://arxiv.org/abs/2604.19092) | 2026 | embodied | OL | O | HCP |
| [**iWorld-Bench △**](https://arxiv.org/abs/2605.03941) | 2026 | video | OL | P | HCP |

## Physical Plausibility

_Aligned with Figure 4 and Table 6 of the latest manuscript._

| Benchmark | Year | Domain | Protocol | Metrics | Data |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**IntPhys**](https://arxiv.org/abs/1803.07616) | 2018 | video | OL | P | SBG |
| [**IntPhys 2**](https://arxiv.org/abs/2506.09849) | 2025 | video | OL | P | SBG |
| [**CLEVRER △**](https://scholar.google.com/scholar?q=CLEVRER%3A%20Collision%20events%20for%20video%20representation%20and%20reasoning) | 2020 | video | OL | P | SBG |
| [**CoPhy △**](https://scholar.google.com/scholar?q=CoPhy%3A%20Counterfactual%20learning%20of%20physical%20dynamics) | 2020 | video | OL | P | SBG |
| [**PHYRE**](https://scholar.google.com/scholar?q=PHYRE%3A%20A%20new%20benchmark%20for%20physical%20reasoning) | 2019 | video | CL | O | SBG |
| [**CRAFT △**](https://scholar.google.com/scholar?q=CRAFT%3A%20A%20benchmark%20for%20causal%20reasoning%20about%20forces%20and%20interactions) | 2022 | video | OL | P | SBG |
| [**Physion △**](https://scholar.google.com/scholar?q=Physion%3A%20Evaluating%20physical%20prediction%20from%20vision%20in%20humans%20and%20machines) | 2021 | video | OL | P | SBG |
| [**Physion++**](https://scholar.google.com/scholar?q=Physion%2B%2B%3A%20Evaluating%20physical%20scene%20understanding%20that%20requires%20online%20inference%20of%20different%20physical%20properties) | 2023 | video | OL | P | SBG |
| [**ComPhy △**](https://scholar.google.com/scholar?q=ComPhy%3A%20Compositional%20physical%20reasoning%20of%20objects%20and%20events%20from%20videos) | 2022 | video | OL | P | SBG |
| [**ContPhy**](https://scholar.google.com/scholar?q=ContPhy%3A%20Continuum%20physical%20concept%20learning%20and%20reasoning%20from%20videos) | 2024 | video | OL | P | SBG |
| [**PhyCoBench**](https://arxiv.org/abs/2502.05503) | 2025 | video | OL | P | SPTC |
| [**VideoPhy △**](https://arxiv.org/abs/2406.03520) | 2024 | video | OL | P | SPTC |
| [**VideoPhy-2 △**](https://arxiv.org/abs/2503.06800) | 2025 | video | OL | P | SPTC |
| [**PhyGenBench △**](https://arxiv.org/abs/2410.05363) | 2024 | video | OL | P | SPTC |
| [**T2VPhysBench**](https://arxiv.org/abs/2505.00337) | 2025 | video | OL | P | SPTC |
| [**Physics-IQ △**](https://arxiv.org/abs/2501.09038) | 2025 | video | OL | P | RWD |
| [**WorldBench**](https://arxiv.org/abs/2601.21282) | 2026 | video | OL | P | HCP |
| [**PhyWorldBench △**](https://arxiv.org/abs/2507.13428) | 2025 | video | OL | P | SPTC |
| [**WorldOlympiad △**](https://arxiv.org/abs/2606.11129) | 2026 | video | OL | P | HCP |
| [**ACWM-Phys △**](https://arxiv.org/abs/2605.08567) | 2026 | video | OL | P | SBG |
| [**WorldModelBench △**](https://arxiv.org/abs/2502.20694) | 2025 | video | OL | P | SPTC |
| [**VBench-2.0 △**](https://arxiv.org/abs/2503.21755) | 2025 | video | OL | P | SPTC |
| [**GameWorld Score △**](https://arxiv.org/abs/2506.18701) | 2025 | game | OL | P | SBG |
| [**T2VWorldBench △**](https://arxiv.org/abs/2507.18107) | 2025 | video | OL | P | SPTC |
| [**4DWorldBench △**](https://arxiv.org/abs/2511.19836) | 2025 | video | OL | P | HCP |
| [**RoboWM-Bench △**](https://arxiv.org/abs/2604.19092) | 2026 | embodied | OL | O | HCP |
| [**DreamGen Bench △**](https://arxiv.org/abs/2505.12705) | 2025 | embodied | OL | P | HCP |
| [**WorldLens △**](https://arxiv.org/abs/2512.10958) | 2026 | driving | OL | P | HCP |
| [**RigidBench**](https://scholar.google.com/scholar?q=Rigidbench%3A%20Evaluating%20rigid-body%20physics%20in%20video%20generation%20models) | 2026 | video | OL | P | SBG |
| [**Morpheus**](https://arxiv.org/abs/2504.02918) | 2025 | video | OL | P | RWD |
| [**What-If World △**](https://arxiv.org/abs/2605.27589) | 2026 | driving+embodied | OL | P | RWD |
| [**PhyGround**](https://arxiv.org/abs/2605.10806) | 2026 | video | OL | P | SPTC |
| [**Physion-Eval**](https://arxiv.org/abs/2603.19607) | 2026 | video | OL | P | HCP |
| [**CRONOS △**](https://arxiv.org/abs/2605.23699) | 2026 | video | OL | P | HCP |
| [**VACT △**](https://arxiv.org/abs/2503.06163) | 2025 | video | OL | P | SPTC |
| [**STEVO-Bench △**](https://arxiv.org/abs/2603.13215) | 2026 | video | OL | P | HCP |
| [**PhysicsMind**](https://arxiv.org/abs/2601.16007) | 2026 | video | OL | P | HCP |
| [**PDI-Bench △**](https://arxiv.org/abs/2605.15185) | 2026 | video | OL | P | HCP |
| [**HOCA-Bench △**](https://arxiv.org/abs/2602.19571) | 2026 | video | OL | P | HCP |

## Causal and Counterfactual Reasoning

_Leaf assignments follow Figure 4; benchmark metadata follow Table 7 of the latest manuscript._

### Causal Reasoning over Observed Worlds

| Benchmark | Year | Domain | Protocol | Metrics | Data |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**CLEVRER △**](https://scholar.google.com/scholar?q=CLEVRER%3A%20Collision%20events%20for%20video%20representation%20and%20reasoning) | 2020 | video | OL | P | SBG |
| [**CATER**](https://scholar.google.com/scholar?q=CATER%3A%20A%20diagnostic%20dataset%20for%20compositional%20actions%20and%20temporal%20reasoning) | 2020 | video | OL | P | SBG |
| [**NExT-QA**](https://arxiv.org/abs/2105.08276) | 2021 | video | OL | P | RWD |
| [**Causal-VidQA**](https://arxiv.org/abs/2205.14895) | 2022 | video | OL | P | RWD |
| [**CRAFT △**](https://scholar.google.com/scholar?q=CRAFT%3A%20A%20benchmark%20for%20causal%20reasoning%20about%20forces%20and%20interactions) | 2022 | video | OL | P | SBG |
| [**IntentQA**](https://scholar.google.com/scholar?q=IntentQA%3A%20Context-aware%20video%20intent%20reasoning) | 2023 | video | OL | P | RWD |
| [**CoPhy △**](https://scholar.google.com/scholar?q=CoPhy%3A%20Counterfactual%20learning%20of%20physical%20dynamics) | 2020 | video | OL | P | SBG |
| [**MMWorld**](https://arxiv.org/abs/2406.08407) | 2025 | video | OL | P | HCP |
| [**CausalVQA**](https://arxiv.org/abs/2506.09943) | 2025 | video | OL | P | RWD |
| [**VCRBench**](https://arxiv.org/abs/2505.08455) | 2025 | video | OL | P | RWD |
| [**Physion △**](https://scholar.google.com/scholar?q=Physion%3A%20Evaluating%20physical%20prediction%20from%20vision%20in%20humans%20and%20machines) | 2021 | video | OL | P | SBG |
| [**Physics-IQ △**](https://arxiv.org/abs/2501.09038) | 2025 | video | OL | P | RWD |
| [**WorldPrediction △**](https://arxiv.org/abs/2506.04363) | 2025 | video | OL | P | RWD |
| [**WR-Arena △**](https://arxiv.org/abs/2603.25887) | 2026 | driving+embodied | OL | P | HCP |
| [**CausalSpatial △**](https://arxiv.org/abs/2601.13304) | 2026 | image | OL | P | SBG |
| [**T2VWorldBench △**](https://arxiv.org/abs/2507.18107) | 2025 | video | OL | P | SPTC |
| [**VACT △**](https://arxiv.org/abs/2503.06163) | 2025 | video | OL | P | SPTC |
| [**HOCA-Bench △**](https://arxiv.org/abs/2602.19571) | 2026 | video | OL | P | HCP |

### Counterfactual Reasoning over Intervened Worlds

| Benchmark | Year | Domain | Protocol | Metrics | Data |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**CLEVRER △**](https://scholar.google.com/scholar?q=CLEVRER%3A%20Collision%20events%20for%20video%20representation%20and%20reasoning) | 2020 | video | OL | P | SBG |
| [**CRAFT △**](https://scholar.google.com/scholar?q=CRAFT%3A%20A%20benchmark%20for%20causal%20reasoning%20about%20forces%20and%20interactions) | 2022 | video | OL | P | SBG |
| [**CoPhy △**](https://scholar.google.com/scholar?q=CoPhy%3A%20Counterfactual%20learning%20of%20physical%20dynamics) | 2020 | video | OL | P | SBG |
| [**ComPhy △**](https://scholar.google.com/scholar?q=ComPhy%3A%20Compositional%20physical%20reasoning%20of%20objects%20and%20events%20from%20videos) | 2022 | video | OL | P | SBG |
| [**ACQUIRED**](https://arxiv.org/abs/2311.01620) | 2023 | video | OL | P | RWD |
| [**Causal-VidQA**](https://arxiv.org/abs/2205.14895) | 2022 | video | OL | P | RWD |
| [**MMWorld**](https://arxiv.org/abs/2406.08407) | 2025 | video | OL | P | HCP |
| [**CausalVQA**](https://arxiv.org/abs/2506.09943) | 2025 | video | OL | P | RWD |
| [**What-If World △**](https://arxiv.org/abs/2605.27589) | 2026 | driving+embodied | OL | P | RWD |
| [**WR-Arena △**](https://arxiv.org/abs/2603.25887) | 2026 | driving+embodied | OL | P | HCP |
| [**CRONOS △**](https://arxiv.org/abs/2605.23699) | 2026 | video | OL | P | HCP |

## Control Fidelity and Interactive Dynamics

_Aligned with Figure 4 and Table 8 of the latest manuscript._

### Pre-specified Control Fidelity

| Benchmark | Year | Domain | Protocol | Metrics | Data |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**T2V-CompBench**](https://scholar.google.com/scholar?q=T2VCompBench%3A%20A%20comprehensive%20benchmark%20for%20compositional%20textto-video%20generation) | 2025 | video | OL | P | SPTC |
| [**TC-Bench △**](https://arxiv.org/abs/2406.08656) | 2024 | video | OL | P | HCP |
| [**StoryEval**](https://arxiv.org/abs/2412.16211) | 2024 | video | OL | P | SPTC |
| [**VideoPhy △**](https://arxiv.org/abs/2406.03520) | 2024 | video | OL | P | SPTC |
| [**VideoPhy-2 △**](https://arxiv.org/abs/2503.06800) | 2025 | video | OL | P | SPTC |
| [**PhyGenBench △**](https://arxiv.org/abs/2410.05363) | 2024 | video | OL | P | SPTC |
| [**PhyWorldBench △**](https://arxiv.org/abs/2507.13428) | 2025 | video | OL | P | SPTC |
| [**OSCBench**](https://arxiv.org/abs/2603.11698) | 2026 | video | OL | P | SPTC |
| [**MoveBench**](https://arxiv.org/abs/2512.08765) | 2025 | video | OL | P | RWD |
| [**MagicBench**](https://arxiv.org/abs/2503.16421) | 2025 | video | OL | P | RWD |
| [**WorldScore △**](https://scholar.google.com/scholar?q=WorldScore%3A%20A%20unified%20evaluation%20benchmark%20for%20world%20generation) | 2025 | video | OL | P | HCP |
| [**4DWorldBench △**](https://arxiv.org/abs/2511.19836) | 2025 | video | OL | P | HCP |
| [**DrivingGen △**](https://arxiv.org/abs/2601.01528) | 2026 | driving | OL | P | RWD |
| [**ACT-Bench**](https://arxiv.org/abs/2412.05337) | 2024 | driving | OL | P | RWD |
| [**What-If World △**](https://arxiv.org/abs/2605.27589) | 2026 | driving+embodied | OL | P | RWD |
| [**Omni-WorldBench**](https://arxiv.org/abs/2603.22212) | 2026 | video | OL | P | HCP |
| [**DreamGen Bench △**](https://arxiv.org/abs/2505.12705) | 2025 | embodied | OL | P | HCP |
| [**WorldModelBench △**](https://arxiv.org/abs/2502.20694) | 2025 | video | OL | P | SPTC |
| [**VBench-2.0 △**](https://arxiv.org/abs/2503.21755) | 2025 | video | OL | P | SPTC |

### Interactive Action Fidelity

| Benchmark | Year | Domain | Protocol | Metrics | Data |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**WorldMark △**](https://arxiv.org/abs/2604.21686) | 2026 | game+video | OL | P | HCP |
| [**WR-Arena △**](https://arxiv.org/abs/2603.25887) | 2026 | driving+embodied | OL | P | HCP |
| [**WorldSimBench △**](https://arxiv.org/abs/2410.18072) | 2024 | game+driving+embodied | OL+CL | P+O | HCP |
| [**WBench △**](https://arxiv.org/abs/2605.25874) | 2026 | video | OL | P | HCP |
| [**iWorld-Bench △**](https://arxiv.org/abs/2605.03941) | 2026 | video | OL | P | HCP |
| [**MIND △**](https://arxiv.org/abs/2602.08025) | 2026 | video | OL | P | SBG |
| [**ACWM-Phys △**](https://arxiv.org/abs/2605.08567) | 2026 | video | OL | P | SBG |
| [**RoboWM-Bench △**](https://arxiv.org/abs/2604.19092) | 2026 | embodied | OL | O | HCP |
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | embodied | OL | P | HCP |
| [**WorldOlympiad △**](https://arxiv.org/abs/2606.11129) | 2026 | video | OL | P | HCP |

## Functional Utility

_Aligned with Figure 4 and Table 9 of the latest manuscript. Protocol and metric codes are role-specific in this section._

### Data Engine

| Benchmark | Year | Domain | Protocol | Metrics | Data |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | embodied | OL | O | SBG |
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | embodied | OL | O | HCP |

### Policy Evaluator

| Benchmark | Year | Domain | Protocol | Metrics | Data |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | embodied | CL | O | SBG |

### Planner

| Benchmark | Year | Domain | Protocol | Metrics | Data |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**WorldArena △**](https://arxiv.org/abs/2602.08971) | 2026 | embodied | CL | O | SBG |
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | embodied | OL+CL | O | HCP |
| [**World-in-World**](https://arxiv.org/abs/2510.18135) | 2025 | embodied | CL | O | HCP |
| [**EVA-Bench**](https://arxiv.org/abs/2410.15461) | 2024 | embodied | OL | O | HCP |
| [**WorldLens △**](https://arxiv.org/abs/2512.10958) | 2026 | driving | CL | O | HCP |
| [**RoboWM-Bench △**](https://arxiv.org/abs/2604.19092) | 2026 | embodied | OL | O | HCP |
| [**WorldSimBench △**](https://arxiv.org/abs/2410.18072) | 2024 | game+driving+embodied | CL | O | HCP |
| [**WR-Arena △**](https://arxiv.org/abs/2603.25887) | 2026 | driving+embodied | OL | P | HCP |

### Interactive Training Environment

| Benchmark | Year | Domain | Protocol | Metrics | Data |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**WorldArena 2.0 △**](https://arxiv.org/abs/2605.17912) | 2026 | embodied | CL | O | HCP |

## Machine-readable data

- [`docs/assets/benchmarks.json`](docs/assets/benchmarks.json): canonical benchmark, target, sub-target, protocol, metric, data-source, year, and domain metadata
- [`docs/assets/metadata.json`](docs/assets/metadata.json): taxonomy labels and release-window definitions
- [Interactive project page](https://axbhb.github.io/world-model-evaluation-survey/)
