# VICENSAE DevHand · Lexicon Unit 001 v0.1 — recovery and publication gate

Status: EXPERIMENTAL. This file is a **remote recovery record, not a complete upload**. Date: 2026-11-10.

## Scope
Canonical repository: PeopleArtFactory/VICENSAE
Frozen base: V2.2/G21 embedded voice lexicon. V2.3 accepts additive JSON lexicon packs without changing its HTML, CSS, Earth Meter, or frozen samples.

## Usage
Open V2.3, use "05 · Biblioteca de voz ampliable", import `VAES_LEXICON_ES_FIDUCIARY_CANDIDATE_v0.1.json`, enter text and generate. Reimport after reopening. Unknown words remain spelled out. A pack cannot replace base words.

## Pack format
`schema: "vaes.lexicon-pack/0.1"`, `sampleRate: 22050`, `encoding: "pcm_s16le_base64"`, `words: {"palabra":"BASE64_RAW_PCM_S16LE"}`. Limits: 8 MB, 1–500 words. Include provenance and license status. The candidate uses legacy eSpeak 1.48.15 to generate 12 words, not a human voice corpus. Rights review required before commercial redistribution. eSpeak NG, Common Voice and Wiktionary are research references, not automatically incorporated.

## Frozen package and SHA-256
`VICENSAE_DEVHAND_LEXICON_CANONICAL_v0.1.zip`: `3e9d52ee660adc050fc78c1043e55238f7e737df9cf6217b5b6cd073305e1f2f`

Files expected in full upload:
- `DEVHAND_UNIT_VAES_LEXICON_001_v0.1.md`: `01e21592b7e8de6d889d669a4e06293eb2d3534b524cfdeac2aec79906dff950`
- `VAES_LEXICON_ES_FIDUCIARY_CANDIDATE_v0.1.json`: `094eab13cbb8d59183b019d2d327c21ee5a3a0a832997b9bd313abec752736db`
- `ENTRIES_PROVENANCE_v0.1.json`: `887cc551476258dad974b00545b8b29567d32bf6e6f161e080c5e1931bdb634a`
- `build_lexicon.py`: `edf0da673d637ec2d706c75b9bd563165619c041bd62404786eb8968d6031095`

**NOT UPLOADED BY THIS COMMIT:** the above full source files, the 981 KB JSON, and ZIP. Upload those bytes to a release or repository, download again and verify hashes. Do not claim backup complete before that.

Always Happy Egress† by Design.
