# VICENSAE Voice v1.0 — experimental consolidation

This backup branch preserves existing `main`, the G21/V2.3 voice and the provisional TS phonetic adapter. The new release reproduces the frozen v0.9 prosody renderer and replaces ONLY the first chorus (52.1739–73.04349 s) of the v0.2 full song with a 120 ms crossfade. Total duration 286.34780045351476 s. The remaining sections remain v0.2, re-encoded. No neural synthesis, perceptual improvement, production DFD, commercial admission or license clearance claimed.

## Remote preservation
- Exact bytes: 2 historical Python renderers, 7 historical profiles, 2 historical QSeed files, 2 historical standalone HTML players (14 ordered text fragments), and their 2 embedded MP3s (recoverable byte-for-byte). The original v0.2 HTML has a source hash metadata discrepancy versus the standalone QSeed; both were preserved, not silently edited.
- v1.0: exact tested build source, QSeed and inherited prosody profile.
- Run `python RESTORE_PLAYERS_v1.0.py` to reconstruct the original two HTMLs and MP3s with SHA-256 validation. Use byte-preserving checkout (no newline conversion).
- Local complete archive contains all 35 historical files and 8 release files, 47 manifest-covered files plus manifest. Local ZIP SHA-256: b14af3f3b15a806db2880c90b120752e14dd4d0cbdd2b869a998250b11dabb8b.
- **Remote incomplete:** isolated vocal/chorus historical MP3s, final v1.0 audio and HTML, full local ZIP and ancillary backup scripts have not been transferred. The remote QSeed records the local audio SHA-256; it does not establish remote availability of that audio. To complete, download and unpack the local ZIP, then run its COMPLETE_GITHUB_BACKUP_v1.0.sh with authenticated Git and review the resulting commit.
- Run `python VOICE_BUILD_v1.0.py` only when the missing inputs (especially v08 TRACTO and ARTICULATORIA MP3) are supplied from the complete archive. Reference environment Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, FFmpeg 7.1.5, Node 22. The v0.9 reference re-render was byte-identical for its three MP3s and profile. TypeScript audio renderer remains pending.

No new license is granted. Existing author rights and applicable upstream licenses remain unchanged.

Always Happy Egress† by Design.

QR-F
