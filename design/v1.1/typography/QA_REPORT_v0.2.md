# VICENSAE Typefaces v0.2 — Local binary QA report

Date: 2026-11-09. Status: **PARTIAL PASS / PRODUCTION WITHHOLD**.

## Inspection method
Inspected the 15 TTF binaries in the conversation artifact `VICENSAE_TYPEFACES_OFL_v0.2.zip` with fontTools TTFont, using `getBestCmap()`. These binaries **are not yet uploaded to GitHub**. This report documents local observations, not a repository binary audit.

| Family | Light | Regular | Bold | Æ | æ | € |
|---|---:|---:|---:|---|---|---|
| UI | 2840 | 2840 | 2840 | Present | Present | Present |
| Text | 2840 | 2840 | 2840 | Present | Present | Present |
| Display | 2840 | 2840 | 2840 | Present | Present | Present |
| Mono | 3367 | 3367 | 3367 | Present | Present | Present |
| Canon | 2840 | 2840 | 2840 | Present | Present | Present |

The numbers are mapped Unicode code points, not independently drawn glyphs. They supersede the earlier 157-character description for these **v0.2** derivatives; 157 belonged to the separate Genesis v0.1 prototypes.

## Open gates

1. Upload and verify the **30** binary TTF/WOFF2 files, comparing against the existing local SHA-256 manifest.
2. Confirm that the upstream Noto font files, versions, notices and SIL OFL 1.1 requirements are accurately preserved. Do not claim exclusive originality of derivative outlines.
3. Visual regression and spacing review at common sizes, especially `Æ/æ`, `Ñ/ñ`, diacritics and mathematical punctuation.
4. Validate WOFF2 decode, name tables, metrics, weights, fixed pitch in Mono, and font-display loading.
5. Test in modern browsers and real PAF4/QSONG/COIIRM layouts.
6. Do not mark typography as master-approved until legal and design sign-off.

**No production approval, cryptographic admission, or warranty is implied.**

QR-FR+ · LOCAL QA / PENDING BINARY PUBLICATION
