#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
manifest_path = ROOT / "docs/assets/benchmarks.json"
index_path = ROOT / "docs/index.html"

manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

# Figure 4 maps several causal benchmarks to both observed-world and
# intervened-world reasoning leaves, even when Table 7 lists a primary group.
overrides = {
    "CLEVRER": "S3+S4",
    "CRAFT": "S3+S4",
    "CoPhy": "S3+S4",
    "Causal-VidQA": "S3+S4",
    "MMWorld": "S3+S4",
    "CausalVQA": "S3+S4",
    "WR-Arena": "S3+S4+S6",
}
for name, codes in overrides.items():
    manifest["records"][name][7] = codes

manifest_path.write_text(
    json.dumps(manifest, ensure_ascii=False, separators=(",", ":")) + "\n",
    encoding="utf-8",
)

html = index_path.read_text(encoding="utf-8")
html = html.replace("World Model Evaluation Survey", "World Model Benchmarks Survey")
html = html.replace(
    '<span class="brand-copy"><strong>Evaluation</strong><small>Survey</small></span>',
    '<span class="brand-copy"><strong>Benchmarks</strong><small>Survey</small></span>',
)
html = html.replace(
    "A benchmark-centric view of <strong>what capability is evaluated</strong>",
    "An evaluation-centric view of <strong>what capability is evaluated</strong>",
)
html = html.replace("Unique benchmarks introduced by year", "Unique benchmarks by release window")
html = html.replace("Clear year filter", "Clear period filter")
html = html.replace('aria-label="Benchmark releases by year"', 'aria-label="Benchmark releases by period"')
html = html.replace(
    "Search and filter the 82 representative benchmarks coded in Tables 3–9 of the latest four-dimensional survey draft.",
    "Search and filter the 82 representative benchmarks coded in Figure 4 and Tables 3–9 of the latest manuscript.",
)
html = html.replace("latest four-dimensional PDF", "latest manuscript")
index_path.write_text(html, encoding="utf-8")

print("Applied final Figure 4 sub-target mappings and page copy.")
