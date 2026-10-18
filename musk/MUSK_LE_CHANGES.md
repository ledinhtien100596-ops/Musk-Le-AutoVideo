# Musk Le AutoVideo — changes on 2026-10-18

Derived from Concat v0.2.7 by Jareer and Concat contributors. Original copyright, AGPL-3.0-or-later and third-party notices retained.

Only product branding, separate settings identity, default project-folder naming, installer identities and build packaging are changed. Timeline, effects, captions, speech, models, rendering and export implementation are retained. Internal crate names, API names and concat.json format stay compatible.

The native window title, About label, startup error label and Windows product metadata use Musk Le AutoVideo. All locales receive an attribution and an upstream-update notice. Installer names and installation identifiers differ from upstream; the executable is internally still concat.exe for build/smoke compatibility.

Upstream update/model endpoints remain upstream. The Version page explicitly states updates are Concat releases, not updates of this rebrand. There is no Musk Le update server. No new telemetry or network endpoint is introduced. The original logo remains; only the requested name is changed.

Only the manual Windows workflow is active. Original workflows are preserved in upstream-workflows/. No releases are published automatically. The build keeps the pinned upstream dependencies and adds a Defender scan gate before the Windows smoke tests. Availability of Defender and the entire workflow still require verification on a Windows runner.

## Compatibility candidate

On Windows software adapters, use a separate software UI renderer and defer uncached effect-card generation to avoid startup shader contention. Existing effects remain available. Add an opt-in GUI smoke test that enters the real event loop. Export performance and compatibility on Intel HD 4400 remain unverified.
