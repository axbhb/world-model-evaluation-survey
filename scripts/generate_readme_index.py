import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "docs" / "assets"
manifest = json.loads((ASSETS / "benchmarks.json").read_text(encoding="utf-8"))
records = []
for i in range(1, 5):
    records += json.loads((ASSETS / f"benchmarks-{i}.json").read_text(encoding="utf-8"))
meta = {r["shortName"]: dict(r) for r in records}

# Apply the aliases/additions/removals from the latest canonical manifest.
for old_name, new_name in manifest.get("aliases", {}).items():
    if old_name in meta:
        meta[new_name] = dict(meta.pop(old_name))
        meta[new_name]["shortName"] = new_name
for name, record in manifest.get("added", {}).items():
    meta[name] = dict(record)
for name in manifest.get("removed", []):
    meta.pop(name, None)

title_override = {
    "PEDRA": "PEDRA: Evaluating the Realism of Pedestrian Dynamics in Video Generation",
    "GameWorld Score": "Matrix-Game: Interactive World Foundation Model",
    "TC-Bench": "TC-Bench: Benchmarking Temporal Compositionality in Text-to-Video and Image-to-Video Generation",
    "VMBench": "VMBench: A Benchmark for Perception-Aligned Video Motion Generation",
    "WorldArena 2.0": "WorldArena 2.0: Extending Embodied World Model Benchmarking on Modality, Functionality and Platform",
    "DrivingGen": "DrivingGen: A Comprehensive Benchmark for Generative Video World Models in Autonomous Driving",
    "WBench": "WBench: A Comprehensive Multi-Turn Benchmark for Interactive Video World Model Evaluation",
    "Gen-ViRe": "Can World Simulators Reason? Gen-ViRe: A Generative Visual Reasoning Benchmark",
    "MIND": "MIND: Benchmarking Memory Consistency and Action Control in World Models",
    "MBench": "MBench: A Comprehensive Benchmark on Memory Capability for Video World Models",
    "LoopNav": "LoopNav: Benchmarking Spatial Consistency in World Models",
    "CRONOS": "CRONOS: Benchmarking Counterfactual Physical Consistency in Video Models",
    "HOCA-Bench": "HOCA-Bench: Beyond Semantic Perception to Predictive World Modeling via Hegelian Ontological-Causal Anomalies",
    "PhysicsMind": "PhysicsMind: Sim and Real Mechanics Benchmarking for Physical Reasoning and Prediction in Foundational VLMs and World Models",
    "Physion-Eval": "Physion-Eval: Evaluating Physical Realism in Generated Video via Human Reasoning",
    "PhyGround": "PhyGround: Benchmarking Physical Reasoning in Generative World Models",
    "World-in-World": "World-in-World: World Models in a Closed-Loop World",
    "EVA-Bench": "EVA: An Embodied World Model for Future Video Anticipation",
    "MoveBench": "Wan-Move: Motion-Controllable Video Generation via Latent Trajectory Guidance",
    "MagicBench": "MagicMotion: Controllable Video Generation with Dense-to-Sparse Trajectory Guidance",
    "ACT-Bench": "ACT-Bench: Towards Action Controllable World Models for Autonomous Driving",
    "VBench-2.0": "VBench-2.0: Advancing Video Generation Benchmark Suite for Intrinsic Faithfulness",
    "T2V-CompBench": "T2V-CompBench: A Comprehensive Benchmark for Compositional Text-to-Video Generation",
    "WorldPrediction": "WorldPrediction: A Benchmark for High-Level World Modeling and Long-Horizon Procedural Planning",
    "HTEWorld": "World-Ego Modeling for Long-Horizon Evolution in Hybrid Embodied Tasks",
    "CausalSpatial": "CausalSpatial: A Benchmark for Object-Centric Causal Spatial Reasoning",
}

