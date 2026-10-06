#!/usr/bin/env python3
"""Finer descriptive findings and explicitly selected illustrative cases.

No recoding, significance tests, inferred population beliefs, or old labels.
"""
import hashlib, importlib.util, json, statistics
from collections import Counter, defaultdict
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
OUT=ROOT/'results'

def module(name, path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    return m

f=module('findings_detail_base',HERE/'build_manuscript_findings.py')


def main():
    paths={'transcripts':ROOT/'data/transcript-codes.jsonl','interactions':ROOT/'data/interaction-codes.jsonl','ecosystem_mapping':OUT/'manuscript-ecosystem-mapping.json'}
    ts=[json.loads(s) for s in paths['transcripts'].read_text().splitlines()]
    aa=[json.loads(s) for s in paths['interactions'].read_text().splitlines()]
    mapping={x['vid']:x for x in json.loads(paths['ecosystem_mapping'].read_text())}
    core=[t for t in ts if t['event']!='E4']
    comments=[a for a in aa if a['type']=='comment']
    byvid=defaultdict(list)
    for a in aa:byvid[a['vid']].append(a)
    cells=['简体中文（大陆）','繁体中文（台港）','英文']
    codes=['R01','R02','R03','R04','R05','R99']
    supply={}
    for cell in cells:
        vv=[t for t in core if mapping[t['vid']]['ecosystem_cell']==cell]
        receivers=Counter();types=Counter();cross=Counter()
        for t in vv:
            al=t['aggregation']['treatment_alternatives']
            receivers.update({x['treatment']['receiver'] for x in al})
            types.update({x['treatment']['type'] for x in al})
            cross[(t['measures']['frame_quadrant']=='high-threat',t['measures']['treatment']['present'])]+=1
        supply[cell]={'videos':len(vv),'recommendation_receivers_video_union':dict(receivers),'recommendation_types_video_union':dict(types),'evaluation_counts':dict(Counter(t['measures']['evaluation'] for t in vv)),'risk_more_but_mixed_evaluation':sum(t['measures']['frame_quadrant']=='high-threat' and t['measures']['evaluation']=='mixed' for t in vv),'risk_more_and_recommendation':cross[(True,True)],'risk_more_without_recommendation':cross[(True,False)]}
    joint={}
    for cell in cells:
        av=[a for a in comments if a['cell']==cell]
        joint[cell]={code:{'units':sum(a['measures']['attribution_exit']==code for a in av),'threat_levels':dict(Counter(a['measures']['perceived_threat'] for a in av if a['measures']['attribution_exit']==code))} for code in codes}
    english_events={};event_covariation={}
    for event in ['E1','E2','E3']:
        xs=[a for a in comments if a['cell']=='英文' and a['event']==event]
        cc=Counter(a['measures']['attribution_exit'] for a in xs)
        tv=[t for t in core if t['event']==event and mapping[t['vid']]['ecosystem_cell']=='英文']
        english_events[event]={'comment_units':len(xs),'comment_videos':len({a['vid'] for a in xs}),'counts':dict(cc),'unit_percent':{code:round(100*cc[code]/len(xs),4) for code in codes},'transcript_videos':len(tv),'score_mean':round(statistics.mean(t['measures']['risk_benefit_score'] for t in tv),4),'recommendation_videos':sum(t['measures']['treatment']['present'] for t in tv)}
        matched=[]
        for t in core:
            ac=[a for a in byvid[t['vid']] if a['type']=='comment']
            if t['event']==event and ac:matched.append((t,ac))
        scores=[t['measures']['risk_benefit_score'] for t,ac in matched]
        r01=[sum(a['measures']['attribution_exit']=='R01' for a in ac)/len(ac) for t,ac in matched]
        defens=[sum(a['measures']['attribution_exit'] in ['R02','R03','R04'] for a in ac)/len(ac) for t,ac in matched]
        event_covariation[event]={'videos':len(matched),'comments':sum(len(ac) for t,ac in matched),'rho_score_R01':f.spearman(scores,r01),'rho_score_R02_R04':f.spearman(scores,defens)}
    paired=[(vid,xs) for vid,xs in byvid.items() if any(a['type']=='comment' for a in xs) and any(a['type']=='danmaku' for a in xs)]
    modality={'paired_videos':len(paired),'video_ids':[v for v,xs in paired]}
    for kind in ['comment','danmaku']:
        xs=[a for vid,av in paired for a in av if a['type']==kind]
        cc=Counter(a['measures']['attribution_exit'] for a in xs)
        modality[kind]={'units':len(xs),'counts':dict(cc),'mean_video_percent':{code:round(100*statistics.mean(sum(a['type']==kind and a['measures']['attribution_exit']==code for a in av)/sum(a['type']==kind for a in av) for vid,av in paired),4) for code in codes}}
    result={'status':'EXPLORATORY_DETAIL_NO_RECODING','script':'scripts/build_manuscript_detail.py','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'inputs':{k:hashlib.sha256(p.read_bytes()).hexdigest() for k,p in paths.items()},'core_supply_detail':supply,'comment_code_threat_cross':joint,'english_event_detail':english_events,'event_covariation':event_covariation,'paired_comment_danmaku':modality,'notes':['Recommendation receiver/type counts use union over retained window alternatives: each video counted once per category; categories overlap.','No low-efficacy construct, duration share, causal effects, p values or independent reliability computed.','Source text and illustrative quotations are omitted from this public release.','Paired modality comparison uses same videos, not same individuals.','E1-E3 event correlations are unadjusted descriptive results; event/cell blocks under 10 videos do not get percentage-based claims.']}
    (OUT/'manuscript-findings-detail.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:result[k] for k in ['core_supply_detail','english_event_detail','event_covariation','paired_comment_danmaku']},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
