# Build status — compatibility candidate

The original renamed Windows build passed CI on 2026-10-18, but showed a white, unresponsive window on Intel HD 4400 with driver 20.19.15.5171. Its log selected Microsoft Basic Render Driver, timed out during effect-card rendering and reported device loss.

This candidate uses the software UI renderer when Windows exposes only a software GPU (or MUSK_LE_COMPATIBILITY=1). It does not share GPU textures with that UI and defers generation of missing effect thumbnails. Existing thumbnails, effect packages and editing/export commands remain present. Video rendering on this hardware may still be slow or fail; an end-to-end video export on the user's PC is not yet verified.

CI adds a fresh-settings GUI event-loop test with a 10-second heartbeat and a 120-second timeout, in addition to Defender and existing startup checks. Read the specific workflow result before claiming this candidate passed. Passing these checks is not a malware-free guarantee or full editing/export verification.