# Prefer the recognizable publication venue used in the earlier linked README when known.
venue_override = {
    "FETV": "NeurIPS Datasets and Benchmarks",
    "VBench": "CVPR",
    "VBench++": "IEEE TPAMI",
    "EvalCrafter": "CVPR",
    "ChronoMagic-Bench": "NeurIPS Datasets and Benchmarks Spotlight",
    "WorldScore": "ICCV",
    "VMBench": "ICCV",
    "EWMBench": "BMVC",
    "4DWorldBench": "CVPR",
    "TC-Bench": "ACL Findings",
    "WorldLens": "CVPR Oral",
    "DrivingGen": "ICLR",
    "PEDRA": "CVPR",
    "WorldPrediction": "ICML Workshop",
    "RoboWM-Bench": "CVPR",
    "IntPhys": "IEEE TPAMI",
    "IntPhys 2": "NeurIPS Datasets and Benchmarks",
    "CLEVRER": "ICLR",
    "CoPhy": "ICLR",
    "PHYRE": "NeurIPS",
    "CRAFT": "Findings of ACL",
    "Physion": "NeurIPS Datasets and Benchmarks",
    "Physion++": "NeurIPS",
    "ComPhy": "ICLR",
    "ContPhy": "ICML",
    "VideoPhy": "ICLR",
    "VideoPhy-2": "ICLR",
    "PhyGenBench": "ICML",
    "Physics-IQ": "WACV",
    "PhyWorldBench": "ICLR",
    "WorldModelBench": "NeurIPS",
    "T2VWorldBench": "WACV",
    "DreamGen Bench": "CoRL",
    "CATER": "ICLR",
    "NExT-QA": "CVPR",
    "Causal-VidQA": "CVPR",
    "IntentQA": "ICCV",
    "MMWorld": "ICLR",
    "VCRBench": "CVPR Workshop",
    "ACQUIRED": "EMNLP",
    "T2V-CompBench": "CVPR",
    "StoryEval": "CVPR",
    "MoveBench": "NeurIPS",
    "MagicBench": "ICCV",
    "OSCBench": "ACL",
    "WorldSimBench": "ICML",
    "World-in-World": "ICLR",
    "EVA-Bench": "ICML",
    "RigidBench": "ICLR Workshop",
}

code_links = {
    "FETV": "https://github.com/llyx97/FETV",
    "VBench": "https://github.com/Vchitect/VBench",
    "VBench++": "https://github.com/Vchitect/VBench",
    "EvalCrafter": "https://github.com/evalcrafter/EvalCrafter",
    "ChronoMagic-Bench": "https://github.com/PKU-YuanGroup/ChronoMagic-Bench",
    "WorldScore": "https://github.com/haoyi-duan/WorldScore",
    "VMBench": "https://github.com/AMAP-ML/VMBench",
    "EWMBench": "https://github.com/AgibotTech/EWMBench",
    "WorldArena": "https://github.com/tsinghua-fib-lab/WorldArena",
    "GameWorld Score": "https://github.com/SkyworkAI/Matrix-Game",
    "WorldMark": "https://github.com/alaya-studio/WorldMark",
    "TC-Bench": "https://github.com/weixi-feng/TC-Bench",
    "WorldLens": "https://github.com/worldbench/WorldLens",
    "WorldArena 2.0": "https://github.com/tsinghua-fib-lab/WorldArena",
    "WR-Arena": "https://github.com/MBZUAI-IFM/WR-Arena",
    "RoboWM-Bench": "https://github.com/fffstrong/RoboWM-Bench",
    "IntPhys 2": "https://github.com/facebookresearch/IntPhys2",
    "CLEVRER": "https://github.com/chuangg/CLEVRER",
    "PHYRE": "https://github.com/facebookresearch/phyre",
    "CRAFT": "https://github.com/hucvl/craft",
    "Physion": "https://github.com/cogtoolslab/physics-benchmarking-neurips2021",
    "PhyCoBench": "https://github.com/Jeckinchen/PhyCoBench",
    "VideoPhy": "https://github.com/Hritikbansal/videophy",
    "VideoPhy-2": "https://github.com/Hritikbansal/videophy",
    "PhyGenBench": "https://github.com/OpenGVLab/PhyGenBench",
    "Physics-IQ": "https://github.com/google-deepmind/physics-iq-benchmark",
    "PhyWorldBench": "https://github.com/g-jing/phy-world-bench",
    "WorldModelBench": "https://github.com/WorldModelBench-Team/WorldModelBench",
    "VBench-2.0": "https://github.com/Vchitect/VBench",
    "DreamGen Bench": "https://github.com/NVIDIA/GR00T-Dreams",
    "CATER": "https://github.com/rohitgirdhar/CATER",
    "NExT-QA": "https://github.com/doc-doc/NExT-QA",
    "Causal-VidQA": "https://github.com/bcmi/Causal-VidQA",
    "IntentQA": "https://github.com/JoseponLee/IntentQA",
    "MMWorld": "https://github.com/UCSB-AI/MMWorld",
    "VCRBench": "https://github.com/pritamqu/VCRBench",
    "ACQUIRED": "https://github.com/PlusLabNLP/acquired",
    "CausalVQA": "https://github.com/facebookresearch/CausalVQA",
    "T2V-CompBench": "https://github.com/KaiyueSun98/T2V-CompBench",
    "StoryEval": "https://github.com/ypwang61/StoryEval",
    "MoveBench": "https://github.com/ali-vilab/Wan-Move",
    "MagicBench": "https://github.com/quanhaol/MagicMotion",
    "Omni-WorldBench": "https://github.com/AMAP-ML/Omni-WorldBench",
    "World-in-World": "https://github.com/World-In-World/world-in-world",
    "EVA-Bench": "https://github.com/litwellchi/EmbodiedVideoAnticipator",
}

