# RoadSoS Manual Testing Checklist

## 1) GPS permission granted
- **Steps:** Open `index.html` and click **Use My GPS**. Allow browser location permission.
- **Expected:** Success status appears, service cards are shown sorted by distance, filters appear, and Golden Hour Mode button becomes visible.

## 2) GPS permission denied
- **Steps:** Click **Use My GPS** and deny location access.
- **Expected:** Error status indicates GPS denial and app remains usable via city search.

## 3) City search (known city)
- **Steps:** Enter a known city (e.g., `Ahmedabad`) and click **Search Nearby Services**.
- **Expected:** Nearby services load with distance labels and filter tabs.

## 4) City search (unknown city)
- **Steps:** Enter an unknown city text and search.
- **Expected:** National/country emergency entries are shown as fallback with no JS errors.

## 5) Filter tabs
- **Steps:** After loading results, click each tab: trauma, ambulance, police, towing, emergency.
- **Expected:** Cards are filtered correctly and counts update without layout break.

## 6) Golden Hour Mode
- **Steps:** Load location via GPS or known city, then click **Golden Hour Mode**.
- **Expected:** Exactly nearest trauma centres, ambulances, and police are prioritized (up to 3 each), sorted by distance.

## 7) Share My Location
- **Steps:** On any card, click **Share My Location**.
- **Expected:** Clipboard receives text in format `Emergency at [lat,lon] [City, Country] - [OSM_link]`; fallback text selection/prompt appears if clipboard API is unavailable.

## 8) Offline mode
- **Steps:** Disconnect internet and open app from local file; search unknown city or use country fallback.
- **Expected:** National emergency numbers still appear because data is embedded in `index.html`.

## 9) Mobile responsiveness (375px)
- **Steps:** Open app in responsive mode at width `375px`.
- **Expected:** Buttons remain usable, cards stack cleanly, no clipped critical controls.

## 10) Console health
- **Steps:** Use all key flows above while observing browser console.
- **Expected:** Zero JavaScript runtime errors.
