#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
from collections import defaultdict, Counter
import glob, json, re

ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/'docs'; ASSETS=DOCS/'assets'
TITLE='A Survey of World Model Benchmarks'; TOTAL=82; CROSS=43
ROWS='''VBench|9|2024|video|OL|A|SPTC
RoboWM-Bench|11|2026|embodied|CL|A+O|HCP
World-in-World|12|2025|embodied|CL|A+J+O|HCP
IntPhys|13|2018|video|OL|A|SBG
CLEVRER|14|2020|video|OL|A|SBG
Physion|15|2021|video|OL|A|SBG
MIND|16|2026|video|OL+CL|A|SBG
WorldOlympiad|17|2026|video|OL+CR|A+J|HCP
WorldArena|18|2026|embodied|OL+CL|A+J+O|SBG
WorldArena 2.0|19|2026|embodied|OL+CL|A+J+O|HCP
FETV|25|2023|video|OL|A+J|SPTC
VBench++|26|2024|video|OL|A|SPTC
EvalCrafter|27|2024|video|OL|A+J|SPTC
ChronoMagic-Bench|28|2024|video|OL|A+J|SPTC
WorldScore|29|2025|video|CR|A+J|HCP
VMBench|30|2025|video|OL|A|SPTC
EWMBench|31|2025|embodied|CR|A+J|HCP
GameWorld Score|32|2025|game|CL|A+J|SBG
WorldMark|33|2026|game+video|OL+CL|A+J|SBG
4DWorldBench|34|2025|video|CR|A+J|HCP
WorldLens|35|2026|driving|OL+CL|A+J+O|HCP
DrivingGen|36|2026|driving|CR|A+J|RWD
Pedestrian sim.|37|2025|video|OL|A|RWD
Gen-ViRe|38|2025|video|OL|J|HCP
iWorld-Bench|39|2026|video|CR|A|HCP
TC-Bench|40|2024|video|CR|A+J|HCP
WBench|41|2026|video|CL|A+J|HCP
PDI-Bench|42|2026|video|OL|A|HCP
LoopNav|43|2025|game|CR|A|SBG
MBench|44|2026|video|OL|A+J|RWD
STEVO-Bench|45|2026|video|CR|J|HCP
CausalSpatial|46|2026|image|CR|A|SBG
What-If World|47|2026|driving+embodied|CR|J|RWD
HOCA-Bench|48|2026|video|OL|J|HCP
WorldPrediction|49|2025|video|OL|A|RWD
SmallWorlds|50|2025|video|OL|A|SBG
WR-Arena|51|2026|driving+embodied|CR+CL|A+J+O|RWD
HTEWorld|52|2026|embodied|CR|A|SBG
IntPhys 2|53|2025|video|OL|A|SBG
CoPhy|54|2020|video|CR|A|SBG
PHYRE|55|2019|video|CL|A+O|SBG
CRAFT|56|2022|video|CR|A|SBG
Physion++|57|2023|video|OL|A|SBG
ComPhy|58|2022|video|CR|A|SBG
ContPhy|59|2024|video|OL|A|SBG
PhyCoBench|60|2025|video|OL|A+J|SPTC
VideoPhy|61|2024|video|CR|J|SPTC
VideoPhy-2|62|2025|video|CR|J|SPTC
PhyGenBench|63|2024|video|CR|J|SPTC
T2VPhysBench|64|2025|video|CR|J|SPTC
Physics-IQ|65|2025|video|OL|A+J|RWD
WorldBench|66|2026|video|OL|A|HCP
PhyWorldBench|67|2025|video|CR|J|SPTC
T2VWorldBench|68|2025|video|OL|J|SPTC
WorldModelBench|69|2025|video|OL|J|SPTC
VBench-2.0|70|2025|video|OL|A+J|SPTC
RigidBench|71|2026|video|OL|A|SBG
Morpheus|72|2025|video|OL|A|RWD
DreamGen Bench|73|2025|embodied|OL|J|HCP
PhyGround|74|2026|video|OL|J|SPTC
Physion-Eval|75|2026|video|OL|J|HCP
CRONOS|76|2026|video|CR|A+J|HCP
VACT|77|2025|video|CR|A+J|SPTC
PhysicsMind|78|2026|video|OL|A|HCP
ACWM-Phys|79|2026|video|CR|A|SBG
CATER|80|2020|video|OL|A|SBG
NExT-QA|81|2021|video|OL|A|RWD
Causal-VidQA|82|2022|video|CR|A|RWD
IntentQA|83|2023|video|OL|A|RWD
MMWorld|84|2025|video|CR|A+J|HCP
CausalVQA|85|2025|video|CR|A|RWD
VCRBench|86|2025|video|OL|A|RWD
ACQUIRED|87|2023|video|CR|A|RWD
T2V-CompBench|88|2025|video|CR|A+J|SPTC
StoryEval|89|2024|video|CR|J|SPTC
OSCBench|90|2026|video|CR|J|SPTC
MoveBench|91|2025|video|CR|A+J|RWD
MagicBench|92|2025|video|CR|A|RWD
ACT-Bench|93|2024|driving|CR|A|RWD
Omni-WorldBench|94|2026|video|CR|A+J|HCP
WorldSimBench|95|2024|game+driving+embodied|OL+CL|A+J+O|HCP
EVA-Bench|96|2024|embodied|OL|A+J|HCP'''
TARGETS={
'T1':('Visual & Temporal Quality','FETV;VBench;VBench++;EvalCrafter;ChronoMagic-Bench;WorldScore;VMBench;EWMBench;WorldArena;GameWorld Score;WorldMark;4DWorldBench;TC-Bench;WorldLens;WorldArena 2.0;DrivingGen;WBench;Pedestrian sim.;Gen-ViRe;iWorld-Bench'),
'T2':('Spatial & State Consistency','VBench;VBench++;WorldMark;WorldLens;WorldArena;WorldScore;DrivingGen;EWMBench;What-If World;4DWorldBench;GameWorld Score;LoopNav;MIND;MBench;STEVO-Bench;CausalSpatial;PDI-Bench;WorldOlympiad;HOCA-Bench'),
'T3':('Long-Horizon Memory & State Persistence','WorldPrediction;SmallWorlds;WR-Arena;WorldMark;MBench;MIND;WBench;WorldOlympiad;HTEWorld;RoboWM-Bench;iWorld-Bench'),
'T4':('Physical Plausibility','IntPhys;IntPhys 2;CLEVRER;CoPhy;PHYRE;CRAFT;Physion;Physion++;ComPhy;ContPhy;PhyCoBench;VideoPhy;VideoPhy-2;PhyGenBench;T2VPhysBench;Physics-IQ;WorldBench;PhyWorldBench;WorldOlympiad;ACWM-Phys;WorldModelBench;VBench-2.0;GameWorld Score;T2VWorldBench;4DWorldBench;RoboWM-Bench;DreamGen Bench;WorldLens;RigidBench;Morpheus;What-If World;PhyGround;Physion-Eval;CRONOS;VACT;STEVO-Bench;PhysicsMind;PDI-Bench;HOCA-Bench'),
'T5':('Causal & Counterfactual Reasoning','CLEVRER;CATER;NExT-QA;Causal-VidQA;CRAFT;IntentQA;MMWorld;VCRBench;Physion;Physics-IQ;WorldPrediction;WR-Arena;CausalSpatial;T2VWorldBench;VACT;HOCA-Bench;CoPhy;ComPhy;ACQUIRED;CausalVQA;What-If World;CRONOS'),
'T6':('Control Fidelity & Interactive Dynamics','T2V-CompBench;TC-Bench;StoryEval;VideoPhy;VideoPhy-2;PhyGenBench;PhyWorldBench;OSCBench;MoveBench;MagicBench;WorldScore;4DWorldBench;DrivingGen;ACT-Bench;What-If World;Omni-WorldBench;DreamGen Bench;WorldModelBench;VBench-2.0;WorldMark;WR-Arena;WorldSimBench;WBench;iWorld-Bench;MIND;ACWM-Phys;RoboWM-Bench;WorldArena 2.0;WorldOlympiad'),
'T7':('Functional Utility','WorldArena;WorldArena 2.0;World-in-World;EVA-Bench;WorldLens;RoboWM-Bench;WorldSimBench')}
SUBS={
'S1':('Visual Quality','FETV;VBench;VBench++;EvalCrafter;ChronoMagic-Bench;WorldScore;VMBench;EWMBench;WorldArena;GameWorld Score;WorldMark;4DWorldBench;WorldLens;DrivingGen;Pedestrian sim.;Gen-ViRe;iWorld-Bench'),
'S2':('Temporal Quality','VBench;VBench++;EvalCrafter;ChronoMagic-Bench;VMBench;TC-Bench;WorldScore;4DWorldBench;GameWorld Score;WorldMark;WBench;EWMBench;WorldArena;WorldArena 2.0;WorldLens;DrivingGen;Pedestrian sim.;Gen-ViRe'),
'S3':('Causal Reasoning over Observed Worlds','CLEVRER;CATER;NExT-QA;Causal-VidQA;CRAFT;IntentQA;MMWorld;VCRBench;Physion;Physics-IQ;WorldPrediction;WR-Arena;CausalSpatial;T2VWorldBench;VACT;HOCA-Bench'),
'S4':('Counterfactual Reasoning over Intervened Worlds','CoPhy;ComPhy;ACQUIRED;CausalVQA;What-If World;CRONOS'),
'S5':('Pre-specified Control Fidelity','T2V-CompBench;TC-Bench;StoryEval;VideoPhy;VideoPhy-2;PhyGenBench;PhyWorldBench;OSCBench;MoveBench;MagicBench;WorldScore;4DWorldBench;DrivingGen;ACT-Bench;What-If World;Omni-WorldBench;DreamGen Bench;WorldModelBench;VBench-2.0'),
'S6':('Interactive Action Fidelity','WorldMark;WR-Arena;WorldSimBench;WBench;iWorld-Bench;MIND;ACWM-Phys;RoboWM-Bench;WorldArena 2.0;WorldOlympiad'),
'S7':('Data Engine','WorldArena;WorldArena 2.0'),'S8':('Policy Evaluator','WorldArena'),
'S9':('Planner','WorldArena;WorldArena 2.0;World-in-World;EVA-Bench;WorldLens;RoboWM-Bench;WorldSimBench'),
'S10':('Interactive Training Environment','WorldArena 2.0')}
SECTIONS=[
('Visual and Temporal Quality',[('Visual and Temporal Quality',TARGETS['T1'][1])]),('Spatial and State Consistency',[('Spatial and State Consistency',TARGETS['T2'][1])]),('Long-Horizon Memory and State Persistence',[('Long-Horizon Memory and State Persistence',TARGETS['T3'][1])]),('Physical Plausibility',[('Physical Plausibility',TARGETS['T4'][1])]),
('Causal and Counterfactual Reasoning',[('Causal Reasoning over Observed Worlds',SUBS['S3'][1]),('Counterfactual Reasoning over Intervened Worlds',SUBS['S4'][1])]),
('Control Fidelity and Interactive Dynamics',[('Pre-specified Control Fidelity',SUBS['S5'][1]),('Interactive Action Fidelity',SUBS['S6'][1])]),
('Functional Utility',[('Data Engine',SUBS['S7'][1]),('Policy Evaluator',SUBS['S8'][1]),('Planner',SUBS['S9'][1]),('Interactive Training Environment',SUBS['S10'][1])])]