project_pages = {
    "VBench": "https://vchitect.github.io/VBench-project/",
    "VBench++": "https://vchitect.github.io/VBench-project/",
    "EvalCrafter": "https://evalcrafter.github.io/",
    "ChronoMagic-Bench": "https://pku-yuangroup.github.io/ChronoMagic-Bench/",
    "WorldScore": "https://haoyi-duan.github.io/WorldScore/",
    "VMBench": "https://amap-ml.github.io/VMBench-Website/",
    "WorldArena": "https://world-arena.ai/",
    "GameWorld Score": "https://matrix-game-homepage.github.io/",
    "WorldMark": "https://alaya-studio.github.io/WorldMark/",
    "4DWorldBench": "https://yeppp27.github.io/4DWorldBench.github.io/",
    "TC-Bench": "https://weixi-feng.github.io/tc-bench/",
    "WorldLens": "https://worldbench.github.io/worldlens",
    "WorldArena 2.0": "https://world-arena.ai/",
    "DrivingGen": "https://drivinggen-bench.github.io/",
    "WorldPrediction": "https://github.com/worldprediction/worldprediction.github.io",
    "RoboWM-Bench": "https://robowm-bench.github.io/RoboWM-Bench/",
    "IntPhys": "https://intphys.cognitive-ml.fr/download.html",
    "CLEVRER": "http://clevrer.csail.mit.edu",
    "CoPhy": "https://comphyreasoning.github.io/",
    "PHYRE": "https://player.phyre.ai",
    "Physion": "https://physion-benchmark.github.io/",
    "Physion++": "https://dingmyu.github.io/physion_v2/",
    "ComPhy": "https://comphyreasoning.github.io/",
    "ContPhy": "https://physical-reasoning-project.github.io/",
    "VideoPhy-2": "https://videophy2.github.io/",
    "PhyGenBench": "https://phygenbench123.github.io/",
    "Physics-IQ": "https://physics-iq.github.io/",
    "WorldBench": "https://world-bench.github.io/",
    "PhyWorldBench": "https://research.nvidia.com/labs/dir/phyworldbench/",
    "WorldModelBench": "https://worldmodelbench-team.github.io",
    "VBench-2.0": "https://vchitect.github.io/VBench-project/",
    "DreamGen Bench": "https://research.nvidia.com/labs/gear/dreamgen/",
    "MMWorld": "https://mmworld-bench.github.io/",
    "VCRBench": "https://pritamqu.github.io/VCRBench/",
    "CausalVQA": "https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/",
    "StoryEval": "https://ypwang61.github.io/project/StoryEval/",
    "MoveBench": "https://wan-move.github.io/",
    "MagicBench": "https://quanhaol.github.io/magicmotion-site/",
    "WorldSimBench": "https://iranqin.github.io/WorldSimBench.github.io/",
    "World-in-World": "https://world-in-world.github.io/",
    "EVA-Bench": "https://sites.google.com/view/eva-public",
}

