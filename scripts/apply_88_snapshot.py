#!/usr/bin/env python3
"""Align the repository and project page with the 88-benchmark manuscript."""

from __future__ import annotations

import json
import re
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "docs" / "assets"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label} occurrence, found {count}: {old!r}")
    return text.replace(old, new, 1)


def replace_assignment(text: str, name: str, values: list[str]) -> str:
    pattern = rf"^{re.escape(name)} = \[.*\]$"
    replacement = f"{name} = {values!r}"
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.MULTILINE)
    if count != 1:
        raise RuntimeError(f"Could not replace assignment for {name}")
    return updated


def insert_mapping_entries(text: str, mapping_name: str, entries: dict[str, str]) -> str:
    missing = {key: value for key, value in entries.items() if f'    "{key}":' not in text}
    if not missing:
        return text
    anchor = f"{mapping_name} = {{\n"
    if anchor not in text:
        raise RuntimeError(f"Could not find mapping {mapping_name}")
    block = "".join(f'    {json.dumps(key)}: {json.dumps(value)},\n' for key, value in missing.items())
    return text.replace(anchor, anchor + block, 1)


manifest_path = ASSETS / "benchmarks.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

reference_numbers = {
    "VBench": 29,
    "RoboWM-Bench": 35,
    "World-in-World": 38,
    "IntPhys": 39,
    "CLEVRER": 40,
    "Physion": 41,
    "MIND": 42,
    "WorldOlympiad": 43,
    "WorldArena": 44,
    "WorldArena 2.0": 45,
    "FETV": 64,
    "VBench++": 65,
    "EvalCrafter": 66,
    "ChronoMagic-Bench": 67,
    "WorldScore": 68,
    "VMBench": 69,
    "EWMBench": 70,
    "GameWorld Score": 71,
    "WorldMark": 72,
    "4DWorldBench": 73,
    "WorldLens": 74,
    "DrivingGen": 75,
    "PEDRA": 76,
    "Gen-ViRe": 77,
    "iWorld-Bench": 78,
    "TC-Bench": 83,
    "WBench": 84,
    "PDI-Bench": 85,
    "LoopNav": 86,
    "MBench": 87,
    "STEVO-Bench": 88,
    "CausalSpatial": 89,
    "What-If World": 90,
    "HOCA-Bench": 91,
    "WorldPrediction": 94,
    "SmallWorlds": 95,
    "WR-Arena": 96,
    "HTEWorld": 97,
    "IntPhys 2": 98,
    "CoPhy": 99,
    "PHYRE": 100,
    "CRAFT": 101,
    "Physion++": 102,
    "ComPhy": 103,
    "ContPhy": 104,
    "PhyCoBench": 105,
    "VideoPhy": 106,
    "VideoPhy-2": 107,
    "PhyGenBench": 108,
    "T2VPhysBench": 109,
    "Physics-IQ": 110,
    "WorldBench": 111,
    "PhyWorldBench": 112,
    "T2VWorldBench": 113,
    "WorldModelBench": 114,
    "VBench-2.0": 115,
    "RigidBench": 116,
    "Morpheus": 117,
    "DreamGen Bench": 118,
    "PhyGround": 119,
    "Physion-Eval": 120,
    "CRONOS": 121,
    "VACT": 122,
    "PhysicsMind": 123,
    "ACWM-Phys": 124,
    "CATER": 125,
    "NExT-QA": 126,
    "Causal-VidQA": 127,
    "IntentQA": 128,
    "MMWorld": 129,
    "CausalVQA": 130,
    "VCRBench": 131,
    "ACQUIRED": 132,
    "T2V-CompBench": 133,
    "StoryEval": 134,
    "OSCBench": 135,
    "MoveBench": 136,
    "MagicBench": 137,
    "ACT-Bench": 138,
    "Omni-WorldBench": 139,
    "WorldSimBench": 140,
    "EVA-Bench": 141,
}

missing_existing = set(reference_numbers) - set(manifest["records"])
if missing_existing:
    raise RuntimeError(f"Existing manifest records are missing: {sorted(missing_existing)}")
for name, ref in reference_numbers.items():
    manifest["records"][name][0] = ref

