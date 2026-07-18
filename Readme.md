# A Survey of World Model Benchmarks

[![Project Page](https://img.shields.io/badge/Project-Page-5965d8)](https://axbhb.github.io/world-model-evaluation-survey/) [![Benchmarks](https://img.shields.io/badge/Benchmarks-82-2f8f63)](https://axbhb.github.io/world-model-evaluation-survey/#benchmarks)

This repository accompanies **A Survey of World Model Benchmarks**. The latest manuscript covers **82 representative benchmarks** published from **2018–2026**; **43** span more than one evaluation-target category. The corpus was last checked in July 2026.

The category membership below follows the latest survey taxonomy and Figure 4. Rows are intentionally repeated when a benchmark belongs to multiple evaluation targets or sub-targets. `△` marks a benchmark assigned to more than one top-level evaluation target.

Each table is designed as a literature index rather than a copy of Tables 3–9: **Article**, **Year**, **Venue**, **Code**, and **Project Page**. `-` means that no verified public link is currently recorded.

## Contents

- [Visual and Temporal Quality](#visual-and-temporal-quality)
- [Spatial and State Consistency](#spatial-and-state-consistency)
- [Long-Horizon Memory and State Persistence](#long-horizon-memory-and-state-persistence)
- [Physical Plausibility](#physical-plausibility)
- [Causal and Counterfactual Reasoning](#causal-and-counterfactual-reasoning)
- [Control Fidelity and Interactive Dynamics](#control-fidelity-and-interactive-dynamics)
- [Functional Utility](#functional-utility)

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

Counts overlap because cross-category benchmarks appear in more than one top-level target.

## Visual and Temporal Quality

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**FETV: A benchmark for fine-grained evaluation of open-domain text-to-video generation**](https://scholar.google.com/scholar?q=FETV%3A%20A%20benchmark%20for%20fine-grained%20evaluation%20of%20open-domain%20text-to-video%20generation) | 2023 | NeurIPS Datasets and Benchmarks | [Code](https://github.com/llyx97/FETV) | - |
| [**VBench: Comprehensive benchmark suite for video generative models △**](https://scholar.google.com/scholar?q=VBench%3A%20Comprehensive%20benchmark%20suite%20for%20video%20generative%20models) | 2024 | CVPR | [Code](https://github.com/Vchitect/VBench) | [Project Page](https://vchitect.github.io/VBench-project/) |
| [**VBench++: Comprehensive and versatile benchmark suite for video generative models △**](https://arxiv.org/abs/2411.13503) | 2024 | IEEE TPAMI | [Code](https://github.com/Vchitect/VBench) | [Project Page](https://vchitect.github.io/VBench-project/) |
| [**EvalCrafter: Benchmarking and evaluating large video generation models**](https://scholar.google.com/scholar?q=EvalCrafter%3A%20Benchmarking%20and%20evaluating%20large%20video%20generation%20models) | 2024 | CVPR | [Code](https://github.com/evalcrafter/EvalCrafter) | [Project Page](https://evalcrafter.github.io/) |
| [**ChronoMagic-Bench: A benchmark for metamorphic evaluation of text-to-time-lapse video generation**](https://scholar.google.com/scholar?q=ChronoMagic-Bench%3A%20A%20benchmark%20for%20metamorphic%20evaluation%20of%20text-to-time-lapse%20video%20generation) | 2024 | NeurIPS Datasets and Benchmarks Spotlight | [Code](https://github.com/PKU-YuanGroup/ChronoMagic-Bench) | [Project Page](https://pku-yuangroup.github.io/ChronoMagic-Bench/) |
| [**WorldScore: A unified evaluation benchmark for world generation △**](https://scholar.google.com/scholar?q=WorldScore%3A%20A%20unified%20evaluation%20benchmark%20for%20world%20generation) | 2025 | ICCV | [Code](https://github.com/haoyi-duan/WorldScore) | [Project Page](https://haoyi-duan.github.io/WorldScore/) |
| [**VMBench: A Benchmark for Perception-Aligned Video Motion Generation**](https://arxiv.org/abs/2503.10076) | 2025 | ICCV | [Code](https://github.com/AMAP-ML/VMBench) | [Project Page](https://amap-ml.github.io/VMBench-Website/) |
| [**EWMBench: Evaluating scene, motion, and semantic quality in embodied world models △**](https://arxiv.org/abs/2505.09694) | 2025 | BMVC | [Code](https://github.com/AgibotTech/EWMBench) | - |
| [**WorldArena: A unified benchmark for evaluating perception and functional utility of embodied world models △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | [Code](https://github.com/tsinghua-fib-lab/WorldArena) | [Project Page](https://world-arena.ai/) |
| [**Matrix-Game: Interactive World Foundation Model △**](https://arxiv.org/abs/2506.18701) | 2025 | arXiv | [Code](https://github.com/SkyworkAI/Matrix-Game) | [Project Page](https://matrix-game-homepage.github.io/) |
| [**WorldMark: A unified benchmark suite for interactive video world models △**](https://arxiv.org/abs/2604.21686) | 2026 | arXiv | [Code](https://github.com/alaya-studio/WorldMark) | [Project Page](https://alaya-studio.github.io/WorldMark/) |
| [**4DWorldBench: A comprehensive evaluation framework for 3d/4d world generation models △**](https://arxiv.org/abs/2511.19836) | 2025 | CVPR | - | [Project Page](https://yeppp27.github.io/4DWorldBench.github.io/) |
| [**TC-Bench: Benchmarking Temporal Compositionality in Text-to-Video and Image-to-Video Generation △**](https://arxiv.org/abs/2406.08656) | 2024 | ACL Findings | [Code](https://github.com/weixi-feng/TC-Bench) | [Project Page](https://weixi-feng.github.io/tc-bench/) |
| [**WorldLens: Full-spectrum evaluations of driving world models in real world △**](https://arxiv.org/abs/2512.10958) | 2026 | CVPR Oral | [Code](https://github.com/worldbench/WorldLens) | [Project Page](https://worldbench.github.io/worldlens) |
| [**WorldArena 2.0: Extending Embodied World Model Benchmarking on Modality, Functionality and Platform △**](https://arxiv.org/abs/2605.17912) | 2026 | arXiv | [Code](https://github.com/tsinghua-fib-lab/WorldArena) | [Project Page](https://world-arena.ai/) |
| [**DrivingGen: A Comprehensive Benchmark for Generative Video World Models in Autonomous Driving △**](https://arxiv.org/abs/2601.01528) | 2026 | ICLR | - | [Project Page](https://drivinggen-bench.github.io/) |
| [**WBench: A Comprehensive Multi-Turn Benchmark for Interactive Video World Model Evaluation △**](https://arxiv.org/abs/2605.25874) | 2026 | arXiv | - | - |
| [**PEDRA: Evaluating the Realism of Pedestrian Dynamics in Video Generation**](https://arxiv.org/abs/2510.20182) | 2025 | CVPR | - | - |
| [**Can World Simulators Reason? Gen-ViRe: A Generative Visual Reasoning Benchmark**](https://arxiv.org/abs/2511.13853) | 2025 | arXiv | - | - |
| [**iWorld-Bench: A benchmark for interactive world models with a unified action generation framework △**](https://arxiv.org/abs/2605.03941) | 2026 | arXiv | - | - |

## Spatial and State Consistency

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**VBench: Comprehensive benchmark suite for video generative models △**](https://scholar.google.com/scholar?q=VBench%3A%20Comprehensive%20benchmark%20suite%20for%20video%20generative%20models) | 2024 | CVPR | [Code](https://github.com/Vchitect/VBench) | [Project Page](https://vchitect.github.io/VBench-project/) |
| [**VBench++: Comprehensive and versatile benchmark suite for video generative models △**](https://arxiv.org/abs/2411.13503) | 2024 | IEEE TPAMI | [Code](https://github.com/Vchitect/VBench) | [Project Page](https://vchitect.github.io/VBench-project/) |
| [**WorldMark: A unified benchmark suite for interactive video world models △**](https://arxiv.org/abs/2604.21686) | 2026 | arXiv | [Code](https://github.com/alaya-studio/WorldMark) | [Project Page](https://alaya-studio.github.io/WorldMark/) |
| [**Matrix-Game: Interactive World Foundation Model △**](https://arxiv.org/abs/2506.18701) | 2025 | arXiv | [Code](https://github.com/SkyworkAI/Matrix-Game) | [Project Page](https://matrix-game-homepage.github.io/) |
| [**EWMBench: Evaluating scene, motion, and semantic quality in embodied world models △**](https://arxiv.org/abs/2505.09694) | 2025 | BMVC | [Code](https://github.com/AgibotTech/EWMBench) | - |
| [**WorldArena: A unified benchmark for evaluating perception and functional utility of embodied world models △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | [Code](https://github.com/tsinghua-fib-lab/WorldArena) | [Project Page](https://world-arena.ai/) |
| [**WorldLens: Full-spectrum evaluations of driving world models in real world △**](https://arxiv.org/abs/2512.10958) | 2026 | CVPR Oral | [Code](https://github.com/worldbench/WorldLens) | [Project Page](https://worldbench.github.io/worldlens) |
| [**DrivingGen: A Comprehensive Benchmark for Generative Video World Models in Autonomous Driving △**](https://arxiv.org/abs/2601.01528) | 2026 | ICLR | - | [Project Page](https://drivinggen-bench.github.io/) |
| [**WorldScore: A unified evaluation benchmark for world generation △**](https://scholar.google.com/scholar?q=WorldScore%3A%20A%20unified%20evaluation%20benchmark%20for%20world%20generation) | 2025 | ICCV | [Code](https://github.com/haoyi-duan/WorldScore) | [Project Page](https://haoyi-duan.github.io/WorldScore/) |
| [**4DWorldBench: A comprehensive evaluation framework for 3d/4d world generation models △**](https://arxiv.org/abs/2511.19836) | 2025 | CVPR | - | [Project Page](https://yeppp27.github.io/4DWorldBench.github.io/) |
| [**Quantitative video world model evaluation for geometric-consistency △**](https://arxiv.org/abs/2605.15185) | 2026 | arXiv | - | - |
| [**LoopNav: Benchmarking Spatial Consistency in World Models**](https://arxiv.org/abs/2505.22976) | 2025 | arXiv | - | - |
| [**MIND: Benchmarking Memory Consistency and Action Control in World Models △**](https://arxiv.org/abs/2602.08025) | 2026 | arXiv | - | - |
| [**MBench: A Comprehensive Benchmark on Memory Capability for Video World Models △**](https://arxiv.org/abs/2606.00793) | 2026 | arXiv | - | - |
| [**Out of sight, out of mind? evaluating state evolution in video world models △**](https://arxiv.org/abs/2603.13215) | 2026 | arXiv | - | - |
| [**CausalSpatial: A Benchmark for Object-Centric Causal Spatial Reasoning △**](https://arxiv.org/abs/2601.13304) | 2026 | arXiv | - | - |
| [**What-if world: A causal benchmark for general world models in embodied scenarios △**](https://arxiv.org/abs/2605.27589) | 2026 | arXiv | - | - |
| [**WorldOlympiad: Can your world model survive a triathlon? △**](https://arxiv.org/abs/2606.11129) | 2026 | arXiv | - | - |
| [**HOCA-Bench: Beyond Semantic Perception to Predictive World Modeling via Hegelian Ontological-Causal Anomalies △**](https://arxiv.org/abs/2602.19571) | 2026 | arXiv | - | - |

## Long-Horizon Memory and State Persistence

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**WorldPrediction: A Benchmark for High-Level World Modeling and Long-Horizon Procedural Planning △**](https://arxiv.org/abs/2506.04363) | 2025 | ICML Workshop | - | [Project Page](https://github.com/worldprediction/worldprediction.github.io) |
| [**SmallWorlds: Assessing dynamics understanding of world models in isolated environments**](https://arxiv.org/abs/2511.23465) | 2025 | arXiv | - | - |
| [**World reasoning arena △**](https://arxiv.org/abs/2603.25887) | 2026 | arXiv | [Code](https://github.com/MBZUAI-IFM/WR-Arena) | - |
| [**WorldMark: A unified benchmark suite for interactive video world models △**](https://arxiv.org/abs/2604.21686) | 2026 | arXiv | [Code](https://github.com/alaya-studio/WorldMark) | [Project Page](https://alaya-studio.github.io/WorldMark/) |
| [**MBench: A Comprehensive Benchmark on Memory Capability for Video World Models △**](https://arxiv.org/abs/2606.00793) | 2026 | arXiv | - | - |
| [**MIND: Benchmarking Memory Consistency and Action Control in World Models △**](https://arxiv.org/abs/2602.08025) | 2026 | arXiv | - | - |
| [**WBench: A Comprehensive Multi-Turn Benchmark for Interactive Video World Model Evaluation △**](https://arxiv.org/abs/2605.25874) | 2026 | arXiv | - | - |
| [**WorldOlympiad: Can your world model survive a triathlon? △**](https://arxiv.org/abs/2606.11129) | 2026 | arXiv | - | - |
| [**World-Ego Modeling for Long-Horizon Evolution in Hybrid Embodied Tasks**](https://arxiv.org/abs/2605.19957) | 2026 | arXiv | - | - |
| [**RoboWM-Bench: A benchmark for evaluating world models in robotic manipulation △**](https://arxiv.org/abs/2604.19092) | 2026 | CVPR | [Code](https://github.com/fffstrong/RoboWM-Bench) | [Project Page](https://robowm-bench.github.io/RoboWM-Bench/) |
| [**iWorld-Bench: A benchmark for interactive world models with a unified action generation framework △**](https://arxiv.org/abs/2605.03941) | 2026 | arXiv | - | - |

## Physical Plausibility

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**IntPhys: A framework and benchmark for visual intuitive physics reasoning**](https://arxiv.org/abs/1803.07616) | 2018 | IEEE TPAMI | - | [Project Page](https://intphys.cognitive-ml.fr/download.html) |
| [**IntPhys 2: Benchmarking intuitive physics understanding in complex synthetic environments**](https://arxiv.org/abs/2506.09849) | 2025 | NeurIPS Datasets and Benchmarks | [Code](https://github.com/facebookresearch/IntPhys2) | - |
| [**CLEVRER: Collision events for video representation and reasoning △**](https://scholar.google.com/scholar?q=CLEVRER%3A%20Collision%20events%20for%20video%20representation%20and%20reasoning) | 2020 | ICLR | [Code](https://github.com/chuangg/CLEVRER) | [Project Page](http://clevrer.csail.mit.edu) |
| [**CoPhy: Counterfactual learning of physical dynamics △**](https://scholar.google.com/scholar?q=CoPhy%3A%20Counterfactual%20learning%20of%20physical%20dynamics) | 2020 | ICLR | - | [Project Page](https://comphyreasoning.github.io/) |
| [**PHYRE: A new benchmark for physical reasoning**](https://scholar.google.com/scholar?q=PHYRE%3A%20A%20new%20benchmark%20for%20physical%20reasoning) | 2019 | NeurIPS | [Code](https://github.com/facebookresearch/phyre) | [Project Page](https://player.phyre.ai) |
| [**CRAFT: A benchmark for causal reasoning about forces and interactions △**](https://scholar.google.com/scholar?q=CRAFT%3A%20A%20benchmark%20for%20causal%20reasoning%20about%20forces%20and%20interactions) | 2022 | Findings of ACL | [Code](https://github.com/hucvl/craft) | - |
| [**Physion: Evaluating physical prediction from vision in humans and machines △**](https://scholar.google.com/scholar?q=Physion%3A%20Evaluating%20physical%20prediction%20from%20vision%20in%20humans%20and%20machines) | 2021 | NeurIPS Datasets and Benchmarks | [Code](https://github.com/cogtoolslab/physics-benchmarking-neurips2021) | [Project Page](https://physion-benchmark.github.io/) |
| [**Physion++: Evaluating physical scene understanding that requires online inference of different physical properties**](https://scholar.google.com/scholar?q=Physion%2B%2B%3A%20Evaluating%20physical%20scene%20understanding%20that%20requires%20online%20inference%20of%20different%20physical%20properties) | 2023 | NeurIPS | - | [Project Page](https://dingmyu.github.io/physion_v2/) |
| [**ComPhy: Compositional physical reasoning of objects and events from videos △**](https://scholar.google.com/scholar?q=ComPhy%3A%20Compositional%20physical%20reasoning%20of%20objects%20and%20events%20from%20videos) | 2022 | ICLR | - | [Project Page](https://comphyreasoning.github.io/) |
| [**ContPhy: Continuum physical concept learning and reasoning from videos**](https://scholar.google.com/scholar?q=ContPhy%3A%20Continuum%20physical%20concept%20learning%20and%20reasoning%20from%20videos) | 2024 | ICML | - | [Project Page](https://physical-reasoning-project.github.io/) |
| [**A physical coherence benchmark for evaluating video generation models via optical flow-guided frame prediction**](https://arxiv.org/abs/2502.05503) | 2025 | arXiv | [Code](https://github.com/Jeckinchen/PhyCoBench) | - |
| [**VideoPhy: Evaluating physical commonsense for video generation △**](https://arxiv.org/abs/2406.03520) | 2024 | ICLR | [Code](https://github.com/Hritikbansal/videophy) | - |
| [**VideoPhy-2: A challenging action-centric physical commonsense evaluation in video generation △**](https://arxiv.org/abs/2503.06800) | 2025 | ICLR | [Code](https://github.com/Hritikbansal/videophy) | [Project Page](https://videophy2.github.io/) |
| [**Towards world simulator: Crafting physical commonsense-based benchmark for video generation △**](https://arxiv.org/abs/2410.05363) | 2024 | ICML | [Code](https://github.com/OpenGVLab/PhyGenBench) | [Project Page](https://phygenbench123.github.io/) |
| [**T2VPhysBench: A first-principles benchmark for physical consistency in text-to-video generation**](https://arxiv.org/abs/2505.00337) | 2025 | arXiv | - | - |
| [**Do generative video models understand physical principles? △**](https://arxiv.org/abs/2501.09038) | 2025 | WACV | [Code](https://github.com/google-deepmind/physics-iq-benchmark) | [Project Page](https://physics-iq.github.io/) |
| [**WorldBench: Disambiguating physics for diagnostic evaluation of world models**](https://arxiv.org/abs/2601.21282) | 2026 | arXiv | - | [Project Page](https://world-bench.github.io/) |
| [**PhyWorldBench: A comprehensive evaluation of physical realism in text-to-video models △**](https://arxiv.org/abs/2507.13428) | 2025 | ICLR | [Code](https://github.com/g-jing/phy-world-bench) | [Project Page](https://research.nvidia.com/labs/dir/phyworldbench/) |
| [**T2VWorldBench: A benchmark for evaluating world knowledge in text-to-video generation △**](https://arxiv.org/abs/2507.18107) | 2025 | WACV | - | - |
| [**WorldModelBench: Judging video generation models as world models △**](https://arxiv.org/abs/2502.20694) | 2025 | NeurIPS | [Code](https://github.com/WorldModelBench-Team/WorldModelBench) | [Project Page](https://worldmodelbench-team.github.io) |
| [**VBench-2.0: Advancing Video Generation Benchmark Suite for Intrinsic Faithfulness △**](https://arxiv.org/abs/2503.21755) | 2025 | arXiv | [Code](https://github.com/Vchitect/VBench) | [Project Page](https://vchitect.github.io/VBench-project/) |
| [**4DWorldBench: A comprehensive evaluation framework for 3d/4d world generation models △**](https://arxiv.org/abs/2511.19836) | 2025 | CVPR | - | [Project Page](https://yeppp27.github.io/4DWorldBench.github.io/) |
| [**Matrix-Game: Interactive World Foundation Model △**](https://arxiv.org/abs/2506.18701) | 2025 | arXiv | [Code](https://github.com/SkyworkAI/Matrix-Game) | [Project Page](https://matrix-game-homepage.github.io/) |
| [**Rigidbench: Evaluating rigid-body physics in video generation models**](https://scholar.google.com/scholar?q=Rigidbench%3A%20Evaluating%20rigid-body%20physics%20in%20video%20generation%20models) | 2026 | ICLR Workshop | - | - |
| [**Morpheus: Benchmarking physical reasoning of video generative models with real physical experiments**](https://arxiv.org/abs/2504.02918) | 2025 | arXiv | - | - |
| [**What-if world: A causal benchmark for general world models in embodied scenarios △**](https://arxiv.org/abs/2605.27589) | 2026 | arXiv | - | - |
| [**RoboWM-Bench: A benchmark for evaluating world models in robotic manipulation △**](https://arxiv.org/abs/2604.19092) | 2026 | CVPR | [Code](https://github.com/fffstrong/RoboWM-Bench) | [Project Page](https://robowm-bench.github.io/RoboWM-Bench/) |
| [**DreamGen: Unlocking generalization in robot learning through video world models (introduces DreamGen Bench) △**](https://arxiv.org/abs/2505.12705) | 2025 | CoRL | [Code](https://github.com/NVIDIA/GR00T-Dreams) | [Project Page](https://research.nvidia.com/labs/gear/dreamgen/) |
| [**WorldLens: Full-spectrum evaluations of driving world models in real world △**](https://arxiv.org/abs/2512.10958) | 2026 | CVPR Oral | [Code](https://github.com/worldbench/WorldLens) | [Project Page](https://worldbench.github.io/worldlens) |
| [**PhyGround: Benchmarking Physical Reasoning in Generative World Models**](https://arxiv.org/abs/2605.10806) | 2026 | arXiv | - | - |
| [**Physion-Eval: Evaluating Physical Realism in Generated Video via Human Reasoning**](https://arxiv.org/abs/2603.19607) | 2026 | arXiv | - | - |
| [**CRONOS: Benchmarking Counterfactual Physical Consistency in Video Models △**](https://arxiv.org/abs/2605.23699) | 2026 | arXiv | - | - |
| [**Vact: A video automatic causal testing system and a benchmark △**](https://arxiv.org/abs/2503.06163) | 2025 | arXiv | - | - |
| [**Out of sight, out of mind? evaluating state evolution in video world models △**](https://arxiv.org/abs/2603.13215) | 2026 | arXiv | - | - |
| [**PhysicsMind: Sim and Real Mechanics Benchmarking for Physical Reasoning and Prediction in Foundational VLMs and World Models**](https://arxiv.org/abs/2601.16007) | 2026 | arXiv | - | - |
| [**Quantitative video world model evaluation for geometric-consistency △**](https://arxiv.org/abs/2605.15185) | 2026 | arXiv | - | - |
| [**HOCA-Bench: Beyond Semantic Perception to Predictive World Modeling via Hegelian Ontological-Causal Anomalies △**](https://arxiv.org/abs/2602.19571) | 2026 | arXiv | - | - |
| [**WorldOlympiad: Can your world model survive a triathlon? △**](https://arxiv.org/abs/2606.11129) | 2026 | arXiv | - | - |
| [**ACWM-Phys: Investigating generalized physical interaction in action-conditioned video world models △**](https://arxiv.org/abs/2605.08567) | 2026 | arXiv | - | - |

## Causal and Counterfactual Reasoning

### Causal Reasoning over Observed Worlds

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**CLEVRER: Collision events for video representation and reasoning △**](https://scholar.google.com/scholar?q=CLEVRER%3A%20Collision%20events%20for%20video%20representation%20and%20reasoning) | 2020 | ICLR | [Code](https://github.com/chuangg/CLEVRER) | [Project Page](http://clevrer.csail.mit.edu) |
| [**CATER: A diagnostic dataset for compositional actions and temporal reasoning**](https://scholar.google.com/scholar?q=CATER%3A%20A%20diagnostic%20dataset%20for%20compositional%20actions%20and%20temporal%20reasoning) | 2020 | ICLR | [Code](https://github.com/rohitgirdhar/CATER) | - |
| [**NExT-QA: Next phase of question-answering to explaining temporal actions**](https://arxiv.org/abs/2105.08276) | 2021 | CVPR | [Code](https://github.com/doc-doc/NExT-QA) | - |
| [**From representation to reasoning: Towards both evidence and commonsense reasoning for video question-answering**](https://arxiv.org/abs/2205.14895) | 2022 | CVPR | [Code](https://github.com/bcmi/Causal-VidQA) | - |
| [**CRAFT: A benchmark for causal reasoning about forces and interactions △**](https://scholar.google.com/scholar?q=CRAFT%3A%20A%20benchmark%20for%20causal%20reasoning%20about%20forces%20and%20interactions) | 2022 | Findings of ACL | [Code](https://github.com/hucvl/craft) | - |
| [**IntentQA: Context-aware video intent reasoning**](https://scholar.google.com/scholar?q=IntentQA%3A%20Context-aware%20video%20intent%20reasoning) | 2023 | ICCV | [Code](https://github.com/JoseponLee/IntentQA) | - |
| [**CoPhy: Counterfactual learning of physical dynamics △**](https://scholar.google.com/scholar?q=CoPhy%3A%20Counterfactual%20learning%20of%20physical%20dynamics) | 2020 | ICLR | - | [Project Page](https://comphyreasoning.github.io/) |
| [**MMWorld: Towards multi-discipline multi-faceted world model evaluation in videos**](https://scholar.google.com/scholar?q=MMWorld%3A%20Towards%20multi-discipline%20multi-faceted%20world%20model%20evaluation%20in%20videos) | 2025 | ICLR | [Code](https://github.com/UCSB-AI/MMWorld) | [Project Page](https://mmworld-bench.github.io/) |
| [**CausalVQA: A physically grounded causal reasoning benchmark for video models**](https://arxiv.org/abs/2506.09943) | 2025 | arXiv | [Code](https://github.com/facebookresearch/CausalVQA) | [Project Page](https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/) |
| [**VCRBench: Exploring long-form causal reasoning capabilities of large video language models**](https://arxiv.org/abs/2505.08455) | 2025 | CVPR Workshop | [Code](https://github.com/pritamqu/VCRBench) | [Project Page](https://pritamqu.github.io/VCRBench/) |
| [**Physion: Evaluating physical prediction from vision in humans and machines △**](https://scholar.google.com/scholar?q=Physion%3A%20Evaluating%20physical%20prediction%20from%20vision%20in%20humans%20and%20machines) | 2021 | NeurIPS Datasets and Benchmarks | [Code](https://github.com/cogtoolslab/physics-benchmarking-neurips2021) | [Project Page](https://physion-benchmark.github.io/) |
| [**Do generative video models understand physical principles? △**](https://arxiv.org/abs/2501.09038) | 2025 | WACV | [Code](https://github.com/google-deepmind/physics-iq-benchmark) | [Project Page](https://physics-iq.github.io/) |
| [**WorldPrediction: A Benchmark for High-Level World Modeling and Long-Horizon Procedural Planning △**](https://arxiv.org/abs/2506.04363) | 2025 | ICML Workshop | - | [Project Page](https://github.com/worldprediction/worldprediction.github.io) |
| [**World reasoning arena △**](https://arxiv.org/abs/2603.25887) | 2026 | arXiv | [Code](https://github.com/MBZUAI-IFM/WR-Arena) | - |
| [**CausalSpatial: A Benchmark for Object-Centric Causal Spatial Reasoning △**](https://arxiv.org/abs/2601.13304) | 2026 | arXiv | - | - |
| [**T2VWorldBench: A benchmark for evaluating world knowledge in text-to-video generation △**](https://arxiv.org/abs/2507.18107) | 2025 | WACV | - | - |
| [**Vact: A video automatic causal testing system and a benchmark △**](https://arxiv.org/abs/2503.06163) | 2025 | arXiv | - | - |
| [**HOCA-Bench: Beyond Semantic Perception to Predictive World Modeling via Hegelian Ontological-Causal Anomalies △**](https://arxiv.org/abs/2602.19571) | 2026 | arXiv | - | - |

### Counterfactual Reasoning over Intervened Worlds

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**CLEVRER: Collision events for video representation and reasoning △**](https://scholar.google.com/scholar?q=CLEVRER%3A%20Collision%20events%20for%20video%20representation%20and%20reasoning) | 2020 | ICLR | [Code](https://github.com/chuangg/CLEVRER) | [Project Page](http://clevrer.csail.mit.edu) |
| [**CRAFT: A benchmark for causal reasoning about forces and interactions △**](https://scholar.google.com/scholar?q=CRAFT%3A%20A%20benchmark%20for%20causal%20reasoning%20about%20forces%20and%20interactions) | 2022 | Findings of ACL | [Code](https://github.com/hucvl/craft) | - |
| [**CoPhy: Counterfactual learning of physical dynamics △**](https://scholar.google.com/scholar?q=CoPhy%3A%20Counterfactual%20learning%20of%20physical%20dynamics) | 2020 | ICLR | - | [Project Page](https://comphyreasoning.github.io/) |
| [**ComPhy: Compositional physical reasoning of objects and events from videos △**](https://scholar.google.com/scholar?q=ComPhy%3A%20Compositional%20physical%20reasoning%20of%20objects%20and%20events%20from%20videos) | 2022 | ICLR | - | [Project Page](https://comphyreasoning.github.io/) |
| [**ACQUIRED: A dataset for answering counterfactual questions in real-life videos**](https://arxiv.org/abs/2311.01620) | 2023 | EMNLP | [Code](https://github.com/PlusLabNLP/acquired) | - |
| [**From representation to reasoning: Towards both evidence and commonsense reasoning for video question-answering**](https://arxiv.org/abs/2205.14895) | 2022 | CVPR | [Code](https://github.com/bcmi/Causal-VidQA) | - |
| [**MMWorld: Towards multi-discipline multi-faceted world model evaluation in videos**](https://scholar.google.com/scholar?q=MMWorld%3A%20Towards%20multi-discipline%20multi-faceted%20world%20model%20evaluation%20in%20videos) | 2025 | ICLR | [Code](https://github.com/UCSB-AI/MMWorld) | [Project Page](https://mmworld-bench.github.io/) |
| [**CausalVQA: A physically grounded causal reasoning benchmark for video models**](https://arxiv.org/abs/2506.09943) | 2025 | arXiv | [Code](https://github.com/facebookresearch/CausalVQA) | [Project Page](https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/) |
| [**What-if world: A causal benchmark for general world models in embodied scenarios △**](https://arxiv.org/abs/2605.27589) | 2026 | arXiv | - | - |
| [**World reasoning arena △**](https://arxiv.org/abs/2603.25887) | 2026 | arXiv | [Code](https://github.com/MBZUAI-IFM/WR-Arena) | - |
| [**CRONOS: Benchmarking Counterfactual Physical Consistency in Video Models △**](https://arxiv.org/abs/2605.23699) | 2026 | arXiv | - | - |

## Control Fidelity and Interactive Dynamics

### Pre-specified Control Fidelity

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**T2V-CompBench: A Comprehensive Benchmark for Compositional Text-to-Video Generation**](https://scholar.google.com/scholar?q=T2VCompBench%3A%20A%20comprehensive%20benchmark%20for%20compositional%20textto-video%20generation) | 2025 | CVPR | [Code](https://github.com/KaiyueSun98/T2V-CompBench) | - |
| [**TC-Bench: Benchmarking Temporal Compositionality in Text-to-Video and Image-to-Video Generation △**](https://arxiv.org/abs/2406.08656) | 2024 | ACL Findings | [Code](https://github.com/weixi-feng/TC-Bench) | [Project Page](https://weixi-feng.github.io/tc-bench/) |
| [**Is your world simulator a good story presenter? a consecutive events-based benchmark for future long video generation**](https://arxiv.org/abs/2412.16211) | 2024 | CVPR | [Code](https://github.com/ypwang61/StoryEval) | [Project Page](https://ypwang61.github.io/project/StoryEval/) |
| [**VideoPhy: Evaluating physical commonsense for video generation △**](https://arxiv.org/abs/2406.03520) | 2024 | ICLR | [Code](https://github.com/Hritikbansal/videophy) | - |
| [**VideoPhy-2: A challenging action-centric physical commonsense evaluation in video generation △**](https://arxiv.org/abs/2503.06800) | 2025 | ICLR | [Code](https://github.com/Hritikbansal/videophy) | [Project Page](https://videophy2.github.io/) |
| [**Towards world simulator: Crafting physical commonsense-based benchmark for video generation △**](https://arxiv.org/abs/2410.05363) | 2024 | ICML | [Code](https://github.com/OpenGVLab/PhyGenBench) | [Project Page](https://phygenbench123.github.io/) |
| [**PhyWorldBench: A comprehensive evaluation of physical realism in text-to-video models △**](https://arxiv.org/abs/2507.13428) | 2025 | ICLR | [Code](https://github.com/g-jing/phy-world-bench) | [Project Page](https://research.nvidia.com/labs/dir/phyworldbench/) |
| [**OSCBench: Benchmarking object state change in text-to-video generation**](https://arxiv.org/abs/2603.11698) | 2026 | ACL | - | - |
| [**Wan-Move: Motion-Controllable Video Generation via Latent Trajectory Guidance**](https://arxiv.org/abs/2512.08765) | 2025 | NeurIPS | [Code](https://github.com/ali-vilab/Wan-Move) | [Project Page](https://wan-move.github.io/) |
| [**MagicMotion: Controllable Video Generation with Dense-to-Sparse Trajectory Guidance**](https://arxiv.org/abs/2503.16421) | 2025 | ICCV | [Code](https://github.com/quanhaol/MagicMotion) | [Project Page](https://quanhaol.github.io/magicmotion-site/) |
| [**WorldScore: A unified evaluation benchmark for world generation △**](https://scholar.google.com/scholar?q=WorldScore%3A%20A%20unified%20evaluation%20benchmark%20for%20world%20generation) | 2025 | ICCV | [Code](https://github.com/haoyi-duan/WorldScore) | [Project Page](https://haoyi-duan.github.io/WorldScore/) |
| [**4DWorldBench: A comprehensive evaluation framework for 3d/4d world generation models △**](https://arxiv.org/abs/2511.19836) | 2025 | CVPR | - | [Project Page](https://yeppp27.github.io/4DWorldBench.github.io/) |
| [**DrivingGen: A Comprehensive Benchmark for Generative Video World Models in Autonomous Driving △**](https://arxiv.org/abs/2601.01528) | 2026 | ICLR | - | [Project Page](https://drivinggen-bench.github.io/) |
| [**ACT-Bench: Towards Action Controllable World Models for Autonomous Driving**](https://arxiv.org/abs/2412.05337) | 2024 | arXiv | - | - |
| [**What-if world: A causal benchmark for general world models in embodied scenarios △**](https://arxiv.org/abs/2605.27589) | 2026 | arXiv | - | - |
| [**Omni-WorldBench: Towards a comprehensive interaction-centric evaluation for world models**](https://arxiv.org/abs/2603.22212) | 2026 | arXiv | [Code](https://github.com/AMAP-ML/Omni-WorldBench) | - |
| [**DreamGen: Unlocking generalization in robot learning through video world models (introduces DreamGen Bench) △**](https://arxiv.org/abs/2505.12705) | 2025 | CoRL | [Code](https://github.com/NVIDIA/GR00T-Dreams) | [Project Page](https://research.nvidia.com/labs/gear/dreamgen/) |
| [**WorldModelBench: Judging video generation models as world models △**](https://arxiv.org/abs/2502.20694) | 2025 | NeurIPS | [Code](https://github.com/WorldModelBench-Team/WorldModelBench) | [Project Page](https://worldmodelbench-team.github.io) |
| [**VBench-2.0: Advancing Video Generation Benchmark Suite for Intrinsic Faithfulness △**](https://arxiv.org/abs/2503.21755) | 2025 | arXiv | [Code](https://github.com/Vchitect/VBench) | [Project Page](https://vchitect.github.io/VBench-project/) |

### Interactive Action Fidelity

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**WorldMark: A unified benchmark suite for interactive video world models △**](https://arxiv.org/abs/2604.21686) | 2026 | arXiv | [Code](https://github.com/alaya-studio/WorldMark) | [Project Page](https://alaya-studio.github.io/WorldMark/) |
| [**World reasoning arena △**](https://arxiv.org/abs/2603.25887) | 2026 | arXiv | [Code](https://github.com/MBZUAI-IFM/WR-Arena) | - |
| [**WorldSimBench: Towards video generation models as world simulators △**](https://arxiv.org/abs/2410.18072) | 2024 | ICML | - | [Project Page](https://iranqin.github.io/WorldSimBench.github.io/) |
| [**WBench: A Comprehensive Multi-Turn Benchmark for Interactive Video World Model Evaluation △**](https://arxiv.org/abs/2605.25874) | 2026 | arXiv | - | - |
| [**iWorld-Bench: A benchmark for interactive world models with a unified action generation framework △**](https://arxiv.org/abs/2605.03941) | 2026 | arXiv | - | - |
| [**MIND: Benchmarking Memory Consistency and Action Control in World Models △**](https://arxiv.org/abs/2602.08025) | 2026 | arXiv | - | - |
| [**ACWM-Phys: Investigating generalized physical interaction in action-conditioned video world models △**](https://arxiv.org/abs/2605.08567) | 2026 | arXiv | - | - |
| [**RoboWM-Bench: A benchmark for evaluating world models in robotic manipulation △**](https://arxiv.org/abs/2604.19092) | 2026 | CVPR | [Code](https://github.com/fffstrong/RoboWM-Bench) | [Project Page](https://robowm-bench.github.io/RoboWM-Bench/) |
| [**WorldArena 2.0: Extending Embodied World Model Benchmarking on Modality, Functionality and Platform △**](https://arxiv.org/abs/2605.17912) | 2026 | arXiv | [Code](https://github.com/tsinghua-fib-lab/WorldArena) | [Project Page](https://world-arena.ai/) |
| [**WorldOlympiad: Can your world model survive a triathlon? △**](https://arxiv.org/abs/2606.11129) | 2026 | arXiv | - | - |

## Functional Utility

### World Model as Data Engine

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**WorldArena: A unified benchmark for evaluating perception and functional utility of embodied world models △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | [Code](https://github.com/tsinghua-fib-lab/WorldArena) | [Project Page](https://world-arena.ai/) |
| [**WorldArena 2.0: Extending Embodied World Model Benchmarking on Modality, Functionality and Platform △**](https://arxiv.org/abs/2605.17912) | 2026 | arXiv | [Code](https://github.com/tsinghua-fib-lab/WorldArena) | [Project Page](https://world-arena.ai/) |

### World Model as Policy Evaluator

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**WorldArena: A unified benchmark for evaluating perception and functional utility of embodied world models △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | [Code](https://github.com/tsinghua-fib-lab/WorldArena) | [Project Page](https://world-arena.ai/) |

### World Model as Planner

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**WorldArena: A unified benchmark for evaluating perception and functional utility of embodied world models △**](https://arxiv.org/abs/2602.08971) | 2026 | arXiv | [Code](https://github.com/tsinghua-fib-lab/WorldArena) | [Project Page](https://world-arena.ai/) |
| [**WorldArena 2.0: Extending Embodied World Model Benchmarking on Modality, Functionality and Platform △**](https://arxiv.org/abs/2605.17912) | 2026 | arXiv | [Code](https://github.com/tsinghua-fib-lab/WorldArena) | [Project Page](https://world-arena.ai/) |
| [**World-in-World: World Models in a Closed-Loop World**](https://arxiv.org/abs/2510.18135) | 2025 | ICLR | [Code](https://github.com/World-In-World/world-in-world) | [Project Page](https://world-in-world.github.io/) |
| [**EVA: An Embodied World Model for Future Video Anticipation**](https://arxiv.org/abs/2410.15461) | 2024 | ICML | [Code](https://github.com/litwellchi/EmbodiedVideoAnticipator) | [Project Page](https://sites.google.com/view/eva-public) |
| [**WorldLens: Full-spectrum evaluations of driving world models in real world △**](https://arxiv.org/abs/2512.10958) | 2026 | CVPR Oral | [Code](https://github.com/worldbench/WorldLens) | [Project Page](https://worldbench.github.io/worldlens) |
| [**RoboWM-Bench: A benchmark for evaluating world models in robotic manipulation △**](https://arxiv.org/abs/2604.19092) | 2026 | CVPR | [Code](https://github.com/fffstrong/RoboWM-Bench) | [Project Page](https://robowm-bench.github.io/RoboWM-Bench/) |
| [**WorldSimBench: Towards video generation models as world simulators △**](https://arxiv.org/abs/2410.18072) | 2024 | ICML | - | [Project Page](https://iranqin.github.io/WorldSimBench.github.io/) |
| [**World reasoning arena △**](https://arxiv.org/abs/2603.25887) | 2026 | arXiv | [Code](https://github.com/MBZUAI-IFM/WR-Arena) | - |

### World Model as Interactive Training Environment

| Article | Year | Venue | Code | Project Page |
|:--|:--:|:--:|:--:|:--:|
| [**WorldArena 2.0: Extending Embodied World Model Benchmarking on Modality, Functionality and Platform △**](https://arxiv.org/abs/2605.17912) | 2026 | arXiv | [Code](https://github.com/tsinghua-fib-lab/WorldArena) | [Project Page](https://world-arena.ai/) |

## Machine-readable data

- [`docs/assets/benchmarks.json`](docs/assets/benchmarks.json): canonical benchmark, target, sub-target, protocol, metric, data-source, year, and domain metadata
- [`docs/assets/metadata.json`](docs/assets/metadata.json): taxonomy labels and release-window definitions
- [Interactive project page](https://axbhb.github.io/world-model-evaluation-survey/)
