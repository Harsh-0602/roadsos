# RoadSoS - Emergency Road Safety Assistant

Submission-ready build for **Road Safety Hackathon 2026 (RoadSoS)**.

## Final entrypoint (canonical build)
- ✅ Open `/tmp/workspace/Harsh-0602/roadsos/index.html` directly (double-click supported, no server required)
- ✅ Structured database export: `/tmp/workspace/Harsh-0602/roadsos/data/services.json`
- ✅ Schema doc: `/tmp/workspace/Harsh-0602/roadsos/data/schema.md`
- ✅ Data credibility doc: `/tmp/workspace/Harsh-0602/roadsos/DATA_SOURCES.md`

## Archived build artifacts
- Previous duplicate build folder is archived at:
  - `/tmp/workspace/Harsh-0602/roadsos/archive/roadsos_final/`
- Use only root `index.html` for final submission/demo.

## Features
- Embedded emergency services database for offline-friendly `file://` use
- Manual city search + GPS detection
- Distance-based nearest sorting
- Service filters (trauma centre, hospital, ambulance, police, towing, emergency)
- **Golden Hour Mode**: top 3 nearest trauma centres, ambulances, and police
- **Share My Location**: copy-ready emergency message with coordinates + map links
- OpenStreetMap map links (no paid APIs)

## Running options
### Option 1 (recommended): No server
Double-click `index.html`.

### Option 2 (optional): Local Python server
`app.py` is optional and only for local serving/testing convenience.

```bash
python app.py
# open http://localhost:8080/index.html
```

> Front-end emergency lookup works from the embedded dataset in `index.html` and does not require backend APIs.

## Validation / Testing
See `/tmp/workspace/Harsh-0602/roadsos/TESTING.md` for full manual checklist.
