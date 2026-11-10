# VICENSAE VOICE · TS PHONETIC ADAPTER v0.1

TypeScript port of the **provisional** IPA tokenization and `vaes.phoneme-sequence/0.1` data contract from Python Adapter 001 v0.3.

## Run

```sh
tsc -p tsconfig.json
node test/test.cjs
```

No npm install, Python, or eSpeak required for the TypeScript runtime. TypeScript compiler is a build-time tool.

## Architecture

`tokenizeIPA(raw)` converts externally provided IPA text into tokens. `sequenceFromIPA(raw, source)` adds provenance. `validateSequence(x)` validates the subset of contract properties used in the adapter; it is not a substitute for a full JSON Schema validator.

**Not yet implemented:** Spanish grapheme-to-phoneme conversion, eSpeak NG execution, a voice synthesizer, phoneme timing, WAV output, acoustic voice identity, Android listening tests, and licensing clearance. The TS adapter accepts IPA; it does **not** convert arbitrary Spanish text into IPA by itself.

The existing G21/V2.3 voice and ES-1224 samples are unchanged. No GitHub remote backup has been performed.

Always Happy Egress† by Design.
