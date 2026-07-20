#!/usr/bin/env python3
"""Validate the repository snapshot against the latest July 2026 manuscript."""

from collections import Counter
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "docs/assets/benchmarks.json").read_text(encoding="utf-8"))
metadata = json.loads((ROOT / "docs/assets/metadata.json").read_text(encoding="utf-8"))
readme = (ROOT / "Readme.md").read_text(encoding="utf-8")
wrapper = (ROOT / "docs/assets/app-v3.js").read_text(encoding="utf-8")
css = (ROOT / "docs/assets/latest-schema.css").read_text(encoding="utf-8")
records = manifest["records"]

assert manifest["title"] == "A Survey of World Model Benchmarks"
assert manifest["version"] == "July 2026 manuscript snapshot"
assert manifest["framework"] == "Target–Protocol–Metrics–Data"
assert manifest["schemaVersion"] == 5
assert manifest["total"] == 88
assert manifest["crossCategory"] == 49
assert len(records) == 88
assert manifest["protocolLabels"] == {
    "OL": "Open-Loop Evaluation",
    "CL": "Closed-Loop Interaction",
}
assert manifest["metricLabels"] == {
    "P": "Prediction-Level Metrics",
    "O": "Downstream Outcome Metrics",
}

protocol_codes = {
    code for row in records.values() for code in str(row[3]).split("+") if code
}
metric_codes = {
    code for row in records.values() for code in str(row[4]).split("+") if code
}
data_codes = {
    code for row in records.values() for code in str(row[5]).split("+") if code
}
assert protocol_codes <= {"OL", "CL"}
assert metric_codes <= {"P", "O"}
assert data_codes <= {"RWD", "SBG", "SPTC", "HCP"}

assert Counter(row[1] for row in records.values()) == Counter({
    2018: 1, 2019: 1, 2020: 3, 2021: 2, 2022: 3,
    2023: 4, 2024: 12, 2025: 32, 2026: 30,
})
target_counts = Counter(
    code for row in records.values() for code in str(row[6]).split("+") if code
)
assert target_counts == Counter({
    "T1": 24, "T2": 25, "T3": 14, "T4": 44,
    "T5": 27, "T6": 33, "T7": 10,
})
assert sum(len(str(row[6]).split("+")) > 1 for row in records.values()) == 49

# High-leverage checks for the six additions in the latest manuscript.
assert records["WoW-World-Eval"] == [
    79, 2026, "embodied", "OL", "P+O", "HCP",
    "T1+T2+T3+T4+T5+T6+T7", "S1+S2+S3+S5+S9",
]
assert records["RBench"] == [
    80, 2026, "embodied", "OL", "P", "RWD",
    "T1+T2+T3+T4+T5+T6", "S1+S2+S3+S5",
]
assert records["PAI-Bench"] == [
    81, 2025, "video", "OL", "P", "HCP",
    "T1+T2+T4+T5+T6", "S1+S2+S3+S5",
]
assert records["EZS-Bench"] == [
    82, 2026, "embodied", "OL", "P", "HCP",
    "T1+T2+T4+T6", "S1+S2+S5",
]
assert records["AutumnBench"] == [
    92, 2025, "game", "CL", "P+O", "SBG",
    "T2+T3+T5+T7", "S4+S9",
]
assert records["MVP"] == [
    93, 2025, "video", "OL", "P", "HCP",
    "T2+T4+T5", "S4",
]

# Existing regression checks retained from the prior snapshot.
assert records["PEDRA"] == [76, 2025, "video", "OL", "P", "RWD", "T1", "S1+S2"]
assert manifest["aliases"]["Pedestrian sim."] == "PEDRA"
assert records["WorldMark"][5] == "HCP"
assert records["WR-Arena"][5] == "HCP"
assert records["WR-Arena"][6] == "T3+T5+T6+T7"
assert records["WR-Arena"][7] == "S3+S4+S6+S9"
assert records["WorldArena"][3:5] == ["OL+CL", "P+O"]
assert records["WorldArena 2.0"][3:5] == ["OL+CL", "P+O"]
assert records["WorldLens"][3:5] == ["OL+CL", "P+O"]
assert records["WorldSimBench"][3:5] == ["OL+CL", "P+O"]
assert records["PHYRE"][3:5] == ["CL", "O"]
assert records["RoboWM-Bench"][3:5] == ["OL", "O"]
assert records["CLEVRER"][7] == "S3+S4"
assert records["CausalVQA"][7] == "S3+S4"

for key in (
    "title", "version", "framework", "total", "crossCategory",
    "protocolLabels", "metricLabels", "dataLabels", "timelineBins",
):
    assert metadata[key] == manifest[key]

# README remains a reader-facing literature index rather than a copy of Tables 3–9.
assert readme.count("| Article | Year | Venue | Code | Project Page |") == 12
assert "| Benchmark | Year | Domain | Protocol | Metrics | Data |" not in readme
for heading in (
    "## Visual and Temporal Quality",
    "## Spatial and State Consistency",
    "## Long-Horizon Memory and State Persistence",
    "## Physical Plausibility",
    "## Causal and Counterfactual Reasoning",
    "## Control Fidelity and Interactive Dynamics",
    "## Functional Utility",
    "### Causal Reasoning over Observed Worlds",
    "### Counterfactual Reasoning over Intervened Worlds",
    "### Pre-specified Control Fidelity",
    "### Interactive Action Fidelity",
    "### World Model as Data Engine",
    "### World Model as Policy Evaluator",
    "### World Model as Planner",
    "### World Model as Interactive Training Environment",
):
    assert heading in readme
assert "| Functional Utility | 10 |" in readme
for benchmark in (
    "WoW-World-Eval", "RBench", "PAI-Bench",
    "EZS-Bench", "AutumnBench", "MVP",
):
    assert benchmark in readme

assert 'const PROTOCOLS = ["OL", "CL"];' in wrapper
assert 'const METRICS = ["P", "O"];' in wrapper
assert "Open-Loop Evaluation" in wrapper
assert "Prediction-Level Metrics" in wrapper
assert "6/10 utility" in wrapper
assert "latest-schema.css" in wrapper
assert "repeat(2" in css

print(
    "Validated the latest survey snapshot: 88 benchmarks, 49 cross-category, "
    "7 targets, 2 protocols, 2 metric levels, and 4 data sources."
)