new_metadata = {
    "WoW-World-Eval": {
        "id": "wow-world-eval",
        "shortName": "WoW-World-Eval",
        "title": "Wow, Wo, Val! A Comprehensive Embodied World Model Evaluation Turing Test",
        "venue": "arXiv",
        "paperUrl": "https://arxiv.org/abs/2601.04137",
        "arxivId": "2601.04137",
        "reference": "C.-K. Fan et al., ‘Wow, Wo, Val! A Comprehensive Embodied World Model Evaluation Turing Test,’ arXiv:2601.04137, 2026.",
    },
    "RBench": {
        "id": "rbench",
        "shortName": "RBench",
        "title": "Rethinking Video Generation Model for the Embodied World",
        "venue": "ICML",
        "paperUrl": "https://arxiv.org/abs/2601.15282",
        "arxivId": "2601.15282",
        "reference": "Y. Deng et al., ‘Rethinking Video Generation Model for the Embodied World,’ ICML, 2026.",
    },
    "PAI-Bench": {
        "id": "pai-bench",
        "shortName": "PAI-Bench",
        "title": "PAI-Bench: A Comprehensive Benchmark for Physical AI",
        "venue": "CVPR",
        "paperUrl": "https://arxiv.org/abs/2512.01989",
        "arxivId": "2512.01989",
        "reference": "F. Zhou et al., ‘PAI-Bench: A Comprehensive Benchmark for Physical AI,’ CVPR, 2026.",
    },
    "EZS-Bench": {
        "id": "ezs-bench",
        "shortName": "EZS-Bench",
        "title": "ABot-PhysWorld: Interactive World Foundation Model for Robotic Manipulation with Physics Alignment (introduces EZS-Bench)",
        "venue": "arXiv",
        "paperUrl": "https://arxiv.org/abs/2603.23376",
        "arxivId": "2603.23376",
        "reference": "Y. Chen et al., ‘ABot-PhysWorld: Interactive World Foundation Model for Robotic Manipulation with Physics Alignment,’ arXiv:2603.23376, 2026.",
    },
    "AutumnBench": {
        "id": "autumnbench",
        "shortName": "AutumnBench",
        "title": "Benchmarking World-Model Learning (introduces AutumnBench)",
        "venue": "ICML",
        "paperUrl": "https://arxiv.org/abs/2510.19788",
        "arxivId": "2510.19788",
        "reference": "A. Warrier et al., ‘Benchmarking World-Model Learning,’ arXiv:2510.19788, 2025.",
    },
    "MVP": {
        "id": "mvp",
        "shortName": "MVP",
        "title": "A Shortcut-Aware Video-QA Benchmark for Physical Understanding via Minimal Video Pairs",
        "venue": "arXiv",
        "paperUrl": "https://arxiv.org/abs/2506.09987",
        "arxivId": "2506.09987",
        "reference": "B. Krojer et al., ‘A Shortcut-Aware Video-QA Benchmark for Physical Understanding via Minimal Video Pairs,’ arXiv:2506.09987, 2025.",
    },
}
new_rows = {
    "WoW-World-Eval": [79, 2026, "embodied", "OL", "P+O", "HCP", "T1+T2+T3+T4+T5+T6+T7", "S1+S2+S3+S5+S9"],
    "RBench": [80, 2026, "embodied", "OL", "P", "RWD", "T1+T2+T3+T4+T5+T6", "S1+S2+S3+S5"],
    "PAI-Bench": [81, 2025, "video", "OL", "P", "HCP", "T1+T2+T4+T5+T6", "S1+S2+S3+S5"],
    "EZS-Bench": [82, 2026, "embodied", "OL", "P", "HCP", "T1+T2+T4+T6", "S1+S2+S5"],
    "AutumnBench": [92, 2025, "game", "CL", "P+O", "SBG", "T2+T3+T5+T7", "S4+S9"],
    "MVP": [93, 2025, "video", "OL", "P", "HCP", "T2+T4+T5", "S4"],
}
manifest.setdefault("added", {}).update(new_metadata)
manifest["records"].update(new_rows)
manifest["schemaVersion"] = 5
manifest["total"] = 88
manifest["crossCategory"] = 49

if len(manifest["records"]) != 88:
    raise RuntimeError(f"Expected 88 records, found {len(manifest['records'])}")
if sum(len(str(row[6]).split("+")) > 1 for row in manifest["records"].values()) != 49:
    raise RuntimeError("Expected 49 cross-category records")

