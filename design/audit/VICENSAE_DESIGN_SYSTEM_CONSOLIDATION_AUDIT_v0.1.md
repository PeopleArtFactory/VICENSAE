# VICENSAE Design System — Consolidation Audit v0.1

Date: 2026-11-08. Target: PeopleArtFactory/VICENSAE. Status: AUDIT_ONLY / DESIGN_ONLY. No constitutive assertion. Canonical branch checked: main at 2b45c4b5b5487d8145417f729c5ae8a5a99e1212.

## Evidence inventory (verified directly in GitHub)
- VICENSAE/main contains design/v1.0 (README, DESIGN_MANUAL, CSS/JSON tokens, components, SvelteKit instructions, browser preview, legal provenance templates) and **no installable original VICENSAE font**. 12 files overall in the repository.
- QSONGS/main contains a React web app and minimal style.css; the richer design system exists on branch feat/qsong-design-system-v0.1-20261106, not on main. Source includes packages/design-system/tokens.json, generated CSS, component CSS, state mapper, tests, token generator, and docs. Do not claim merged.
- paf4-monorepo/main packages/ui/src/tokens.css defines a third standalone theme and index.ts is only uiMeta. No complete shared component package.
- Fiduciary-Computation/main docs/style.css defines light scientific/editorial styling.
- COIIRM-hub-Lab/main is README only; no approved visual implementation verified.
- Local user-supplied vicens_protocol_typography_suite.html is a visual experiment using Cinzel + JetBrains Mono, with gold, lapidary SVG, tracking, patina, UI shell and tabs. Its Proof of Honor verifier declares success without cryptographic verification; exportAEO uses Math.random rather than secure digest. **Never deploy without explicitly marking as DEMO.**
- Library contains QSONG_DESIGN_SYSTEM_v0.1_PREVIEW.html, QSONG_SWARM_DESIGN_SYSTEM_v0.1_SOURCE.json, VICENSAE_SOFTWARE_TREE_ARCHITECTURE_v0.1.md, poster/handbook artwork. These are historical evidence, not automatically canonical code.

## Pre-existing design decisions from prior conversations (subject to source reconciliation)
- ADR-0003: IBM Plex Sans for interface, Plex Mono for proof/IDs, Plex Serif for constitutional/editorial typography; SPEC-0003 L3 Surface, L2 Operation, L0 Canon, optional Proof. Restore decision log instead of silently overwriting with new Sans/Display names.
- New proposal: original VICENSAE UI + VICENSAE Display + VICENSAE Mono, inspired by Inter, Raleway, Plex, not yet actual glyph outlines. Glyph-first proof for V A E R S Æ plus accents, figures, tabular numbers.
- Green PAF has been designated an accent in PAF-specific work; current palettes disagree. Distinguish core semantic color from product brand accent and status colors.
- Respect the official wordmark master: do not reconstruct an existing logo simply by changing font; ASCII VICENSAE in paths; VICENSÆ in display.
- Design is not an admission kernel: local digest equality does not prove creator authority, rights, eIDAS accreditation, legal admission, or long-term continuity.

## Gaps and recommended work priority
P0: Formal provenance and non-fabrication gate; no fabricated hash, genesis number, ACTIVE MAINNET or VERIFIED by default; represent UNKNOWN/DEMO, MISMATCH, INVALID_STRUCTURE, UNSUPPORTED_PROFILE, DEGRADED, WITHHOLD and FULL_FOR_PROFILE semantically. Preserve source domain state, never map arbitrary input to success.
P0: Reconcile tokens/themes (global primitives -> semantics -> product overrides) and document source-of-truth. Existing v1.0 frozen. Build vNext in new directory; no destructive replacement.
P0: Accessibility: keyboard navigation, focus, contrast audits, status text independent of color, motion reduction, screen reader announcements, 44px targets, mobile layouts.
P1: Typography roadmap with upstream license proofs, provenance, Reserved Font Names, version/sha and explicit IBM Plex source; no imaginary WOFF2/OTF/TTF. Font license not automatically PSL/VPPL.
P1: Framework-neutral primitives (CSS/HTML/ARIA) and adapters for SvelteKit, React and static docs; no copying state/domain logic.
P1: QSONG revelation/audio design contract: image independent/zoomable; initial 45% visible and 55% protected; protect tiles server-side; readable/copied acquired text, guide appended after revealed text; terrestrial/monotonic billing separated from fiduciary clock and backend-authorized.
P1: Shared verification panels: labels for id_D, profile, evidence, digest, signatures, lineage, authority, custody, last check; demo vs production separated.
P2: Storybook-like offline gallery, snapshots, a11y CI, token generation and checks, distribution package, docs, standard icons, UX of errors/empty/loading/offline, RTL and multilingual tests as requirements emerge.

## Proposed source tree (proposed, NOT existing)
design/v1.1/
  README.md
  decisions/ADR-0003-reconciliation.md
  tokens/{core.json,semantic.json,products.json}
  src/{tokens.css,components.css,status.css}
  typography/{SPEC.md,GLYPHS.md,PROVENANCE.json}
  patterns/{verification.md,revelation.md,earth-meter.md}
  adapters/{sveltekit.md,react.md,static.md}
  preview/index.html
  legal/{THIRD_PARTY_NOTICE.md,LICENSE_MATRIX.md}
  tests/{acceptance.md}
  audit/{INVENTORY_2026-11-08.md}

## Handoff rules
1. Preserve design/v1.0 unchanged; stage changes on a dedicated branch and draft PR.
2. One source of token truth; generated CSS checked in CI.
3. Public previews are marked DEMO; no privileged keys, private assets or data.
4. State presentation never grants admission. Authentication, witness, custody, admission and execution remain separate.
5. No unverified license claim and no unverified long-term 40-year guarantee.
6. Versioned canonical files and provenance with SHA256 hashes for future releases; README and docs end QR-F/QR-FR+.

QR-FR+ · AUDIT ONLY · PRODUCTION WITHHOLD
