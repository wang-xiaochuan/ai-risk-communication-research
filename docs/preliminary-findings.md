# Preliminary descriptive findings

**6 October 2026. Exploratory descriptive results; independent coding reliability and sensitivity checks outstanding.** This English summary follows the current Chinese manuscript sections 12-14 ([public excerpt](manuscript-findings-zh.md)); they do not reinstate earlier withdrawn findings. Every number below is recomputable from the reduced coded records. See [reproduction instructions](../REPRODUCING.md).

## Scope and units

304 transcripts / 840 windows are fully coded and aggregated. Core supply comparisons use 278 E1-E3 videos: Simplified Chinese 38, Traditional Chinese 19, English 221. The remaining 26 E4 videos are exploratory and excluded from those comparisons. Reception uses 5,967 linked interactions: 4,649 comments and 1,318 danmaku. Comment comparisons cover 101 videos. Platform, content-language and audience residence are distinct concepts.

## 1. Risk emphasis can coexist with recommendations

| Coded content group | Core videos | Mean risk-benefit score | Risk-more count category | Videos with an institutional recommendation |
|---|---:|---:|---:|---:|
| Simplified Chinese | 38 | -0.2303 | 21 | 29 |
| Traditional Chinese | 19 | -0.1079 | 10 | 18 |
| English | 221 | -0.5467 | 201 | 181 |

Among risk-more videos, recommendations also appear in 13/21 Simplified Chinese, 10/10 Traditional Chinese, and 165/201 English videos. Risk-heavy discourse therefore cannot by itself establish a lack of response proposals. The score includes actual risk/benefit discourse across the full transcript, including off-topic material; it is not an AI-only danger score, duration share, or response-efficacy measure.

## 2. Recommendations usually address institutions

| Recommendation receiver (video-level union) | Simplified Chinese (38 videos) | Traditional Chinese (19 videos) | English (221 videos) |
|---|---:|---:|---:|
| Industry | 19 | 8 | 109 |
| Political institutions | 11 | 13 | 108 |
| Public | 0 | 0 | 14 |
| Academia | 0 | 0 | 10 |

Categories can overlap. Zero means no public-directed institutional recommendation was identified under this coding convention, not that a language community lacks agency or personal advice. The distinction between institutional responses and audience participation is a question for communication design, not an established intervention effect.

## 3. Comment attribution differs in this selected corpus

Percentages below are comment-weighted, with explicit comment and video denominators.

| Coding category | Simplified Chinese (1,268 comments / 27 videos) | Traditional Chinese (631 / 19) | English (2,750 / 55) |
|---|---:|---:|---:|
| R01 danger-control demands | 6.6% | 7.3% | 10.9% |
| R02 fatalistic expressions | 4.5% | 7.9% | 6.5% |
| R03 cynicism / motive attribution | 16.6% | 4.0% | 11.1% |
| R04 defensive othering | 7.8% | 9.7% | 2.5% |
| R05 technical / neutral discourse | 52.6% | 39.5% | 47.6% |
| R99 unclassifiable | 11.9% | 31.7% | 21.4% |

R05 is the largest category in all three groups; it also includes some playful responses without coded helplessness or motive attribution. R99 is substantial and must not be silently excluded. Video-equal-weighted R03 percentages are 16.5%, 3.8%, and 11.1%; R04 percentages are 8.0%, 8.2%, and 2.5%. These are structures of observable expression, not population psychological profiles.

## 4. Supply-reception associations remain exploratory

Across 101 comment-bearing core videos (4,649 comments), descriptive Spearman rho between the risk-benefit score and R01 comment share is -0.3193. The corresponding association with the combined R02-R04 share is -0.0343. These pooled figures are unadjusted; ecosystem- and event-specific results are in the machine-readable outputs. Neither a significant effect nor a null effect is inferred. Event composition, format and duration remain potential confounders.

## Limits and validation status

Core event composition is uneven: Simplified Chinese E1/E2/E3 = 31/4/3; Traditional Chinese = 12/3/4; English = 81/81/59. Small cells prevent strong event-specific comparative claims. Formal audit completion does not establish semantic accuracy. Multi-agent division of coding work and violation rejudging do not constitute independent double coding. Exact model IDs, temperatures and token metadata are unavailable for some sessions.

Independent semantic review, reliability, segmentation/window-boundary sensitivity, off-topic sensitivity, title recoding, fitted frame-cluster analysis, uncertainty estimation and confounder-adjusted models remain outstanding. No causal mediation claim is made.

## Source pointers

- [Main recomputed facts](../results/manuscript-findings-facts.json)
- [Detailed recomputed facts](../results/manuscript-findings-detail.json)
- [Video-level input](../data/video-level.csv)
- [Main aggregation script](../scripts/build_manuscript_findings.py)
- [Detail aggregation script](../scripts/build_manuscript_detail.py)

## Event and modality detail from the manuscript

Within E1, comment-weighted R03 is 16.4% / 2.2% / 9.0% in Simplified Chinese / Traditional Chinese / English (970/409/900 comments across 20/12/18 videos); R04 is 7.1% / 10.3% / 1.8%. These comparisons preserve the observed direction within a shared event, but do not identify a language effect.

English E1/E2/E3 comments (900/900/950 records across 18/18/19 videos) have R02 percentages of 5.1%/10.6%/3.9% and R03 percentages of 9.0%/5.6%/18.2%. Attribution differs by event as well as content group.

For the same 20 Bilibili videos with both modalities, 938 comments and 1,318 danmaku yield equal-video-weighted R03 shares of 16.1% versus 3.1%, and R99 shares of 10.0% versus 29.8%. This is a paired-video channel comparison, not a within-person attitude change.

Event-specific score versus combined R02-R04 correlations are +0.138/+0.237/-0.509 for E1/E2/E3 (50/25/26 videos). The pooled near-zero value is not evidence that each event has no structure. No significance or null-effect inference is made.

## Discussion and conclusion

Following manuscript sections 13-14, the main interpretation is that risk emphasis, institutional recommendations, audience skepticism and accountability demands can coexist. “More risk necessarily closes rational response” is not a uniform descriptive pattern in this corpus. Benefit, response efficacy and self-efficacy must be measured separately; the current variables do not test a causal EPPM pathway.

Proposed communication directions are to make evidence and commercial interests auditable, specify responsibility in geopolitical discussion, and connect institutional responses with routes for public participation. These are proposals for testing, not validated prescriptions for whole language populations. Public-facing recommendations should state what risk has actually been observed, who is responsible, and which action is feasible.