expected_years = Counter({2018: 1, 2019: 1, 2020: 3, 2021: 2, 2022: 3, 2023: 4, 2024: 12, 2025: 32, 2026: 30})
actual_years = Counter(row[1] for row in manifest["records"].values())
if actual_years != expected_years:
    raise RuntimeError(f"Unexpected release-year distribution: {actual_years}")

expected_targets = Counter({"T1": 24, "T2": 25, "T3": 14, "T4": 44, "T5": 27, "T6": 33, "T7": 10})
actual_targets = Counter(
    code
    for row in manifest["records"].values()
    for code in str(row[6]).split("+")
    if code
)
if actual_targets != expected_targets:
    raise RuntimeError(f"Unexpected target coverage: {actual_targets}")

manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")

metadata_path = ASSETS / "metadata.json"
metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
metadata["total"] = 88
metadata["crossCategory"] = 49
metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# Update the reader-facing literature-index generator while preserving its layout.
generator_path = ROOT / "scripts" / "generate_readme_index.py"
generator = generator_path.read_text(encoding="utf-8")

generator = generator.replace("Benchmarks-82-2f8f63", "Benchmarks-88-2f8f63")
generator = generator.replace("**82 representative benchmarks**", "**88 representative benchmarks**")
generator = generator.replace("; **43** span more than one", "; **49** span more than one")
generator = generator.replace('"| Visual & Temporal Quality | 20 |",', '"| Visual & Temporal Quality | 24 |",')
generator = generator.replace('"| Spatial & State Consistency | 19 |",', '"| Spatial & State Consistency | 25 |",')
generator = generator.replace('"| Long-Horizon Memory & State Persistence | 11 |",', '"| Long-Horizon Memory & State Persistence | 14 |",')
generator = generator.replace('"| Physical Plausibility | 39 |",', '"| Physical Plausibility | 44 |",')
generator = generator.replace('"| Causal & Counterfactual Reasoning | 22 |",', '"| Causal & Counterfactual Reasoning | 27 |",')
generator = generator.replace('"| Control Fidelity & Interactive Dynamics | 29 |",', '"| Control Fidelity & Interactive Dynamics | 33 |",')
generator = generator.replace('"| Functional Utility | 8 |",', '"| Functional Utility | 10 |",')
generator = generator.replace('assert len(meta) == manifest["total"] == 82', 'assert len(meta) == manifest["total"] == 88')
generator = generator.replace('assert sum(len(targets) > 1 for targets in top.values()) == manifest["crossCategory"] == 43', 'assert sum(len(targets) > 1 for targets in top.values()) == manifest["crossCategory"] == 49')

generator = insert_mapping_entries(generator, "code_links", {
    "RBench": "https://github.com/DAGroup-PKU/ReVidgen",
    "PAI-Bench": "https://github.com/SHI-Labs/physical-ai-bench",
    "EZS-Bench": "https://github.com/amap-cvlab/ABot-PhysWorld",
    "MVP": "https://github.com/facebookresearch/minimal_video_pairs",
})
generator = insert_mapping_entries(generator, "project_pages", {
    "RBench": "https://dagroup-pku.github.io/ReVidgen.github.io/",
    "MVP": "https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/",
})