# Latest Figure 4 membership and display order.
T1 = ["FETV", "VBench", "VBench++", "EvalCrafter", "ChronoMagic-Bench", "WorldScore", "VMBench", "EWMBench", "WorldArena", "GameWorld Score", "WorldMark", "4DWorldBench", "TC-Bench", "WorldLens", "WorldArena 2.0", "DrivingGen", "WBench", "PEDRA", "Gen-ViRe", "iWorld-Bench"]
T2 = ["VBench", "VBench++", "WorldMark", "GameWorld Score", "EWMBench", "WorldArena", "WorldLens", "DrivingGen", "WorldScore", "4DWorldBench", "PDI-Bench", "LoopNav", "MIND", "MBench", "STEVO-Bench", "CausalSpatial", "What-If World", "WorldOlympiad", "HOCA-Bench"]
T3 = ["WorldPrediction", "SmallWorlds", "WR-Arena", "WorldMark", "MBench", "MIND", "WBench", "WorldOlympiad", "HTEWorld", "RoboWM-Bench", "iWorld-Bench"]
T4 = ["IntPhys", "IntPhys 2", "CLEVRER", "CoPhy", "PHYRE", "CRAFT", "Physion", "Physion++", "ComPhy", "ContPhy", "PhyCoBench", "VideoPhy", "VideoPhy-2", "PhyGenBench", "T2VPhysBench", "Physics-IQ", "WorldBench", "PhyWorldBench", "T2VWorldBench", "WorldModelBench", "VBench-2.0", "4DWorldBench", "GameWorld Score", "RigidBench", "Morpheus", "What-If World", "RoboWM-Bench", "DreamGen Bench", "WorldLens", "PhyGround", "Physion-Eval", "CRONOS", "VACT", "STEVO-Bench", "PhysicsMind", "PDI-Bench", "HOCA-Bench", "WorldOlympiad", "ACWM-Phys"]
S3 = ["CLEVRER", "CATER", "NExT-QA", "Causal-VidQA", "CRAFT", "IntentQA", "CoPhy", "MMWorld", "CausalVQA", "VCRBench", "Physion", "Physics-IQ", "WorldPrediction", "WR-Arena", "CausalSpatial", "T2VWorldBench", "VACT", "HOCA-Bench"]
S4 = ["CLEVRER", "CRAFT", "CoPhy", "ComPhy", "ACQUIRED", "Causal-VidQA", "MMWorld", "CausalVQA", "What-If World", "WR-Arena", "CRONOS"]
S5 = ["T2V-CompBench", "TC-Bench", "StoryEval", "VideoPhy", "VideoPhy-2", "PhyGenBench", "PhyWorldBench", "OSCBench", "MoveBench", "MagicBench", "WorldScore", "4DWorldBench", "DrivingGen", "ACT-Bench", "What-If World", "Omni-WorldBench", "DreamGen Bench", "WorldModelBench", "VBench-2.0"]
S6 = ["WorldMark", "WR-Arena", "WorldSimBench", "WBench", "iWorld-Bench", "MIND", "ACWM-Phys", "RoboWM-Bench", "WorldArena 2.0", "WorldOlympiad"]
S7 = ["WorldArena", "WorldArena 2.0"]
S8 = ["WorldArena"]
S9 = ["WorldArena", "WorldArena 2.0", "World-in-World", "EVA-Bench", "WorldLens", "RoboWM-Bench", "WorldSimBench", "WR-Arena"]
S10 = ["WorldArena 2.0"]

top = {}
for target_code, names in [
    ("T1", T1),
    ("T2", T2),
    ("T3", T3),
    ("T4", T4),
    ("T5", list(dict.fromkeys(S3 + S4))),
    ("T6", list(dict.fromkeys(S5 + S6))),
    ("T7", list(dict.fromkeys(S7 + S8 + S9 + S10))),
]:
    for name in names:
        top.setdefault(name, set()).add(target_code)

all_names = set(sum([T1, T2, T3, T4, S3, S4, S5, S6, S7, S8, S9, S10], []))
missing = all_names - set(meta)
assert not missing, missing
assert len(meta) == manifest["total"] == 82
assert sum(len(targets) > 1 for targets in top.values()) == manifest["crossCategory"] == 43


def md_link(label, url):
    return f"[{label}]({url})" if url else "-"


def row(name):
    record = meta[name]
    title = title_override.get(name, record.get("title", name)).strip().rstrip(".")
    marker = " △" if len(top.get(name, set())) > 1 else ""
    article = f"[**{title}{marker}**]({record.get('paperUrl', '#')})"
    year = manifest["records"][name][1]
    venue = venue_override.get(name, record.get("venue", "-")) or "-"
    return (
        f"| {article} | {year} | {venue} | "
        f"{md_link('Code', code_links.get(name))} | "
        f"{md_link('Project Page', project_pages.get(name))} |"
    )


