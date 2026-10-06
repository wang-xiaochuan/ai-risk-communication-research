# Communicating AI Risk Across Languages

Video narratives and audience responses on Bilibili and YouTube.

**Status: research in progress.** This repository provides supporting materials for a proposed IASEAI 2027 talk. It is an initial documentation and coding-protocol release, not a completed empirical paper or an executable reproduction package. Proposal acceptance has not been confirmed.

## Research questions

1. How do video titles and full narratives frame societal threats and responses across English, Simplified Chinese, and Traditional Chinese content?
2. How do audience interactions express threat, attribution, skepticism, and possible responses?
3. To what extent do supply and reception measures co-vary at the video level?

## Start here

- [Research note](docs/research-note.md): design, corpus, analysis plan, and limits.
- [Talk proposal](docs/talk-proposal.md): presentation description and audience takeaways.
- [One-page supporting PDF](materials/supporting-research-note.pdf).
- [Coding prompts](methods/prompts/) and [output schemas](methods/schemas/): current operational artifacts, released for inspection. They require semantic validation; schema compliance alone is not coding reliability.
- [Methods and release boundaries](methods/README.md).

## Corpus

| Asset | Count | Meaning |
|---|---:|---|
| Core event-related titles | 4,331 | Three-event title corpus |
| Selected videos with transcripts | 304 | View-coverage selection; not population representative |
| Linked audience interactions | 5,967 | Reception records linked to the selected videos |
| Other archived interactions | 556 | Outside this selection; excluded from aligned analysis |

Selected platform/content split: Bilibili 35, English-language YouTube 236, Chinese-language YouTube 33. These platform/content counts must not be equated with inferred geographical populations.

The linked interactions have structured recoding records and completed schema/quotation checks. Transcript recoding, independent reliability assessment, and aggregate analysis remain in progress. Counts describe data assets; they are not substantive findings. Prior exploratory statistics are not supplied as evidence here.

## Evidence limits

This observational, selective corpus cannot establish population attitudes or causal effects. Language and platform are partly confounded. Comments and timestamped on-screen messages are situated discourse, not transparent measures of private beliefs. No validated intervention effect or mediation mechanism is claimed.

## Data availability

Raw transcripts, audience text, account identifiers, private correspondence, credentials, and internal review logs are not included in this release. Data redistribution and anonymization require a separate review. No public full-data release is promised at this stage.

## Planned additions

- Validated aggregate tables, with units, effective sample sizes, and uncertainty.
- Independent coding reliability reports and documented disagreements.
- Analysis code, environment specification, and number-level recomputation manifest.
- A clear public data-access and redistribution policy.

## Attribution and AI assistance

Maintained by Xiaochuan Wang in connection with research and community work at 706. This wording does not establish additional authorship or institutional endorsement. AI assistance is used in drafting and structured coding; human decisions and validation remain necessary. Exact model and sampling metadata are unavailable for some coding sessions and will be disclosed as missing rather than inferred.

Funding and competing-interest declarations are pending confirmation and will be completed separately for the conference submission.

Last updated: 6 October 2026.
