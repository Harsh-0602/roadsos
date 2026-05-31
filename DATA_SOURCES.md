# RoadSoS Data Sources and Credibility

## Data sourcing methodology
- National emergency entries are sourced from widely published country-level emergency directories and official helpline references.
- City-level hospital, trauma centre, ambulance, police, and towing entries are curated from public service directories and publicly available institutional/contact pages.
- The app keeps an embedded dataset in `index.html` for offline and double-click operation, and provides a structured export in `data/services.json`.

## Last verified policy
- Baseline verification window: **January 2026**.
- `last_verified` is tracked per service record in `data/services.json`.
- Future updates should refresh high-priority emergency records first (national numbers, trauma centres, ambulance, police).

## Emergency disclaimer
- In life-threatening emergencies, **national emergency numbers are the primary fallback**.
- Local numbers can change; users should follow local authority instructions if any contact fails.

## Per-service source attribution guidance
- Use `source_type = national_emergency_directory` for country/national emergency records.
- Use `source_type = curated_public_directory` for city-level institutions and services.
- When updating records, keep source evidence in maintainer notes (official portal, institutional page, or trusted public directory) and refresh `last_verified`.
