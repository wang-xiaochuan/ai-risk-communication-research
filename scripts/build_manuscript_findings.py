#!/usr/bin/env python3
"""Descriptive facts for PAPER Q12-Q14, from preserved local adjudications.

Language cells come from event metadata, never a non-English platform fallback.
Correlation is descriptive, not a significance test or causal estimate.
"""
import csv, hashlib, json, math, statistics
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'results'
OUT.mkdir(exist_ok=True)
FILES = {
    'videos': ROOT / 'data/video-level.csv',
    'interactions': ROOT / 'data/interaction-codes.jsonl',
    'event_metadata': ROOT / 'data/event-metadata.csv',
}
CODES = ['R01', 'R02', 'R03', 'R04', 'R05', 'R99']

def require(condition, message):
    if not condition:
        raise ValueError(message)

def ranks(values):
    order = sorted(range(len(values)), key=lambda i: values[i])
    result = [0.0] * len(values)
    start = 0
    while start < len(order):
        end = start + 1
        while end < len(order) and values[order[end]] == values[order[start]]:
            end += 1
        for i in order[start:end]:
            result[i] = (start + end + 1) / 2
        start = end
    return result

def spearman(x, y):
    a, b = ranks(x), ranks(y)
    am, bm = statistics.mean(a), statistics.mean(b)
    den = math.sqrt(sum((v-am)**2 for v in a) * sum((v-bm)**2 for v in b))
    return round(sum((v-am)*(w-bm) for v,w in zip(a,b))/den, 4) if den else None

