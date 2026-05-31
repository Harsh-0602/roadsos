# RoadSoS Data Sources & Credibility Notes

## Data sourcing approach
- The emergency services dataset is curated from public emergency helplines and commonly listed city-level trauma/hospital/police/ambulance records.
- National-level emergency numbers (for India and supported countries) are included as fallback entries.
- The app is designed for fast hackathon-use discovery with location-based sorting.

## Verification policy
- Keep a rolling verification log for each release.
- Recommended policy: verify phone numbers and key addresses at least once every 90 days.
- For future updates, add per-entry metadata fields like `source_url` and `last_verified` in the structured JSON.

## Emergency disclaimer
- In a life-threatening emergency, always use official national emergency numbers first (for example: India 112/108/100).
- This database is best-effort and may contain stale or changed records.
- Users should confirm critical details with official channels before action whenever possible.
