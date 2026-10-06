# Methods and release boundaries

The prompts and JSON schemas are snapshots of the current coding workflow on 6 October 2026. They are provided for methodological inspection, not as a validated off-the-shelf measurement instrument.

## Reception coding

Each comment or timestamped on-screen message is assigned perceived threat, attribution/efficacy exit, responsibility, and actionability, with a rationale and source quotation. The operational taxonomy and precedence rules are in `prompts/system-interaction.md`; the output structure is in `schemas/interaction.schema.json`. Coding labels do not establish a respondent's psychological state.

## Transcript coding

The active window-based workflow reads sentence segments within windows of at most 6,000 characters. It returns risk and benefit segment IDs, counts, evaluation, institutional recommendations and recipients, evidence, and confidence. Aggregate scores are intended to be derived from validated window records. See `prompts/system-transcript-window.md` and its corresponding schema. The whole-transcript prompt/schema are retained as companion artifacts and must not be mixed into a run without explicit versioning.

## Validation still required

Independent semantic review and coding reliability, cross-language equivalence, degeneracy checks, aggregation verification, and appropriate video-level statistical inference remain necessary. Formal checks of JSON structure and verbatim quotation do not substitute for these.

## Reproduction status

This release contains no raw research corpus, complete execution environment, or aggregate-analysis runner. It cannot independently reproduce the study's results. Future reproducibility releases must declare input hashes, versions, analysis units, exclusions, and mechanically derived statistics.