def table(names):
    return [
        "| Article | Year | Venue | Code | Project Page |",
        "|:--|:--:|:--:|:--:|:--:|",
        *[row(name) for name in names],
    ]


lines = [
    "# A Survey of World Model Benchmarks",
    "",
    "[![Project Page](https://img.shields.io/badge/Project-Page-5965d8)](https://axbhb.github.io/world-model-evaluation-survey/) [![Benchmarks](https://img.shields.io/badge/Benchmarks-82-2f8f63)](https://axbhb.github.io/world-model-evaluation-survey/#benchmarks)",
    "",
    "This repository accompanies **A Survey of World Model Benchmarks**. The latest manuscript covers **82 representative benchmarks** published from **2018–2026**; **43** span more than one evaluation-target category. The corpus was last checked in July 2026.",
    "",
    "The category membership below follows the latest survey taxonomy and Figure 4. Rows are intentionally repeated when a benchmark belongs to multiple evaluation targets or sub-targets. `△` marks a benchmark assigned to more than one top-level evaluation target.",
    "",
    "Each table is designed as a literature index rather than a copy of Tables 3–9: **Article**, **Year**, **Venue**, **Code**, and **Project Page**. `-` means that no verified public link is currently recorded.",
    "",
    "## Contents",
    "",
    "- [Visual and Temporal Quality](#visual-and-temporal-quality)",
    "- [Spatial and State Consistency](#spatial-and-state-consistency)",
    "- [Long-Horizon Memory and State Persistence](#long-horizon-memory-and-state-persistence)",
    "- [Physical Plausibility](#physical-plausibility)",
    "- [Causal and Counterfactual Reasoning](#causal-and-counterfactual-reasoning)",
    "- [Control Fidelity and Interactive Dynamics](#control-fidelity-and-interactive-dynamics)",
    "- [Functional Utility](#functional-utility)",
    "",
    "## Evaluation-target coverage",
    "",
    "| Evaluation target | Benchmarks |",
    "|:--|--:|",
    "| Visual & Temporal Quality | 20 |",
    "| Spatial & State Consistency | 19 |",
    "| Long-Horizon Memory & State Persistence | 11 |",
    "| Physical Plausibility | 39 |",
    "| Causal & Counterfactual Reasoning | 22 |",
    "| Control Fidelity & Interactive Dynamics | 29 |",
    "| Functional Utility | 8 |",
    "",
    "Counts overlap because cross-category benchmarks appear in more than one top-level target.",
    "",
]

sections = [
    ("Visual and Temporal Quality", None, T1),
    ("Spatial and State Consistency", None, T2),
    ("Long-Horizon Memory and State Persistence", None, T3),
    ("Physical Plausibility", None, T4),
    ("Causal and Counterfactual Reasoning", "Causal Reasoning over Observed Worlds", S3),
    (None, "Counterfactual Reasoning over Intervened Worlds", S4),
    ("Control Fidelity and Interactive Dynamics", "Pre-specified Control Fidelity", S5),
    (None, "Interactive Action Fidelity", S6),
    ("Functional Utility", "World Model as Data Engine", S7),
    (None, "World Model as Policy Evaluator", S8),
    (None, "World Model as Planner", S9),
    (None, "World Model as Interactive Training Environment", S10),
]
for h2, h3, names in sections:
    if h2:
        lines += [f"## {h2}", ""]
    if h3:
        lines += [f"### {h3}", ""]
    lines += table(names) + [""]

lines += [
    "## Machine-readable data",
    "",
    "- [`docs/assets/benchmarks.json`](docs/assets/benchmarks.json): canonical benchmark, target, sub-target, protocol, metric, data-source, year, and domain metadata",
    "- [`docs/assets/metadata.json`](docs/assets/metadata.json): taxonomy labels and release-window definitions",
    "- [Interactive project page](https://axbhb.github.io/world-model-evaluation-survey/)",
    "",
]

output = "\n".join(lines)
(ROOT / "Readme.md").write_text(output, encoding="utf-8")
print(f"Generated {len(lines)} README lines for {manifest['total']} benchmarks.")