T1 = ["FETV", "VBench", "VBench++", "EvalCrafter", "ChronoMagic-Bench", "WorldScore", "VMBench", "EWMBench", "WorldArena", "GameWorld Score", "WorldMark", "4DWorldBench", "TC-Bench", "WorldLens", "WorldArena 2.0", "DrivingGen", "WBench", "PEDRA", "Gen-ViRe", "iWorld-Bench", "WoW-World-Eval", "RBench", "PAI-Bench", "EZS-Bench"]
T2 = ["VBench", "VBench++", "WorldMark", "GameWorld Score", "EWMBench", "WorldArena", "WorldLens", "DrivingGen", "WorldScore", "4DWorldBench", "PDI-Bench", "LoopNav", "MIND", "MBench", "STEVO-Bench", "CausalSpatial", "What-If World", "WorldOlympiad", "HOCA-Bench", "WoW-World-Eval", "RBench", "AutumnBench", "MVP", "PAI-Bench", "EZS-Bench"]
T3 = ["WorldPrediction", "SmallWorlds", "WR-Arena", "WorldMark", "MBench", "MIND", "WBench", "WorldOlympiad", "HTEWorld", "RoboWM-Bench", "iWorld-Bench", "WoW-World-Eval", "RBench", "AutumnBench"]
T4 = ["IntPhys", "IntPhys 2", "CLEVRER", "CoPhy", "PHYRE", "CRAFT", "Physion", "Physion++", "ComPhy", "ContPhy", "PhyCoBench", "VideoPhy", "VideoPhy-2", "PhyGenBench", "T2VPhysBench", "Physics-IQ", "WorldBench", "PhyWorldBench", "T2VWorldBench", "WorldModelBench", "VBench-2.0", "4DWorldBench", "GameWorld Score", "RigidBench", "Morpheus", "What-If World", "RoboWM-Bench", "DreamGen Bench", "WorldLens", "PhyGround", "Physion-Eval", "CRONOS", "VACT", "STEVO-Bench", "PhysicsMind", "PDI-Bench", "HOCA-Bench", "WorldOlympiad", "ACWM-Phys", "WoW-World-Eval", "RBench", "MVP", "PAI-Bench", "EZS-Bench"]
S3 = ["CLEVRER", "CATER", "NExT-QA", "Causal-VidQA", "CRAFT", "IntentQA", "CoPhy", "MMWorld", "CausalVQA", "VCRBench", "Physion", "Physics-IQ", "WorldPrediction", "WR-Arena", "CausalSpatial", "T2VWorldBench", "VACT", "HOCA-Bench", "WoW-World-Eval", "RBench", "PAI-Bench"]
S4 = ["CLEVRER", "CRAFT", "CoPhy", "ComPhy", "ACQUIRED", "Causal-VidQA", "MMWorld", "CausalVQA", "What-If World", "WR-Arena", "CRONOS", "AutumnBench", "MVP"]
S5 = ["T2V-CompBench", "TC-Bench", "StoryEval", "VideoPhy", "VideoPhy-2", "PhyGenBench", "PhyWorldBench", "OSCBench", "MoveBench", "MagicBench", "WorldScore", "4DWorldBench", "DrivingGen", "ACT-Bench", "What-If World", "Omni-WorldBench", "DreamGen Bench", "WorldModelBench", "VBench-2.0", "WoW-World-Eval", "RBench", "PAI-Bench", "EZS-Bench"]
S9 = ["WorldArena", "WorldArena 2.0", "World-in-World", "EVA-Bench", "WorldLens", "RoboWM-Bench", "WorldSimBench", "WR-Arena", "WoW-World-Eval", "AutumnBench"]
for name, values in (("T1", T1), ("T2", T2), ("T3", T3), ("T4", T4), ("S3", S3), ("S4", S4), ("S5", S5), ("S9", S9)):
    generator = replace_assignment(generator, name, values)

generator_path.write_text(generator, encoding="utf-8")
subprocess.run(["python", str(generator_path)], cwd=ROOT, check=True)

# Update static project-page copy and cache-busting query strings.
index_path = ROOT / "docs" / "index.html"
index = index_path.read_text(encoding="utf-8")
replacements = {
    "Explore 82 world-model benchmarks": "Explore 88 world-model benchmarks",
    "Latest manuscript snapshot · 82 benchmarks · 43 cross-category": "Latest manuscript snapshot · 88 benchmarks · 49 cross-category",
    '<strong id="stat-total">82</strong>': '<strong id="stat-total">88</strong>',
    '<strong id="stat-cross">43</strong>': '<strong id="stat-cross">49</strong>',
    '<strong>3</strong><span>protocol / metric families</span>': '<strong>2 / 2</strong><span>protocol classes / metric levels</span>',
    "OL · CR · CL": "OL · CL",
    "automatic · judge · outcome": "prediction-level · downstream",
    "Distinguishes open-loop prediction, controlled rollout, and closed-loop interaction.": "Distinguishes open-loop evaluation from feedback-driven closed-loop interaction.",
    "Distinguishes automatic, judge-based, and outcome-grounded metric families.": "Separates prediction-level evidence from downstream outcome evidence.",
    "<strong>29 new in 2025 (2.4× 2024)</strong>; target coverage includes 5 spatial, 14 physical, and 10 control.": "<strong>32 new in 2025 (2.7× 2024)</strong>; target coverage includes 8 spatial, 16 physical, and 11 control.",
    "2026 contributes <strong>9/11 long-horizon</strong> and <strong>4/7 utility</strong> benchmarks.": "2026 contributes <strong>11/14 long-horizon</strong> and <strong>6/10 utility</strong> benchmarks.",
    "Search and filter the 82 representative benchmarks": "Search and filter the 88 representative benchmarks",
    '<strong id="result-count">82</strong>': '<strong id="result-count">88</strong>',
    "assets/app-v3.js?v=5": "assets/app-v3.js?v=6",
}
for old, new in replacements.items():
    if old not in index:
        raise RuntimeError(f"Could not update index.html: {old}")
    index = index.replace(old, new)
