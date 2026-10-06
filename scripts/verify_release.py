#!/usr/bin/env python3
"""Verify release hashes, aggregation outputs and numeric input alignment."""
import csv,json,hashlib,subprocess,sys,math
from pathlib import Path
from collections import Counter,defaultdict
ROOT=Path(__file__).resolve().parent.parent

def require(ok,message):
    if not ok: raise ValueError(message)

def main():
    manifest=json.loads((ROOT/'release-manifest.json').read_text())
    for r in manifest['files']:
        require(hashlib.sha256((ROOT/r['path']).read_bytes()).hexdigest()==r['sha256'],'hash mismatch: '+r['path'])
    videos=list(csv.DictReader((ROOT/'data/video-level.csv').open(encoding='utf-8-sig')))
    transcripts=[json.loads(l) for l in (ROOT/'data/transcript-codes.jsonl').read_text().splitlines()]
    audience=[json.loads(l) for l in (ROOT/'data/interaction-codes.jsonl').read_text().splitlines()]
    require(len(videos)==len(transcripts)==304,'transcript/video counts')
    require(len(audience)==5967,'audience count')
    require(sum(t['aggregation']['window_count'] for t in transcripts)==840,'window count')
    byvid={v['video_id']:v for v in videos}; aa=defaultdict(list)
    for a in audience: aa[a['vid']].append(a)
    for t in transcripts:
        v=byvid[t['vid']];a=t['aggregation'];m=t['measures']
        require(int(v['risk_segment_count'])==a['risk_hit_count'] and int(v['benefit_segment_count'])==a['benefit_hit_count'],'segment-count alignment')
        den=a['risk_hit_count']+a['benefit_hit_count'];score=round((a['benefit_hit_count']-a['risk_hit_count'])/den,2) if den else 0
        require(abs(score-m['risk_benefit_score'])<=0.0001,'score formula')
        require(float(v['risk_benefit_score'])==m['risk_benefit_score'],'score alignment')
        for kind in ['comment','danmaku']:
            xs=[x for x in aa[t['vid']] if x['type']==kind]; cc=Counter(x['measures']['attribution_exit'] for x in xs)
            require(int(v[kind+'_n'])==len(xs),'interaction alignment')
            for code in ['R01','R02','R03','R04','R05','R99']:
                require(int(v[kind+'_'+code+'_n'])==cc[code],'code-count alignment')
    for script in ['build_manuscript_findings.py','build_manuscript_detail.py']:
        subprocess.run([sys.executable,str(ROOT/'scripts'/script)],check=True,stdout=subprocess.DEVNULL)
    for file,expected,omit in [('manuscript-findings-facts.json','findings-expected.json',['inputs','aggregation_script','aggregation_script_sha256']),('manuscript-findings-detail.json','detail-expected.json',['inputs','script','script_sha256','notes'])]:
        actual=json.loads((ROOT/'results'/file).read_text())
        for k in omit:actual.pop(k,None)
        require(actual==json.loads((ROOT/'reference'/expected).read_text()),'full result mismatch: '+file)
    print('PASS: release hashes, 304 video records, 840 window counts, 5967 coded interactions, and all released findings reproduced. This is aggregation verification, not independent semantic validation.')

if __name__=='__main__':main()
