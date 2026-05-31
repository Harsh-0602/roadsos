# RoadSoS Manual Testing Checklist

## Environment
- [ ] Open `./index.html` directly by double-click (no server)
- [ ] Optional: run `python app.py` and open `http://localhost:8080`

## Functional checks
- [ ] GPS allowed: click **Use My GPS** and verify nearby services appear
- [ ] GPS denied: deny permission and verify user-friendly error appears
- [ ] Manual city search (known): search `Ahmedabad` (or another known city) and verify sorted results
- [ ] Manual city search (unknown): search unknown city and verify fallback/nice error behavior
- [ ] Filter tabs: switch all service filters and verify category-specific results
- [ ] Golden Hour Mode: verify top 3 nearest trauma centres, ambulances, and police are shown
- [ ] Share My Location: verify copy message includes lat/lon, city+country, OSM and Google Maps links
- [ ] Share fallback: in non-secure context, verify prompt fallback appears for manual copy

## UX and quality checks
- [ ] Offline behavior: disable internet and verify app still loads embedded services and national contacts
- [ ] Mobile responsiveness: test narrow viewport and verify controls/cards remain usable
- [ ] Browser console: verify no runtime JavaScript errors during core flows