def parse_rows():
 out={}
 for line in ROWS.splitlines():
  n,ref,y,d,p,m,data=line.split('|'); out[n]=[int(ref),int(y),d,p,m,data]
 return out

def build_manifest():
 rows=parse_rows(); target_by=defaultdict(list); sub_by=defaultdict(list)
 for code,(label,names) in TARGETS.items():
  for n in names.split(';'): target_by[n].append(code)
 for code,(label,names) in SUBS.items():
  for n in names.split(';'): sub_by[n].append(code)
 records={n:[*vals,'+'.join(target_by[n]),'+'.join(sub_by[n])] for n,vals in rows.items()}
 manifest={'title':TITLE,'version':'July 2026 manuscript snapshot','framework':'Target–Protocol–Metrics–Data','schemaVersion':3,'total':82,'crossCategory':43,
 'protocolLabels':{'OL':'Open-Loop Prediction','CR':'Controlled Rollout','CL':'Closed-Loop Interaction'},'metricLabels':{'A':'Automatic Metrics','J':'Judge-Based Metrics','O':'Outcome-Grounded Metrics'},'dataLabels':{'RWD':'Real-World Data Collection','SBG':'Simulation-Based Generation','SPTC':'Scenario, Prompt, and Task Curation','HCP':'Hybrid Construction Pipelines'},
 'timelineBins':[{'label':'2018–2021','years':[2018,2019,2020,2021]},{'label':'2022–2023','years':[2022,2023]},{'label':'2024','years':[2024]},{'label':'2025','years':[2025]},{'label':'2026','years':[2026]}],
 'targetLabels':{k:v[0] for k,v in TARGETS.items()},'subtargetLabels':{k:v[0] for k,v in SUBS.items()},'aliases':{},'removed':['VideoScore','Scalable Policy Eval','stable-worldmodel'],
 'added':{'CausalSpatial':{'id':'causalspatial','shortName':'CausalSpatial','title':'CausalSpatial: A Benchmark for Object-Centric Causal Spatial Reasoning','venue':'arXiv','paperUrl':'https://arxiv.org/abs/2601.13304','arxivId':'2601.13304','reference':'CausalSpatial: A Benchmark for Object-Centric Causal Spatial Reasoning, arXiv:2601.13304, 2026.'}},'records':records,
 'supportingResources':[{'name':'VideoScore','url':'https://arxiv.org/abs/2406.15252'},{'name':'Scalable Policy Evaluation','url':'https://arxiv.org/abs/2511.11520'},{'name':'stable-worldmodel','url':'https://arxiv.org/abs/2605.21800'}]}
 assert len(records)==82 and sum(len(target_by[n])>1 for n in records)==43
 years=Counter(v[1] for v in records.values()); assert years==Counter({2025:29,2026:27,2024:12,2023:4,2020:3,2022:3,2021:2,2018:1,2019:1})
 return manifest,target_by

