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
assert manifest["schemaVersion"] == 4
assert manifest["total"] == 82
assert manifest["crossCategory"] == 43
assert len(records) == 82
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
assert "CR" not in protocol_codes
assert not ({"A", "J"} & metric_codes)

assert Counter(row[1] for row in records.values()) == Counter({
    2018: 1, 2019: 1, 2020: 3, 2021: 2, 2022: 3,
    2023: 4, 2024: 12, 2025: 29, 2026: 27,
})
target_counts = Counter(
    code for row in records.values() for code in str(row[6]).split("+") if code
)
assert target_counts == Counter({
    "T1": 20, "T2": 19, "T3": 11, "T4": 39,
    "T5": 22, "T6": 29, "T7": 8,
})
assert sum(len(str(row[6]).split("+")) > 1 for row in records.values()) == 43

# High-leverage regression checks from the revised manuscript.
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

assert "`OL` Open-Loop Evaluation; `CL` Closed-Loop Interaction" in readme
assert "`P` Prediction-Level Metrics; `O` Downstream Outcome Metrics" in readme
assert "Functional Utility (`T7`) | 8" in readme
assert "**PEDRA**" in readme
assert "**WR-Arena △**" in readme
assert "Controlled Rollout" not in readme
assert "Automatic / Judge-Based / Outcome-Grounded" not in readme

assert 'const PROTOCOLS = ["OL", "CL"];' in wrapper
assert 'const METRICS = ["P", "O"];' in wrapper
assert "Open-Loop Evaluation" in wrapper
assert "Prediction-Level Metrics" in wrapper
assert "5/8 utility" in wrapper
assert "latest-schema.css" in wrapper
assert "repeat(2" in css

print(
    "Validated latest manuscript snapshot: 82 benchmarks, 43 cross-category, "
    "7 targets, 2 protocols, 2 metric levels, and 4 data sources."
)