index_path.write_text(index, encoding="utf-8")

wrapper_path = ASSETS / "app-v3.js"
wrapper = wrapper_path.read_text(encoding="utf-8")
wrapper = replace_once(
    wrapper,
    '2026 contributes <strong>9/11 long-horizon</strong> and <strong>5/8 utility</strong> benchmarks.',
    '2026 contributes <strong>11/14 long-horizon</strong> and <strong>6/10 utility</strong> benchmarks.',
    "timeline phase-four copy",
)
wrapper = replace_once(wrapper, "app-v3-core.js?v=7", "app-v3-core.js?v=8", "explorer core cache key")
wrapper_path.write_text(wrapper, encoding="utf-8")

social_path = ASSETS / "social-preview.svg"
social = social_path.read_text(encoding="utf-8")
social = replace_once(social, '>82</text>', '>88</text>', "social preview benchmark count")
social_path.write_text(social, encoding="utf-8")

validation_path = ROOT / "scripts" / "sync_latest_survey.py"
validation = validation_path.read_text(encoding="utf-8")
validation = validation.replace('manifest["schemaVersion"] == 4', 'manifest["schemaVersion"] == 5')
validation = validation.replace('manifest["total"] == 82', 'manifest["total"] == 88')
validation = validation.replace('manifest["crossCategory"] == 43', 'manifest["crossCategory"] == 49')
validation = validation.replace('len(records) == 82', 'len(records) == 88')
validation = validation.replace('2023: 4, 2024: 12, 2025: 29, 2026: 27,', '2023: 4, 2024: 12, 2025: 32, 2026: 30,')
validation = validation.replace('"T1": 20, "T2": 19, "T3": 11, "T4": 39,\n    "T5": 22, "T6": 29, "T7": 8,', '"T1": 24, "T2": 25, "T3": 14, "T4": 44,\n    "T5": 27, "T6": 33, "T7": 10,')
validation = validation.replace('== 43\n', '== 49\n', 1)
validation = validation.replace('assert "| Functional Utility | 8 |" in readme', 'assert "| Functional Utility | 10 |" in readme')
validation = validation.replace('assert "5/8 utility" in wrapper', 'assert "6/10 utility" in wrapper')
validation = validation.replace('82 benchmarks, 43 cross-category', '88 benchmarks, 49 cross-category')
anchor = 'assert records["CausalVQA"][7] == "S3+S4"\n'
new_assertions = '''assert records["CausalVQA"][7] == "S3+S4"\nassert records["WoW-World-Eval"] == [79, 2026, "embodied", "OL", "P+O", "HCP", "T1+T2+T3+T4+T5+T6+T7", "S1+S2+S3+S5+S9"]\nassert records["RBench"][6] == "T1+T2+T3+T4+T5+T6"\nassert records["PAI-Bench"][1:6] == [2025, "video", "OL", "P", "HCP"]\nassert records["EZS-Bench"][7] == "S1+S2+S5"\nassert records["AutumnBench"][3:6] == ["CL", "P+O", "SBG"]\nassert records["MVP"][6:8] == ["T2+T4+T5", "S4"]\n'''
validation = replace_once(validation, anchor, new_assertions, "new benchmark validation block")
validation = validation.replace('assert "World reasoning arena" in readme', 'assert "World reasoning arena" in readme\nassert "WoW-World-Eval" in readme\nassert "RBench" in readme\nassert "PAI-Bench" in readme\nassert "EZS-Bench" in readme\nassert "AutumnBench" in readme\nassert "MVP" in readme')
validation_path.write_text(validation, encoding="utf-8")

print("Aligned repository data, README, validation, and project page with the 88-benchmark manuscript.")