def old_records():
 records=[]
 for p in sorted(glob.glob(str(ASSETS/'benchmarks-[1-4].json'))): records+=json.loads(Path(p).read_text())
 return {r['shortName']:r for r in records}

def generate_readme(manifest,target_by):
 old=old_records(); old['CausalSpatial']=manifest['added']['CausalSpatial']; rows=parse_rows(); lines=[f'# {TITLE}','',f'[![Project Page](https://img.shields.io/badge/Project-Page-5965d8)](https://axbhb.github.io/world-model-evaluation-survey/) [![Benchmarks](https://img.shields.io/badge/Benchmarks-82-2f8f63)](https://axbhb.github.io/world-model-evaluation-survey/#benchmarks)','',f'This repository accompanies **{TITLE}**. The latest manuscript contains **82 representative benchmarks** from **2018–2026**; **43** span multiple evaluation-target categories.','', 'The project page follows the paper’s four-dimensional taxonomy: **Evaluation Target × Evaluation Protocol × Evaluation Metrics × Evaluation Data**.','', 'Rows are intentionally repeated across target tables. `△` marks a cross-category benchmark. The corpus was last checked in July 2026.','', '## Contents']
 for sec,_ in SECTIONS: lines.append(f"- [{sec}](#{re.sub('[^a-z0-9 -]','',sec.lower()).replace(' ','-')})")
 lines += ['', '## Column conventions','', '| Dimension | Codes | Meaning |','|:--|:--|:--|','| Protocol | `OL` / `CR` / `CL` | Open-Loop Prediction / Controlled Rollout / Closed-Loop Interaction |','| Metrics | `A` / `J` / `O` | Automatic / Judge-Based / Outcome-Grounded Metrics |','| Data | `RWD` / `SBG` / `SPTC` / `HCP` | Real-World Data Collection / Simulation-Based Generation / Scenario, Prompt, and Task Curation / Hybrid Construction Pipelines |']
 for sec,groups in SECTIONS:
  lines += ['',f'## {sec}','', '_Aligned with Figure 4 and Tables 3–9 of the latest manuscript._']
  multi=len(groups)>1 or sec=='Functional Utility'
  for group,names in groups:
   if multi: lines += ['',f'### {group}']
   lines += ['', '| Benchmark | Year | Domain | Protocol | Metrics | Data |','|:--|:--:|:--:|:--:|:--:|:--:|']
   for n in names.split(';'):
    ref,y,d,p,m,data=rows[n]; r=old[n]; tri=' △' if len(target_by[n])>1 else ''
    lines.append(f"| [**{n}{tri}**]({r.get('paperUrl','#')}) | {y} | {d} | {p} | {m} | {data} |")
 lines += ['', '## Machine-readable data','', '- [`docs/assets/benchmarks.json`](docs/assets/benchmarks.json): compact canonical manifest used by the explorer','- [Interactive project page](https://axbhb.github.io/world-model-evaluation-survey/)','']
 (ROOT/'Readme.md').write_text('\n'.join(lines),encoding='utf-8')

