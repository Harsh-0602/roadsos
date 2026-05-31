# RoadSoS Services Schema

`data/services.json` contains an array of service objects.

| Field | Type | Description |
|---|---|---|
| `name` | string | Service provider name |
| `type` | string | Category (`trauma_centre`, `hospital`, `ambulance`, `police`, `towing`, `emergency`, `fire`) |
| `phone` | string | Primary emergency/service contact number |
| `address` | string | Service address or area description |
| `city` | string | Service city (`All India`/`All Cities` for national contacts) |
| `state` | string | State/region name (`All States` if national) |
| `country` | string | Country name |
| `lat` | number | Latitude in decimal degrees |
| `lon` | number | Longitude in decimal degrees |
| `available_24x7` | number | Availability flag (`1` = available 24x7) |
| `trauma_level` | string \| null | Trauma capability level when applicable |

Notes:
- `index.html` keeps the same embedded dataset for `file://` offline use.
- `data/services.json` is provided for structured database submission compliance.
