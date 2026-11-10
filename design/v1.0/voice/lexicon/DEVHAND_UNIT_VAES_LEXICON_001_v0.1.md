# DevHand Unit — VAES Lexicon Packs and Canonical Open-Source Candidate

**ID:** `VICENSAE-DEVHAND-VOICE-LEXICON-001`  
**Version:** `0.1` · **Status:** experimental, rights review required  
**Scope:** VICENSÆ Voice V2.3 · additive lexical packs · no UI/CSS changes  
**Frozen baseline:** V2.2/G21 embedded lexicon, preserved unchanged

## 1. Purpose and non-negotiable invariants

V2.3 pronounces words already present in the embedded G21 lexicon and spells unknown words. The extension protocol allows an operator to load additional PCM word samples from JSON, without editing or overwriting the embedded HTML. **Loading a pack does not make the voice a general-purpose Spanish TTS.**

- Do not alter frozen G21 samples, V2.3 HTML/CSS, existing identifiers, or the Earth Meter rate.
- No browser `speechSynthesis`, remote `fetch`, or server is needed to import the pack.
- A pack must not replace an existing base or previously imported word.
- Packs are transient: reload them after reopening the page.
- Licenses and audio rights must be recorded per source; declaring a license string does not grant rights.
- Hashes verify bytes, not authorization or listening intelligibility.

## 2. How to use the dictionary on Android

1. Open the original `VICENSAE_VOICE_V2_3_EXTENSIBLE_v0.1/index.html` unchanged.
2. Under **05 · Biblioteca de voz ampliable**, tap the file picker and choose `VAES_LEXICON_ES_FIDUCIARY_CANDIDATE_v0.1.json`.
3. Wait for the successful import message; the import is rejected atomically on a conflict or malformed entry.
4. Enter a phrase containing a newly imported word, tap **Generar y escuchar**, then optionally export the WAV.
5. Reimport after refreshing/reopening the HTML. For durable availability, a future opt-in IndexedDB cache can store approved packs without changing the base dictionary.

If an imported word is already present in G21, the entire pack is rejected. Pack IDs must be unique. The importer currently limits each JSON to **8 MB**, **1–500 words**, individual base64 strings to **300,000 characters**, and key length to **40 Spanish alphabetic characters**. It requires **22,050 Hz**, signed 16-bit mono PCM encoded as base64. No audio header is included inside each base64 field.

## 3. Wire contract — `vaes.lexicon-pack/0.1`

```json
{
  "schema": "vaes.lexicon-pack/0.1",
  "id": "org.vicensae.es.fiduciary.open-source.v0.1",
  "sampleRate": 22050,
  "encoding": "pcm_s16le_base64",
  "license": "SOURCE_ENGINE_GPL-3.0-or-later__OUTPUT_RIGHTS_REVIEW_REQUIRED",
  "provenance": "Generation method and review status; see manifest",
  "words": {"palabra": "BASE64_RAW_PCM_S16LE"}
}
```

The `words` object maps normalized lowercase lexical tokens to standalone spoken samples. **Do not confuse text lexicons, phonetic dictionaries, and audio sample libraries.** This version is the latter. For scalable speech, introduce a separate, versioned phoneme/syllable layer rather than pretending a growing word list solves coarticulation and prosody.

## 4. Open sources and rights matrix

| Source | Useful for | Rights / limitations | Decision |
|---|---|---|---|
| eSpeak NG | Spanish phonetics, reproducible open synthesis | GPL-3.0-or-later engine; bundled components may have additional licenses; output and redistribution require separate analysis | Reference candidate; do not silently incorporate engine into proprietary code |
| Legacy eSpeak 1.48.15 | Exact reproduction of G21-style sample generation in this environment | Older software; inspect its actual distributed license and audio output rights separately | Used to generate this **candidate** pack; not rights-cleared |
| Mozilla Common Voice Spanish | CC0 speech data, evaluation and research | Datasets published CC0; human voices vary; consent, provenance and consistency matter | Future evaluation / curated research, not used in this pack |
| Wiktionary | Lexical/IPA reference | Attribution/share-alike obligations and possible database restrictions | Do not copy blindly into VPPL corpus |

Open source does **not** mean public domain. The proprietary/VPPL licensing of original VICENSÆ code does not automatically relicense third-party tools, recordings, or phonetic data. The generated pack's `license` field explicitly indicates **review required**. It is **not approved for commercial distribution** by this unit.

## 5. Canonical build procedure

The bundled `build_lexicon.py` generates a reproducible candidate from an explicit vocabulary, using a locally installed eSpeak executable and SciPy for resampling. Pin executable version, input words, generation settings, and output hashes in a release. To approve a production pack, replace the placeholder rights status with verified permissions and add listening tests, reproducible source artifacts and an approval signature.

## 6. Acceptance criteria

- [x] Candidate pack conforms to V2.3 importer schema and size limits.
- [x] No collision with frozen G21 base dictionary.
- [x] SHA-256 manifest and per-word PCM hashes generated.
- [x] Original V2.3 HTML left unchanged.
- [ ] Auditory intelligibility and coarticulation tested by listeners.
- [ ] Audio redistribution and commercial license clearance.
- [ ] Android import and playback validated on target device.
- [ ] GitHub backup of complete pack and source verified by round-trip hash.

## 7. Next development increment

`vaes.lexicon-pack/0.2` should add `sources[]`, `wordProvenance`, `sourceSha256`, optional `phonemes`, `locale`, `voiceProfile`, explicit rights flags, collision policy and a signed pack manifest. Preserve `0.1` compatibility through an adapter; do not reinterpret or mutate original G21 bytes.

**Always Happy Egress† by Design.**
