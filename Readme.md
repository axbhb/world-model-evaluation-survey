# World Model Benchmark List

This list follows the table style of the referenced Awesome-Multimodal-Large-Language-Models benchmark page: `Title`, `Venue`, `Date`, `Code`, and `Page`.

Taxonomy and category membership are synchronized to **Figure 4 and Tables 3–9** of the supplied survey. Repeated rows are intentionally preserved across categories when a benchmark belongs to more than one category. Venue/date/code/page metadata are preserved from the previous Markdown where available; newly added entries use the survey reference metadata, with `-` when no exact repository or project-page URL is available in the supplied local sources.

---

<font size=5><center><b> Table of Contents </b></center></font>

- [Visual and Temporal Quality](#visual-and-temporal-quality)
- [Spatial and State Consistency](#spatial-and-state-consistency)
- [Long-Horizon Memory and State Persistence](#long-horizon-memory-and-state-persistence)
- [Physical Plausibility](#physical-plausibility)
- [Causal and Counterfactual Reasoning](#causal-and-counterfactual-reasoning)
- [Control Fidelity and Interactive Dynamics](#control-fidelity-and-interactive-dynamics)
- [Functional Utility](#functional-utility)

---

## Visual and Temporal Quality

| Title | Venue | Date | Code | Page |
|:--|:--:|:--:|:--:|:--:|
| [**FETV: A Benchmark for Fine-Grained Evaluation of Open-Domain Text-to-Video Generation**](https://arxiv.org/abs/2311.01813) | NeurIPS Datasets and Benchmarks | 2023-11 | [Github](https://github.com/llyx97/FETV) | - |
| [**VBench: Comprehensive Benchmark Suite for Video Generative Models**](https://arxiv.org/abs/2311.17982) | CVPR | 2023-11 | [Github](https://github.com/Vchitect/VBench) | [Page](https://vchitect.github.io/VBench-project/) |
| [**VBench++: Comprehensive and Versatile Benchmark Suite for Video Generative Models**](https://arxiv.org/abs/2411.13503) | IEEE TPAMI | 2024-11 | [Github](https://github.com/Vchitect/VBench) | [Page](https://vchitect.github.io/VBench-project/) |
| [**EvalCrafter: Benchmarking and Evaluating Large Video Generation Models**](https://arxiv.org/abs/2310.11440) | CVPR | 2023-10 | [Github](https://github.com/evalcrafter/EvalCrafter) | [Page](https://evalcrafter.github.io/) |
| [**VideoScore: Building Automatic Metrics to Simulate Fine-grained Human Feedback for Video Generation**](https://arxiv.org/abs/2406.15252) | EMNLP | 2024-06 | [Github](https://github.com/TIGER-AI-Lab/VideoScore) | [Page](https://tiger-ai-lab.github.io/VideoScore/) |
| [**ChronoMagic-Bench: A Benchmark for Metamorphic Evaluation of Text-to-Time-lapse Video Generation**](https://arxiv.org/abs/2406.18522) | NeurIPS Datasets and Benchmarks Spotlight | 2024-06 | [Github](https://github.com/PKU-YuanGroup/ChronoMagic-Bench) | [Page](https://pku-yuangroup.github.io/ChronoMagic-Bench/) |
| [**WorldScore: A Unified Evaluation Benchmark for World Generation**](https://arxiv.org/abs/2504.00983) | ICCV | 2025-04 | [Github](https://github.com/haoyi-duan/WorldScore) | [Page](https://haoyi-duan.github.io/WorldScore/) |
| [**VMBench: A Benchmark for Perception-Aligned Video Motion Generation**](https://arxiv.org/abs/2503.10076) | ICCV | 2025-03 | [Github](https://github.com/AMAP-ML/VMBench) | [Page](https://amap-ml.github.io/VMBench-Website/) |
| [**EWMBench: Evaluating Scene, Motion, and Semantic Quality in Embodied World Models**](https://arxiv.org/abs/2505.09694) | BMVC | 2025-05 | [Github](https://github.com/AgibotTech/EWMBench) | - |
| [**WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models**](https://arxiv.org/abs/2602.08971) | arXiv | 2026-02 | [Github](https://github.com/tsinghua-fib-lab/WorldArena) | [Page](https://world-arena.ai/) |
| [**Matrix-Game: Interactive World Foundation Model**](https://arxiv.org/abs/2506.18701) | arXiv | 2025-06 | [Github](https://github.com/SkyworkAI/Matrix-Game) | [Page](https://matrix-game-homepage.github.io/) |
| [**WorldMark: A Unified Benchmark Suite for Interactive Video World Models**](https://arxiv.org/abs/2604.21686) | arXiv | 2026-04 | [Github](https://github.com/alaya-studio/WorldMark) | [Page](https://alaya-studio.github.io/WorldMark/) |
| [**4DWorldBench: A Comprehensive Evaluation Framework for 3D/4D World Generation Models**](https://arxiv.org/abs/2511.19836) | CVPR | 2025-11 | - | [Page](https://yeppp27.github.io/4DWorldBench.github.io/) |
| [**TC-Bench: Benchmarking Temporal Compositionality in Text-to-Video and Image-to-Video Generation**](https://arxiv.org/abs/2406.08656) | ACL Findings | 2024-06 | [Github](https://github.com/weixi-feng/TC-Bench) | [Page](https://weixi-feng.github.io/tc-bench/) |
| [**WorldLens: Full-Spectrum Evaluations of Driving World Models in Real World**](https://arxiv.org/abs/2512.10958) | CVPR Oral | 2025-12 | [Github](https://github.com/worldbench/WorldLens) | [Page](https://worldbench.github.io/worldlens) |
| [**WorldArena 2.0: Extending Embodied World Model Benchmarking on Modality, Functionality and Platform**](https://arxiv.org/abs/2605.17912) | arXiv | 2026-05 | [Github](https://github.com/tsinghua-fib-lab/WorldArena) | [Page](https://world-arena.ai/) |
| [**DrivingGen: A Comprehensive Benchmark for Generative Video World Models in Autonomous Driving**](https://arxiv.org/abs/2601.01528) | ICLR | 2026-01 | - | [Page](https://drivinggen-bench.github.io/) |
| [**WBench: A Comprehensive Multi-Turn Benchmark for Interactive Video World Model Evaluation**](https://arxiv.org/abs/2605.25874) | arXiv | 2026-05 | - | - |
| [**Pedra: Evaluating the Realism of Pedestrian Dynamics in Video Generation**](https://arxiv.org/abs/2510.20182) | arXiv | 2025-10 | - | - |
| [**Can World Simulators Reason? Gen-ViRe: A Generative Visual Reasoning Benchmark**](https://arxiv.org/abs/2511.13853) | arXiv | 2025-11 | - | - |

## Spatial and State Consistency

| Title | Venue | Date | Code | Page |
|:--|:--:|:--:|:--:|:--:|
| [**VBench: Comprehensive Benchmark Suite for Video Generative Models**](https://arxiv.org/abs/2311.17982) | CVPR | 2023-11 | [Github](https://github.com/Vchitect/VBench) | [Page](https://vchitect.github.io/VBench-project/) |
| [**VBench++: Comprehensive and Versatile Benchmark Suite for Video Generative Models**](https://arxiv.org/abs/2411.13503) | IEEE TPAMI | 2024-11 | [Github](https://github.com/Vchitect/VBench) | [Page](https://vchitect.github.io/VBench-project/) |
| [**WorldMark: A Unified Benchmark Suite for Interactive Video World Models**](https://arxiv.org/abs/2604.21686) | arXiv | 2026-04 | [Github](https://github.com/alaya-studio/WorldMark) | [Page](https://alaya-studio.github.io/WorldMark/) |
| [**WorldLens: Full-Spectrum Evaluations of Driving World Models in Real World**](https://arxiv.org/abs/2512.10958) | CVPR Oral | 2025-12 | [Github](https://github.com/worldbench/WorldLens) | [Page](https://worldbench.github.io/worldlens) |
| [**WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models**](https://arxiv.org/abs/2602.08971) | arXiv | 2026-02 | [Github](https://github.com/tsinghua-fib-lab/WorldArena) | [Page](https://world-arena.ai/) |
| [**WorldScore: A Unified Evaluation Benchmark for World Generation**](https://arxiv.org/abs/2504.00983) | ICCV | 2025-04 | [Github](https://github.com/haoyi-duan/WorldScore) | [Page](https://haoyi-duan.github.io/WorldScore/) |
| [**DrivingGen: A Comprehensive Benchmark for Generative Video World Models in Autonomous Driving**](https://arxiv.org/abs/2601.01528) | ICLR | 2026-01 | - | [Page](https://drivinggen-bench.github.io/) |
| [**EWMBench: Evaluating Scene, Motion, and Semantic Quality in Embodied World Models**](https://arxiv.org/abs/2505.09694) | BMVC | 2025-05 | [Github](https://github.com/AgibotTech/EWMBench) | - |
| [**What-If World: A Causal Benchmark for General World Models in Embodied Scenarios**](https://arxiv.org/abs/2605.27589) | arXiv | 2026-05 | - | - |
| [**4DWorldBench: A Comprehensive Evaluation Framework for 3D/4D World Generation Models**](https://arxiv.org/abs/2511.19836) | CVPR | 2025-11 | - | [Page](https://yeppp27.github.io/4DWorldBench.github.io/) |
| [**Matrix-Game: Interactive World Foundation Model**](https://arxiv.org/abs/2506.18701) | arXiv | 2025-06 | [Github](https://github.com/SkyworkAI/Matrix-Game) | [Page](https://matrix-game-homepage.github.io/) |
| [**LoopNav: Benchmarking Spatial Consistency in World Models**](https://arxiv.org/abs/2505.22976) | arXiv | 2025-05 | - | - |
| [**MIND: Benchmarking Memory Consistency and Action Control in World Models**](https://arxiv.org/abs/2602.08025) | arXiv | 2026-02 | - | - |
| [**MBench: A Comprehensive Benchmark on Memory Capability for Video World Models**](https://arxiv.org/abs/2606.00793) | arXiv | 2026-06 | - | - |
| [**Out of Sight, Out of Mind? Evaluating State Evolution in Video World Models**](https://arxiv.org/abs/2603.13215) | arXiv | 2026-03 | - | - |
| [**Quantitative Video World Model Evaluation for Geometric-Consistency**](https://arxiv.org/abs/2605.15185) | arXiv | 2026-05 | - | - |

## Long-Horizon Memory and State Persistence

| Title | Venue | Date | Code | Page |
|:--|:--:|:--:|:--:|:--:|
| [**WorldPrediction: A Benchmark for High-level World Modeling and Long-horizon Procedural Planning**](https://arxiv.org/abs/2506.04363) | ICML Workshop | 2025-06 | - | [Page](https://github.com/worldprediction/worldprediction.github.io) |
| [**SmallWorlds: Assessing Dynamics Understanding of World Models in Isolated Environments**](https://arxiv.org/abs/2511.23465) | arXiv | 2025-11 | - | - |
| [**World Reasoning Arena**](https://arxiv.org/abs/2603.25887) | arXiv | 2026-03 | [Github](https://github.com/MBZUAI-IFM/WR-Arena) | - |
| [**WorldMark: A Unified Benchmark Suite for Interactive Video World Models**](https://arxiv.org/abs/2604.21686) | arXiv | 2026-04 | [Github](https://github.com/alaya-studio/WorldMark) | [Page](https://alaya-studio.github.io/WorldMark/) |
| [**MBench: A Comprehensive Benchmark on Memory Capability for Video World Models**](https://arxiv.org/abs/2606.00793) | arXiv | 2026-06 | - | - |
| [**MIND: Benchmarking Memory Consistency and Action Control in World Models**](https://arxiv.org/abs/2602.08025) | arXiv | 2026-02 | - | - |
| [**WBench: A Comprehensive Multi-Turn Benchmark for Interactive Video World Model Evaluation**](https://arxiv.org/abs/2605.25874) | arXiv | 2026-05 | - | - |
| [**WorldOlympiad: Can Your World Model Survive a Triathlon?**](https://arxiv.org/abs/2606.11129) | arXiv | 2026-06 | - | - |
| [**World-Ego Modeling for Long-Horizon Evolution in Hybrid Embodied Tasks (Introduces HTEWorld)**](https://arxiv.org/abs/2605.19957) | arXiv | 2026-05 | - | - |
| [**RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation**](https://arxiv.org/abs/2604.19092) | CVPR Workshop | 2026-04 | [Github](https://github.com/fffstrong/RoboWM-Bench) | [Page](https://robowm-bench.github.io/RoboWM-Bench/) |

## Physical Plausibility

| Title | Venue | Date | Code | Page |
|:--|:--:|:--:|:--:|:--:|
| [**IntPhys: A Benchmark for Visual Intuitive Physics Reasoning**](https://arxiv.org/abs/1803.07616) | IEEE TPAMI | 2018-03 | - | [Page](https://intphys.cognitive-ml.fr/download.html) |
| [**IntPhys 2: Benchmarking Intuitive Physics Understanding In Complex Synthetic Environments**](https://arxiv.org/abs/2506.09849) | NeurIPS Datasets and Benchmarks | 2025-06 | [Github](https://github.com/facebookresearch/IntPhys2) | - |
| [**CLEVRER: Collision Events for Video Representation and Reasoning**](https://arxiv.org/abs/1910.01442) | ICLR | 2019-10 | [Github](https://github.com/chuangg/CLEVRER) | [Page](http://clevrer.csail.mit.edu) |
| [**CoPhy: Counterfactual Learning of Physical Dynamics**](https://arxiv.org/abs/1909.12000) | ICLR | 2019-09 | - | [Page](https://comphyreasoning.github.io/) |
| [**PHYRE: A New Benchmark for Physical Reasoning**](https://arxiv.org/abs/1908.05656) | NeurIPS | 2019-08 | [Github](https://github.com/facebookresearch/phyre) | [Page](https://player.phyre.ai) |
| [**CRAFT: A Benchmark for Causal Reasoning About Forces and inTeractions**](https://arxiv.org/abs/2012.04293) | Findings of ACL | 2020-12 | [Github](https://github.com/hucvl/craft) | - |
| [**Physion: Evaluating Physical Prediction from Vision in Humans and Machines**](https://arxiv.org/abs/2106.08261) | NeurIPS Datasets and Benchmarks | 2021-06 | [Github](https://github.com/cogtoolslab/physics-benchmarking-neurips2021) | [Page](https://physion-benchmark.github.io/) |
| [**Physion++: Evaluating Physical Scene Understanding that Requires Online Inference of Different Physical Properties**](https://arxiv.org/abs/2306.15668) | NeurIPS | 2023-06 | - | [Page](https://dingmyu.github.io/physion_v2/) |
| [**ComPhy: Compositional Physical Reasoning of Objects and Events from Videos**](https://arxiv.org/abs/2205.01089) | ICLR | 2022-05 | - | [Page](https://comphyreasoning.github.io/) |
| [**ContPhy: Continuum Physical Concept Learning and Reasoning from Videos**](https://arxiv.org/abs/2402.06119) | ICML | 2024-02 | - | [Page](https://physical-reasoning-project.github.io/) |
| [**A Physical Coherence Benchmark for Evaluating Video Generation Models via Optical Flow-guided Frame Prediction**](https://arxiv.org/abs/2502.05503) | arXiv | 2025-02 | [Github](https://github.com/Jeckinchen/PhyCoBench) | - |
| [**VideoPhy: Evaluating Physical Commonsense for Video Generation**](https://arxiv.org/abs/2406.03520) | ICLR | 2024-06 | [Github](https://github.com/Hritikbansal/videophy) | - |
| [**VideoPhy-2: A Challenging Action-Centric Physical Commonsense Evaluation in Video Generation**](https://arxiv.org/abs/2503.06800) | ICLR | 2025-03 | [Github](https://github.com/Hritikbansal/videophy) | [Page](https://videophy2.github.io/) |
| [**Towards World Simulator: Crafting Physical Commonsense-Based Benchmark for Video Generation**](https://arxiv.org/abs/2410.05363) | ICML | 2024-10 | [Github](https://github.com/OpenGVLab/PhyGenBench) | [Page](https://phygenbench123.github.io/) |
| [**T2VPhysBench: A First-Principles Benchmark for Physical Consistency in Text-to-Video Generation**](https://arxiv.org/abs/2505.00337) | arXiv | 2025-05 | - | - |
| [**Do generative video models understand physical principles?**](https://arxiv.org/abs/2501.09038) | WACV | 2025-01 | [Github](https://github.com/google-deepmind/physics-iq-benchmark) | [Page](https://physics-iq.github.io/) |
| [**WorldBench: Disambiguating Physics for Diagnostic Evaluation of World Models**](https://arxiv.org/abs/2601.21282) | arXiv | 2026-01 | - | [Page](https://world-bench.github.io/) |
| [**PhyWorldBench: A Comprehensive Evaluation of Physical Realism in Text-to-Video Models**](https://arxiv.org/abs/2507.13428) | ICLR | 2025-07 | [Github](https://github.com/g-jing/phy-world-bench) | [Page](https://research.nvidia.com/labs/dir/phyworldbench/) |
| [**WorldModelBench: Judging Video Generation Models As World Models**](https://arxiv.org/abs/2502.20694) | CVPR Workshop | 2025-02 | [Github](https://github.com/WorldModelBench-Team/WorldModelBench) | [Page](https://worldmodelbench-team.github.io) |
| [**VBench-2.0: Advancing Video Generation Benchmark Suite for Intrinsic Faithfulness**](https://arxiv.org/abs/2503.21755) | arXiv | 2025-03 | [Github](https://github.com/Vchitect/VBench) | [Page](https://vchitect.github.io/VBench-project/) |
| [**Matrix-Game: Interactive World Foundation Model**](https://arxiv.org/abs/2506.18701) | arXiv | 2025-06 | [Github](https://github.com/SkyworkAI/Matrix-Game) | [Page](https://matrix-game-homepage.github.io/) |
| [**T2VWorldBench: A Benchmark for Evaluating World Knowledge in Text-to-Video Generation**](https://arxiv.org/abs/2507.18107) | WACV | 2025-07 | - | - |
| [**4DWorldBench: A Comprehensive Evaluation Framework for 3D/4D World Generation Models**](https://arxiv.org/abs/2511.19836) | CVPR | 2025-11 | - | [Page](https://yeppp27.github.io/4DWorldBench.github.io/) |
| [**RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation**](https://arxiv.org/abs/2604.19092) | CVPR Workshop | 2026-04 | [Github](https://github.com/fffstrong/RoboWM-Bench) | [Page](https://robowm-bench.github.io/RoboWM-Bench/) |
| [**DreamGen: Unlocking Generalization in Robot Learning through Video World Models**](https://arxiv.org/abs/2505.12705) | CoRL | 2025-05 | [Github](https://github.com/NVIDIA/GR00T-Dreams) | [Page](https://research.nvidia.com/labs/gear/dreamgen/) |
| [**WorldLens: Full-Spectrum Evaluations of Driving World Models in Real World**](https://arxiv.org/abs/2512.10958) | CVPR Oral | 2025-12 | [Github](https://github.com/worldbench/WorldLens) | [Page](https://worldbench.github.io/worldlens) |
| [**RigidBench: Evaluating Rigid-Body Physics in Video Generation Models**](https://openreview.net/forum?id=HEjWQkFrzR) | OpenReview | 2026 | - | - |
| [**Morpheus: Benchmarking physical reasoning of video generative models with real physical experiments**](https://arxiv.org/abs/2504.02918) | arXiv | 2025-04 | - | - |
| [**What-If World: A Causal Benchmark for General World Models in Embodied Scenarios**](https://arxiv.org/abs/2605.27589) | arXiv | 2026-05 | - | - |
| [**PhyGround: Benchmarking Physical Reasoning in Generative World Models**](https://arxiv.org/abs/2605.10806) | arXiv | 2026-05 | - | - |
| [**Physion-Eval: Evaluating Physical Realism in Generated Video via Human Reasoning**](https://arxiv.org/abs/2603.19607) | arXiv | 2026-03 | - | - |
| [**CRONOS: Benchmarking Counterfactual Physical Consistency in Video Models**](https://arxiv.org/abs/2605.23699) | arXiv | 2026-05 | - | - |
| [**VACT: A Video Automatic Causal Testing System and a Benchmark**](https://arxiv.org/abs/2503.06163) | arXiv | 2025-03 | - | - |
| [**Out of Sight, Out of Mind? Evaluating State Evolution in Video World Models**](https://arxiv.org/abs/2603.13215) | arXiv | 2026-03 | - | - |
| [**PhysicsMind: Sim and Real Mechanics Benchmarking for Physical Reasoning and Prediction in Foundational VLMs and World Models**](https://arxiv.org/abs/2601.16007) | arXiv | 2026-01 | - | - |
| [**Quantitative Video World Model Evaluation for Geometric-Consistency**](https://arxiv.org/abs/2605.15185) | arXiv | 2026-05 | - | - |
| [**HOCA-Bench: Beyond Semantic Perception to Predictive World Modeling via Hegelian Ontological-Causal Anomalies**](https://arxiv.org/abs/2602.19571) | arXiv | 2026-02 | - | - |

## Causal and Counterfactual Reasoning

### Causal Reasoning over Observed Worlds

| Title | Venue | Date | Code | Page |
|:--|:--:|:--:|:--:|:--:|
| [**CLEVRER: Collision Events for Video Representation and Reasoning**](https://arxiv.org/abs/1910.01442) | ICLR | 2019-10 | [Github](https://github.com/chuangg/CLEVRER) | [Page](http://clevrer.csail.mit.edu) |
| [**CATER: A diagnostic dataset for Compositional Actions and TEmporal Reasoning**](https://arxiv.org/abs/1910.04744) | ICLR | 2019-10 | [Github](https://github.com/rohitgirdhar/CATER) | [Page](https://rohitgirdhar.github.io/CATER/) |
| [**NExT-QA: Next Phase of Question-Answering to Explaining Temporal Actions**](https://arxiv.org/abs/2105.08276) | CVPR | 2021-05 | [Github](https://github.com/doc-doc/NExT-QA) | - |
| [**From Representation to Reasoning: Towards both Evidence and Commonsense Reasoning for Video Question-Answering**](https://arxiv.org/abs/2205.14895) | CVPR | 2022-05 | [Github](https://github.com/bcmi/Causal-VidQA) | - |
| [**CRAFT: A Benchmark for Causal Reasoning About Forces and inTeractions**](https://arxiv.org/abs/2012.04293) | Findings of ACL | 2020-12 | [Github](https://github.com/hucvl/craft) | - |
| [**IntentQA: Context-aware Video Intent Reasoning**](https://openaccess.thecvf.com/content/ICCV2023/papers/Li_IntentQA_Context-aware_Video_Intent_Reasoning_ICCV_2023_paper.pdf) | ICCV | 2023 | [Github](https://github.com/JoseponLee/IntentQA) | - |
| [**MMWorld: Towards Multi-discipline Multi-faceted World Model Evaluation in Videos**](https://arxiv.org/abs/2406.08407) | ICLR | 2024-06 | [Github](https://github.com/UCSB-AI/MMWorld) | [Page](https://mmworld-bench.github.io/) |
| [**VCRBench: Exploring Long-form Causal Reasoning Capabilities of Large Video Language Models**](https://arxiv.org/abs/2505.08455) | CVPRW 2026 (CogVL) | 2025-05 | [Github](https://github.com/pritamqu/VCRBench) | [Page](https://pritamqu.github.io/VCRBench/) |
| [**Physion: Evaluating Physical Prediction from Vision in Humans and Machines**](https://arxiv.org/abs/2106.08261) | NeurIPS Datasets and Benchmarks | 2021-06 | [Github](https://github.com/cogtoolslab/physics-benchmarking-neurips2021) | [Page](https://physion-benchmark.github.io/) |
| [**Do generative video models understand physical principles?**](https://arxiv.org/abs/2501.09038) | WACV | 2025-01 | [Github](https://github.com/google-deepmind/physics-iq-benchmark) | [Page](https://physics-iq.github.io/) |
| [**WorldPrediction: A Benchmark for High-level World Modeling and Long-horizon Procedural Planning**](https://arxiv.org/abs/2506.04363) | ICML Workshop | 2025-06 | - | [Page](https://github.com/worldprediction/worldprediction.github.io) |
| [**World Reasoning Arena**](https://arxiv.org/abs/2603.25887) | arXiv | 2026-03 | [Github](https://github.com/MBZUAI-IFM/WR-Arena) | - |

### Counterfactual Reasoning over Intervened Worlds

| Title | Venue | Date | Code | Page |
|:--|:--:|:--:|:--:|:--:|
| [**CoPhy: Counterfactual Learning of Physical Dynamics**](https://arxiv.org/abs/1909.12000) | ICLR | 2019-09 | - | [Page](https://comphyreasoning.github.io/) |
| [**ComPhy: Compositional Physical Reasoning of Objects and Events from Videos**](https://arxiv.org/abs/2205.01089) | ICLR | 2022-05 | - | [Page](https://comphyreasoning.github.io/) |
| [**ACQUIRED: A Dataset for Answering Counterfactual Questions In Real-Life Videos**](https://arxiv.org/abs/2311.01620) | EMNLP | 2023-11 | [Github](https://github.com/PlusLabNLP/acquired) | - |
| [**CausalVQA: A Physically Grounded Causal Reasoning Benchmark for Video Models**](https://arxiv.org/abs/2506.09943) | arXiv | 2025-06 | [Github](https://github.com/facebookresearch/CausalVQA) | [Page](https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/) |
| [**What-If World: A Causal Benchmark for General World Models in Embodied Scenarios**](https://arxiv.org/abs/2605.27589) | arXiv | 2026-05 | - | - |

## Control Fidelity and Interactive Dynamics

### Pre-specified Control Fidelity

| Title | Venue | Date | Code | Page |
|:--|:--:|:--:|:--:|:--:|
| [**T2V-CompBench: A Comprehensive Benchmark for Compositional Text-to-video Generation**](https://arxiv.org/abs/2407.14505) | CVPR | 2024-07 | [Github](https://github.com/KaiyueSun98/T2V-CompBench) | - |
| [**TC-Bench: Benchmarking Temporal Compositionality in Text-to-Video and Image-to-Video Generation**](https://arxiv.org/abs/2406.08656) | ACL Findings | 2024-06 | [Github](https://github.com/weixi-feng/TC-Bench) | [Page](https://weixi-feng.github.io/tc-bench/) |
| [**Is Your World Simulator a Good Story Presenter? A Consecutive Events-Based Benchmark for Future Long Video Generation**](https://arxiv.org/abs/2412.16211) | CVPR 2025 | 2024-12 | [Github](https://github.com/ypwang61/StoryEval) | [Page](https://ypwang61.github.io/project/StoryEval/) |
| [**VideoPhy: Evaluating Physical Commonsense for Video Generation**](https://arxiv.org/abs/2406.03520) | ICLR | 2024-06 | [Github](https://github.com/Hritikbansal/videophy) | - |
| [**VideoPhy-2: A Challenging Action-Centric Physical Commonsense Evaluation in Video Generation**](https://arxiv.org/abs/2503.06800) | ICLR | 2025-03 | [Github](https://github.com/Hritikbansal/videophy) | [Page](https://videophy2.github.io/) |
| [**Towards World Simulator: Crafting Physical Commonsense-Based Benchmark for Video Generation**](https://arxiv.org/abs/2410.05363) | ICML | 2024-10 | [Github](https://github.com/OpenGVLab/PhyGenBench) | [Page](https://phygenbench123.github.io/) |
| [**PhyWorldBench: A Comprehensive Evaluation of Physical Realism in Text-to-Video Models**](https://arxiv.org/abs/2507.13428) | ICLR | 2025-07 | [Github](https://github.com/g-jing/phy-world-bench) | [Page](https://research.nvidia.com/labs/dir/phyworldbench/) |
| [**OSCBench: Benchmarking Object State Change in Text-to-Video Generation**](https://arxiv.org/abs/2603.11698) | arXiv | 2026-03 | - | - |
| [**Wan-Move: Motion-controllable Video Generation via Latent Trajectory Guidance**](https://arxiv.org/abs/2512.08765) | NeurIPS | 2025-12 | [Github](https://github.com/ali-vilab/Wan-Move) | [Page](https://wan-move.github.io/) |
| [**MagicMotion: Controllable Video Generation with Dense-to-Sparse Trajectory Guidance**](https://arxiv.org/abs/2503.16421) | ICCV | 2025-03 | [Github](https://github.com/quanhaol/MagicMotion) | [Page](https://quanhaol.github.io/magicmotion-site/) |
| [**WorldScore: A Unified Evaluation Benchmark for World Generation**](https://arxiv.org/abs/2504.00983) | ICCV | 2025-04 | [Github](https://github.com/haoyi-duan/WorldScore) | [Page](https://haoyi-duan.github.io/WorldScore/) |
| [**4DWorldBench: A Comprehensive Evaluation Framework for 3D/4D World Generation Models**](https://arxiv.org/abs/2511.19836) | CVPR | 2025-11 | - | [Page](https://yeppp27.github.io/4DWorldBench.github.io/) |
| [**DrivingGen: A Comprehensive Benchmark for Generative Video World Models in Autonomous Driving**](https://arxiv.org/abs/2601.01528) | ICLR | 2026-01 | - | [Page](https://drivinggen-bench.github.io/) |
| [**ACT-Bench: Towards Action Controllable World Models for Autonomous Driving**](https://arxiv.org/abs/2412.05337) | arXiv | 2024-12 | - | - |
| [**What-If World: A Causal Benchmark for General World Models in Embodied Scenarios**](https://arxiv.org/abs/2605.27589) | arXiv | 2026-05 | - | - |
| [**Omni-WorldBench: Towards a Comprehensive Interaction-Centric Evaluation for World Models**](https://arxiv.org/abs/2603.22212) | arXiv | 2026-03 | [Github](https://github.com/AMAP-ML/Omni-WorldBench) | - |

### Interactive Action Fidelity

| Title | Venue | Date | Code | Page |
|:--|:--:|:--:|:--:|:--:|
| [**WorldMark: A Unified Benchmark Suite for Interactive Video World Models**](https://arxiv.org/abs/2604.21686) | arXiv | 2026-04 | [Github](https://github.com/alaya-studio/WorldMark) | [Page](https://alaya-studio.github.io/WorldMark/) |
| [**World Reasoning Arena**](https://arxiv.org/abs/2603.25887) | arXiv | 2026-03 | [Github](https://github.com/MBZUAI-IFM/WR-Arena) | - |
| [**WorldSimBench: Towards Video Generation Models as World Simulators**](https://arxiv.org/abs/2410.18072) | ICML | 2024-10 | - | [Page](https://iranqin.github.io/WorldSimBench.github.io/) |
| [**WBench: A Comprehensive Multi-Turn Benchmark for Interactive Video World Model Evaluation**](https://arxiv.org/abs/2605.25874) | arXiv | 2026-05 | - | - |
| [**iWorld-Bench: A Benchmark for Interactive World Models with a Unified Action Generation Framework**](https://arxiv.org/abs/2605.03941) | arXiv | 2026-05 | - | - |
| [**MIND: Benchmarking Memory Consistency and Action Control in World Models**](https://arxiv.org/abs/2602.08025) | arXiv | 2026-02 | - | - |
| [**ACWM-Phys: Investigating Generalized Physical Interaction in Action-Conditioned Video World Models**](https://arxiv.org/abs/2605.08567) | arXiv | 2026-05 | - | - |
| [**RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation**](https://arxiv.org/abs/2604.19092) | CVPR Workshop | 2026-04 | [Github](https://github.com/fffstrong/RoboWM-Bench) | [Page](https://robowm-bench.github.io/RoboWM-Bench/) |
| [**WorldArena 2.0: Extending Embodied World Model Benchmarking on Modality, Functionality and Platform**](https://arxiv.org/abs/2605.17912) | arXiv | 2026-05 | [Github](https://github.com/tsinghua-fib-lab/WorldArena) | [Page](https://world-arena.ai/) |

## Functional Utility

### World Model as Data Engine

| Title | Venue | Date | Code | Page |
|:--|:--:|:--:|:--:|:--:|
| [**WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models**](https://arxiv.org/abs/2602.08971) | arXiv | 2026-02 | [Github](https://github.com/tsinghua-fib-lab/WorldArena) | [Page](https://world-arena.ai/) |
| [**WorldArena 2.0: Extending Embodied World Model Benchmarking on Modality, Functionality and Platform**](https://arxiv.org/abs/2605.17912) | arXiv | 2026-05 | [Github](https://github.com/tsinghua-fib-lab/WorldArena) | [Page](https://world-arena.ai/) |

### World Model as Policy Evaluator

| Title | Venue | Date | Code | Page |
|:--|:--:|:--:|:--:|:--:|
| [**WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models**](https://arxiv.org/abs/2602.08971) | arXiv | 2026-02 | [Github](https://github.com/tsinghua-fib-lab/WorldArena) | [Page](https://world-arena.ai/) |
| [**Scalable Policy Evaluation with Video World Models**](https://arxiv.org/abs/2511.11520) | arXiv | 2025-11 | - | - |

### World Model as Planner

| Title | Venue | Date | Code | Page |
|:--|:--:|:--:|:--:|:--:|
| [**WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models**](https://arxiv.org/abs/2602.08971) | arXiv | 2026-02 | [Github](https://github.com/tsinghua-fib-lab/WorldArena) | [Page](https://world-arena.ai/) |
| [**WorldArena 2.0: Extending Embodied World Model Benchmarking on Modality, Functionality and Platform**](https://arxiv.org/abs/2605.17912) | arXiv | 2026-05 | [Github](https://github.com/tsinghua-fib-lab/WorldArena) | [Page](https://world-arena.ai/) |
| [**World-in-World: World Models in a Closed-Loop World**](https://arxiv.org/abs/2510.18135) | ICLR | 2025-10 | [Github](https://github.com/World-In-World/world-in-world) | [Page](https://world-in-world.github.io/) |
| [**EVA: An Embodied World Model for Future Video Anticipation**](https://arxiv.org/abs/2410.15461) | ICML | 2024-10 | [Github](https://github.com/litwellchi/EmbodiedVideoAnticipator) | [Page](https://sites.google.com/view/eva-public) |
| [**WorldLens: Full-Spectrum Evaluations of Driving World Models in Real World**](https://arxiv.org/abs/2512.10958) | CVPR Oral | 2025-12 | [Github](https://github.com/worldbench/WorldLens) | [Page](https://worldbench.github.io/worldlens) |
| [**stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation**](https://arxiv.org/abs/2605.21800) | arXiv | 2026-05 | [Github](https://github.com/galilai-group/stable-worldmodel) | [Page](https://galilai-group.github.io/stable-worldmodel/) |
| [**RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation**](https://arxiv.org/abs/2604.19092) | CVPR Workshop | 2026-04 | [Github](https://github.com/fffstrong/RoboWM-Bench) | [Page](https://robowm-bench.github.io/RoboWM-Bench/) |
| [**WorldSimBench: Towards Video Generation Models as World Simulators**](https://arxiv.org/abs/2410.18072) | ICML | 2024-10 | - | [Page](https://iranqin.github.io/WorldSimBench.github.io/) |

### World Model as Interactive Training Environment

| Title | Venue | Date | Code | Page |
|:--|:--:|:--:|:--:|:--:|
| [**WorldArena 2.0: Extending Embodied World Model Benchmarking on Modality, Functionality and Platform**](https://arxiv.org/abs/2605.17912) | arXiv | 2026-05 | [Github](https://github.com/tsinghua-fib-lab/WorldArena) | [Page](https://world-arena.ai/) |