def main():
    hashes = {k: hashlib.sha256(p.read_bytes()).hexdigest() for k,p in FILES.items()}
    videos = list(csv.DictReader(FILES['videos'].open(encoding='utf-8-sig')))
    interactions = [json.loads(s) for s in FILES['interactions'].read_text().splitlines()]
    require(len(videos) == len({x['video_id'] for x in videos}) == 304, 'video coverage')
    require(len(interactions) == len({x['unit_id'] for x in interactions}) == 5967, 'interaction coverage')
    cells = defaultdict(set)
    for row in csv.DictReader(FILES['event_metadata'].open(encoding='utf-8-sig')):
        u = urlparse(row['链接'])
        vid = parse_qs(u.query).get('v', [None])[0] if 'youtube' in u.netloc else next((s for s in u.path.split('/') if s.startswith('BV')), None)
        if vid:
            cells[(vid, row['事件'])].add(row['内容格'])
    mapping = []
    for v in videos:
        key = (v['video_id'], v['event'])
        require(len(cells[key]) == 1, f'missing/ambiguous metadata: {key}')
        v['ecosystem_cell'] = next(iter(cells[key]))
        mapping.append({'vid': v['video_id'], 'event':v['event'], 'platform':v['selected_platform'], 'selected_cell':v['selected_cell'], 'ecosystem_cell':v['ecosystem_cell']})
    byvid = {v['video_id']:v for v in videos}
    audience = defaultdict(list)
    for a in interactions:
        v = byvid[a['vid']]
        require(a['event'] == v['event'] and a['cell'] == v['ecosystem_cell'], 'interaction metadata differs from event metadata')
        audience[a['vid']].append(a)
    core = [v for v in videos if v['event'] != 'E4']
    def supply(vs):
        return {'videos':len(vs), 'events':dict(Counter(v['event'] for v in vs)), 'score_mean':round(statistics.mean(float(v['risk_benefit_score']) for v in vs),4), 'frame_counts':dict(Counter(v['frame_quadrant'] for v in vs)), 'treatment_videos':sum(v['treatment_present']=='True' for v in vs)}
    def reception(xs):
        counts=Counter(x['measures']['attribution_exit'] for x in xs)
        vv=defaultdict(list)
        for x in xs: vv[x['vid']].append(x)
        return {'units':len(xs),'videos':len(vv),'counts':{c:counts[c] for c in CODES},'unit_percent':{c:round(100*counts[c]/len(xs),4) for c in CODES},'mean_video_percent':{c:round(100*statistics.mean(sum(x['measures']['attribution_exit']==c for x in aa)/len(aa) for aa in vv.values()),4) for c in CODES},'perceived_threat_counts':dict(Counter(x['measures']['perceived_threat'] for x in xs))}
    eco = sorted({v['ecosystem_cell'] for v in core})
    supply_facts={cell:supply([v for v in core if v['ecosystem_cell']==cell]) for cell in eco}
    reception_facts={cell:reception([a for a in interactions if a['type']=='comment' and a['cell']==cell]) for cell in eco}
    e1_comments={cell:reception([a for a in interactions if a['type']=='comment' and a['cell']==cell and a['event']=='E1']) for cell in eco}
    matched=[]
    for v in core:
        aa=[a for a in audience[v['video_id']] if a['type']=='comment']
        if not aa: continue
        n=len(aa); cc=Counter(a['measures']['attribution_exit'] for a in aa)
        matched.append({'vid':v['video_id'],'event':v['event'],'cell':v['ecosystem_cell'],'score':float(v['risk_benefit_score']),'frame':v['frame_quadrant'],'treatment':v['treatment_present']=='True','comment_n':n,'R01_share':cc['R01']/n,'R02_R04_share':sum(cc[c] for c in ['R02','R03','R04'])/n,'high_moderate_threat_share':sum(a['measures']['perceived_threat'] in ['high','moderate'] for a in aa)/n})
    def covariation(ms):
        return {'videos':len(ms),'comments':sum(x['comment_n'] for x in ms),'rho_score_R01':spearman([x['score'] for x in ms],[x['R01_share'] for x in ms]),'rho_score_R02_R04':spearman([x['score'] for x in ms],[x['R02_R04_share'] for x in ms]),'rho_score_perceived_threat':spearman([x['score'] for x in ms],[x['high_moderate_threat_share'] for x in ms])}
    groups={}
    for name, pred in [('risk_more',lambda x:x['frame']=='high-threat'),('other_frames',lambda x:x['frame']!='high-threat'),('recommendation_present',lambda x:x['treatment']),('recommendation_absent',lambda x:not x['treatment'])]:
        ms=[x for x in matched if pred(x)]
        groups[name]={'videos':len(ms),'comments':sum(x['comment_n'] for x in ms),'mean_video_R01_percent':round(100*statistics.mean(x['R01_share'] for x in ms),4) if ms else None,'mean_video_R02_R04_percent':round(100*statistics.mean(x['R02_R04_share'] for x in ms),4) if ms else None}
    result={'status':'EXPLORATORY_DESCRIPTIVE_NOT_ACCEPTANCE_CERTIFICATION','inputs':hashes,'mapping_source':'unique event-metadata cell by parsed link video ID and event; all 5967 interaction cells agree','core_videos':278,'exploratory_videos':26,'core_supply':supply_facts,'comments':reception_facts,'E1_comments':e1_comments,'bilibili_danmaku':reception([a for a in interactions if a['type']=='danmaku']),'covariation_all':covariation(matched),'covariation_by_cell':{cell:covariation([m for m in matched if m['cell']==cell]) for cell in eco},'descriptive_groups':groups,'omitted':['Independent semantic review and coding reliability','Segmentation/window-boundary and off-topic sensitivity','Title recoding and title-transcript comparison','Published-framework cluster procedure and EPPM threat-by-efficacy classification','Confidence intervals, p values, confounder-adjusted models and causal mediation'], 'interpretation':['risk_benefit_score measures benefits versus risks; benefit is not response efficacy','treatment_present denotes an institutional suggestion somewhere in the transcript, not proven actionability or self-efficacy','frame labels are deterministic count summaries, not fitted published-framework clusters','rho is descriptive and unadjusted; no significance or null-effect claim','ecological cell labels are source classifications, not verified viewer residence']}
    result['aggregation_script'] = 'scripts/build_manuscript_findings.py'
    result['aggregation_script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (OUT/'manuscript-findings-facts.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    (OUT/'manuscript-ecosystem-mapping.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
