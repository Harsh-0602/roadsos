# RoadSoS - Emergency Services Finder

Production-ready RoadSoS submission package for Road Safety Hackathon 2026.

## Run Instructions

### Option 1 (primary): Direct offline use
1. Open `/tmp/workspace/Harsh-0602/roadsos/index.html` by double-clicking in a browser.
2. Use **Use My GPS** or city search.

### Option 2 (optional): Local Python server
```bash
cd /tmp/workspace/Harsh-0602/roadsos
python app.py
# open http://localhost:8080
```
> `app.py` is optional. `index.html` works standalone.

## What's Included
- Embedded emergency services DB in `index.html` (offline-friendly, double-click ready)
- 60 structured emergency service records in `data/services.json`
- GPS detection + city search + distance sorting
- Type filters: trauma, hospital, ambulance, police, towing, emergency
- Golden Hour Mode (nearest trauma + ambulance + police)
- Share My Location per service card (clipboard/fallback copy)
- OpenStreetMap quick map links

## Data and Documentation
- Structured DB export: `data/services.json`
- Data schema: `data/schema.md`
- Data credibility and verification policy: `DATA_SOURCES.md`
- Manual testing checklist: `TESTING.md`

## Submission Package Contents
- `index.html` (final frontend entry)
- `app.py` (optional local server)
- `data/services.json`
- `data/schema.md`
- `DATA_SOURCES.md`
- `TESTING.md`
- `README.md`
- `archive/roadsos_final/` (archived legacy copy; not submission entry)

## Testing
Use the manual checklist in [`TESTING.md`](./TESTING.md).
