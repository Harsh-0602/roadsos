# RoadSoS Services Data Schema

`data/services.json` stores the structured emergency service directory used for submission documentation.

| Field | Type | Description |
|---|---|---|
| `name` | string | Service name shown to users. |
| `type` | string | Category (`trauma_centre`, `hospital`, `ambulance`, `police`, `towing`, `emergency`, `fire`). |
| `phone` | string | Primary phone number for contact/call actions. |
| `address` | string | Street/locality or national coverage label. |
| `city` | string | Service city, `All India`, or `All Cities` for country/national entries. |
| `state` | string | State/province or `All States` for national entries. |
| `country` | string | Country name used for country filter. |
| `lat` | number | Latitude coordinate used for distance sorting/map links. |
| `lon` | number | Longitude coordinate used for distance sorting/map links. |
| `available_24x7` | boolean | Whether service is available 24x7 (`true`/`false`). |
| `trauma_level` | string \| null | Trauma capability label where available (e.g., `Level 1`). |
| `source_type` | string | Attribution class (`national_emergency_directory` or `curated_public_directory`). |
| `last_verified` | string (YYYY-MM-DD) | Last verification date for the record, policy-aligned to January 2026. |