def patch_index():
 p=DOCS/'index.html'; s=p.read_text(encoding='utf-8')
 s=s.replace('A Survey of Benchmarks for World Model Evaluation',TITLE).replace('World Model Evaluation · 2018–2026','World Model Benchmarks · 2018–2026')
 s=s.replace('Explore 84 world-model benchmarks','Explore 82 world-model benchmarks').replace('84 representative benchmarks','82 representative benchmarks').replace('the 84 representative benchmarks','the 82 representative benchmarks')
 s=s.replace('<h1 id="hero-title">A Survey of Benchmarks for<br><span>World Model Evaluation</span></h1>','<h1 id="hero-title">A Survey of<br><span>World Model Benchmarks</span></h1>')
 s=re.sub(r'<div class="snapshot-note">.*?</div>','<div class="snapshot-note"><span class="status-dot"></span> Latest manuscript snapshot · 82 benchmarks · 43 cross-category · checked July 2026</div>',s,count=1,flags=re.S)
 s=re.sub(r'<div class="stat-strip" aria-label="Survey statistics">.*?</div>\s*</section>', '<div class="stat-strip" aria-label="Survey statistics"><div><strong id="stat-total">82</strong><span>representative benchmarks</span></div><div><strong id="stat-cross">43</strong><span>cross-category benchmarks</span></div><div><strong>7</strong><span>evaluation targets</span></div><div><strong>3</strong><span>protocol / metric families</span></div><div><strong>4</strong><span>evaluation data sources</span></div></div></section>',s,count=1,flags=re.S)
 s=s.replace('Browse the paper snapshot.','Browse the latest paper snapshot.').replace('Search and filter the 84 representative benchmarks coded in Tables 3–9 of the latest four-dimensional survey draft.','Search and filter the 82 representative benchmarks coded in Figure 4 and Tables 3–9 of the latest manuscript.')
 s=s.replace('<strong id="result-count">84</strong>','<strong id="result-count">82</strong>')
 s=s.replace('A benchmark-centric survey of world-model evaluation','An evaluation-centric survey of world model benchmarks')
 s=s.replace('world_model_evaluation_survey_2026','world_model_benchmarks_survey_2026')
 s=s.replace('<script src="assets/app.js" defer></script>','<script src="assets/app-v3.js?v=4" defer></script>')
 s=s.replace('<script src="assets/app-v2.js" defer></script>','<script src="assets/app-v3.js?v=4" defer></script>')
 s=s.replace('<script src="assets/app-v3.js" defer></script>','<script src="assets/app-v3.js?v=4" defer></script>')
 s=s.replace('<script src="assets/app-1.js" defer></script>\n  <script src="assets/app-2.js" defer></script>\n  <script src="assets/app-3.js" defer></script>','<script src="assets/app-v3.js?v=4" defer></script>')
 p.write_text(s,encoding='utf-8')

def patch_social():
 p=ASSETS/'social-preview.svg'; s=p.read_text(encoding='utf-8'); s=s.replace('EVALUATION SURVEY','BENCHMARKS SURVEY').replace('A Survey of Benchmarks for','A Survey of').replace('World Model Evaluation','World Model Benchmarks').replace('>84</text>','>82</text>'); p.write_text(s,encoding='utf-8')

def main():
 manifest,target_by=build_manifest(); (ASSETS/'benchmarks.json').write_text(json.dumps(manifest,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
 metadata={k:manifest[k] for k in ['title','version','framework','total','crossCategory','protocolLabels','metricLabels','dataLabels','timelineBins']}; metadata['dimensions']=4; metadata['yearMin']=2018; metadata['yearMax']=2026; metadata['targets']=[v[0] for v in TARGETS.values()]; (ASSETS/'metadata.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 generate_readme(manifest,target_by); patch_index(); patch_social()
 p=DOCS/'404.html'; p.write_text(p.read_text().replace('World Model Evaluation Survey','World Model Benchmarks Survey'),encoding='utf-8')
 print('Aligned latest manuscript: 82 benchmarks, 43 cross-category.')
if __name__=='__main__': main()
