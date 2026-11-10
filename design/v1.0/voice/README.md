# VICENSAE Official Voice · Canonical Asset Registry v0.1

**Status: CANDIDATE / SOURCE ASSETS NOT VERIFIED / OFFICIAL VOICE NOT YET RELEASED.**

This directory is the canonical location for the future VICENSAE voice identity, alongside the existing design/v1.0 typography, visual tokens and preview. Do not confuse the browser speech-synthesis demonstration with an official, proprietary voice.

## Canonical paths

- `design/v1.0/voice/README.md` — voice identity and integration contract (this file).
- `design/v1.0/voice/manifests/VICENSAE_VOICE_MANIFEST_v0.1.json` — future provenance, model/audio hashes, versions, languages, authorization, and release status.
- `design/v1.0/voice/licenses/` — authoritative signed/approved license texts and third-party rights documentation (pending; no license grant is implied by this README).
- `design/v1.0/voice/models/` — versioned model references or approved distributables, only if repository policy, rights and file-size constraints allow.
- `design/v1.0/voice/samples/` — consented, licensed source samples and approved reference audio, subject to privacy review.
- `design/v1.0/voice/profiles/` — language, pronunciation, voice rendering and accessibility profiles.

Do not upload personal recordings, training datasets, voiceprints or third-party material without explicit rights and consent review. For large or restricted assets, use protected storage and immutable SHA-256-addressed references in manifests; never commit secrets.

## Integration contract

QSONGS, PAF4 and LEES should consume one canonical versioned voice manifest, not duplicate voice binaries or independently declare a voice 'official'. Every production narration should record the exact voice/profile version, source authorization, licensing scope, language, SHA-256 of delivered audio, and content version. Text remains accessible and exportable under Happy Egress†. Playback timing uses monotonic terrestrial time; DFD constitutive identifiers are not clocks.

## Release gate

1. Locate and audit original voice work and any typography-adjacent voice assets in existing PeopleArtFactory repositories and history.
2. Establish ownership, contributor permissions, consent and exact license text; separate code, typography, training data, model and generated audio rights.
3. Verify reproducible voice output and audio provenance; review languages and pronunciation.
4. Approve and publish a versioned manifest. Only then mark voice status OFFICIAL.
5. Integrate QSONG/LEES TTWNAM as a consumer, with explicit fallback labelled 'browser demo voice'.

**No audio, model, proprietary license or font binaries have been added by this checkpoint.**

QR-FR+ · PROVENANCE PENDING · OFFICIAL RELEASE WITHHOLD
