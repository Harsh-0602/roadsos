from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import sqlite3
import urllib.parse
import urllib.request
import os

DB_PATH = "roadsos.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS emergency_services (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        type TEXT NOT NULL,
        phone TEXT,
        address TEXT,
        city TEXT,
        state TEXT,
        country TEXT DEFAULT 'India',
        lat REAL,
        lon REAL,
        available_24x7 INTEGER DEFAULT 1,
        trauma_level TEXT
    )''')

    # Seed data - India + Global
    services = [
        # India - National Emergency Numbers
        ("National Emergency", "emergency", "112", "All India", "All Cities", "All States", "India", 20.5937, 78.9629, 1, None),
        ("Ambulance India", "ambulance", "108", "All India", "All Cities", "All States", "India", 20.5937, 78.9629, 1, None),
        ("Police India", "police", "100", "All India", "All Cities", "All States", "India", 20.5937, 78.9629, 1, None),
        ("Fire Brigade India", "fire", "101", "All India", "All Cities", "All States", "India", 20.5937, 78.9629, 1, None),
        ("Road Accident Emergency", "emergency", "1073", "NHAI Helpline", "All Cities", "All States", "India", 20.5937, 78.9629, 1, None),

        # Delhi
        ("AIIMS Trauma Centre", "trauma_centre", "011-26588500", "Ansari Nagar, New Delhi", "New Delhi", "Delhi", "India", 28.5672, 77.2100, 1, "Level 1"),
        ("Safdarjung Hospital", "hospital", "011-26730000", "Safdarjung, New Delhi", "New Delhi", "Delhi", "India", 28.5678, 77.2070, 1, "Level 1"),
        ("Delhi Police HQ", "police", "011-23490000", "ITO, New Delhi", "New Delhi", "Delhi", "India", 28.6286, 77.2395, 1, None),
        ("Delhi Ambulance", "ambulance", "102", "New Delhi", "New Delhi", "Delhi", "India", 28.6139, 77.2090, 1, None),
        ("Ram Manohar Lohia Hospital", "hospital", "011-23404000", "Baba Kharak Singh Marg", "New Delhi", "Delhi", "India", 28.6270, 77.2017, 1, "Level 2"),

        # Mumbai
        ("KEM Hospital", "trauma_centre", "022-24107000", "Acharya Donde Marg, Parel", "Mumbai", "Maharashtra", "India", 18.9937, 72.8407, 1, "Level 1"),
        ("Nair Hospital", "hospital", "022-23027600", "Dr A.L. Nair Rd, Mumbai Central", "Mumbai", "Maharashtra", "India", 18.9716, 72.8192, 1, "Level 1"),
        ("Mumbai Police Control", "police", "022-22621855", "Crawford Market", "Mumbai", "Maharashtra", "India", 18.9479, 72.8346, 1, None),
        ("Mumbai Ambulance", "ambulance", "108", "Mumbai", "Mumbai", "Maharashtra", "India", 19.0760, 72.8777, 1, None),
        ("Towing Service Mumbai", "towing", "1800-22-1406", "Mumbai", "Mumbai", "Maharashtra", "India", 19.0760, 72.8777, 1, None),

        # Bangalore
        ("Victoria Hospital", "trauma_centre", "080-26701150", "Fort Rd, Bangalore", "Bangalore", "Karnataka", "India", 12.9641, 77.5784, 1, "Level 1"),
        ("Bangalore Medical College", "hospital", "080-26703200", "Fort Road", "Bangalore", "Karnataka", "India", 12.9634, 77.5781, 1, "Level 2"),
        ("Bangalore Police Control", "police", "080-22942222", "Infantry Road", "Bangalore", "Karnataka", "India", 12.9785, 77.5985, 1, None),
        ("Bangalore CATS Ambulance", "ambulance", "108", "Bangalore", "Bangalore", "Karnataka", "India", 12.9716, 77.5946, 1, None),
        ("Bangalore Towing", "towing", "080-22868686", "Bangalore", "Bangalore", "Karnataka", "India", 12.9716, 77.5946, 1, None),

        # Chennai
        ("Rajiv Gandhi Government Hospital", "trauma_centre", "044-25305000", "Park Town, Chennai", "Chennai", "Tamil Nadu", "India", 13.0843, 80.2784, 1, "Level 1"),
        ("Stanley Medical College", "hospital", "044-25281330", "Old Jail Road", "Chennai", "Tamil Nadu", "India", 13.1076, 80.2891, 1, "Level 2"),
        ("Chennai Police Control", "police", "044-28447777", "Vepery", "Chennai", "Tamil Nadu", "India", 13.0860, 80.2707, 1, None),
        ("Chennai Ambulance 108", "ambulance", "108", "Chennai", "Chennai", "Tamil Nadu", "India", 13.0827, 80.2707, 1, None),

        # Hyderabad
        ("Osmania General Hospital", "trauma_centre", "040-24600128", "Afzalgunj", "Hyderabad", "Telangana", "India", 17.3794, 78.4718, 1, "Level 1"),
        ("Gandhi Hospital", "hospital", "040-23267926", "Musheerabad", "Hyderabad", "Telangana", "India", 17.4170, 78.4869, 1, "Level 1"),
        ("Hyderabad Police Control", "police", "040-27852323", "Hyderabad", "Hyderabad", "Telangana", "India", 17.3850, 78.4867, 1, None),
        ("Hyderabad Ambulance", "ambulance", "108", "Hyderabad", "Hyderabad", "Telangana", "India", 17.3850, 78.4867, 1, None),

        # Ahmedabad
        ("Civil Hospital Ahmedabad", "trauma_centre", "079-22681060", "Asarwa, Ahmedabad", "Ahmedabad", "Gujarat", "India", 23.0549, 72.6091, 1, "Level 1"),
        ("LG Hospital", "hospital", "079-22682400", "Maninagar", "Ahmedabad", "Gujarat", "India", 23.0042, 72.6000, 1, "Level 2"),
        ("Ahmedabad Police Control", "police", "079-25630100", "Shahibaug", "Ahmedabad", "Gujarat", "India", 23.0618, 72.6025, 1, None),
        ("Ahmedabad Ambulance 108", "ambulance", "108", "Ahmedabad", "Ahmedabad", "Gujarat", "India", 23.0225, 72.5714, 1, None),
        ("Ahmedabad Towing GVK", "towing", "079-26444444", "Ahmedabad", "Ahmedabad", "Gujarat", "India", 23.0225, 72.5714, 1, None),

        # Pune
        ("Sassoon General Hospital", "trauma_centre", "020-26128000", "Pune Station", "Pune", "Maharashtra", "India", 18.5184, 73.8676, 1, "Level 1"),
        ("Pune Police Control", "police", "020-26123456", "Shivajinagar", "Pune", "Maharashtra", "India", 18.5308, 73.8474, 1, None),
        ("Pune Ambulance", "ambulance", "108", "Pune", "Pune", "Maharashtra", "India", 18.5204, 73.8567, 1, None),

        # Kolkata
        ("SSKM Hospital", "trauma_centre", "033-22041818", "AJC Bose Road", "Kolkata", "West Bengal", "India", 22.5372, 88.3399, 1, "Level 1"),
        ("Kolkata Police Control", "police", "033-22143000", "Lalbazar", "Kolkata", "West Bengal", "India", 22.5688, 88.3702, 1, None),
        ("Kolkata Ambulance", "ambulance", "108", "Kolkata", "Kolkata", "West Bengal", "India", 22.5726, 88.3639, 1, None),

        # Global - USA
        ("Emergency USA", "emergency", "911", "United States", "All Cities", "All States", "USA", 37.0902, -95.7129, 1, None),
        ("Poison Control USA", "emergency", "1-800-222-1222", "United States", "All Cities", "All States", "USA", 37.0902, -95.7129, 1, None),

        # Global - UK
        ("Emergency UK", "emergency", "999", "United Kingdom", "All Cities", "All States", "UK", 55.3781, -3.4360, 1, None),
        ("NHS Non-Emergency UK", "hospital", "111", "United Kingdom", "All Cities", "All States", "UK", 55.3781, -3.4360, 1, None),

        # Global - Australia
        ("Emergency Australia", "emergency", "000", "Australia", "All Cities", "All States", "Australia", -25.2744, 133.7751, 1, None),

        # Global - UAE
        ("Emergency UAE", "emergency", "999", "UAE", "All Cities", "All States", "UAE", 23.4241, 53.8478, 1, None),
        ("Ambulance UAE", "ambulance", "998", "UAE", "All Cities", "All States", "UAE", 23.4241, 53.8478, 1, None),

        # Global - Canada
        ("Emergency Canada", "emergency", "911", "Canada", "All Cities", "All States", "Canada", 56.1304, -106.3468, 1, None),

        # Global - Germany
        ("Emergency Germany", "emergency", "112", "Germany", "All Cities", "All States", "Germany", 51.1657, 10.4515, 1, None),
        ("Police Germany", "police", "110", "Germany", "All Cities", "All States", "Germany", 51.1657, 10.4515, 1, None),
    ]

    c.executemany('''INSERT OR IGNORE INTO emergency_services
        (name, type, phone, address, city, state, country, lat, lon, available_24x7, trauma_level)
        VALUES (?,?,?,?,?,?,?,?,?,?,?)''', services)

    conn.commit()
    conn.close()
    print(f"Database initialized with {len(services)} services.")

def get_nearby_services(lat, lon, radius_km=50, service_type=None, country=None):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    query = '''SELECT *, (
        6371 * acos(
            cos(radians(?)) * cos(radians(lat)) *
            cos(radians(lon) - radians(?)) +
            sin(radians(?)) * sin(radians(lat))
        )
    ) AS distance_km
    FROM emergency_services
    WHERE lat IS NOT NULL AND lon IS NOT NULL'''

    params = [lat, lon, lat]

    if service_type and service_type != "all":
        query += " AND type = ?"
        params.append(service_type)

    if country:
        query += " AND (country = ? OR city = 'All Cities')"
        params.append(country)

    query += " ORDER BY distance_km ASC LIMIT 20"

    c.execute(query, params)
    rows = c.fetchall()
    conn.close()

    cols = ["id","name","type","phone","address","city","state","country","lat","lon","available_24x7","trauma_level","distance_km"]
    results = []
    for row in rows:
        d = dict(zip(cols, row))
        d["distance_km"] = round(d["distance_km"], 1)
        results.append(d)
    return results

def get_all_services():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM emergency_services ORDER BY country, city, type")
    rows = c.fetchall()
    conn.close()
    cols = ["id","name","type","phone","address","city","state","country","lat","lon","available_24x7","trauma_level"]
    return [dict(zip(cols, row)) for row in rows]

class RoadSoSHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)

        if parsed.path == "/":
            self.serve_file("index.html", "text/html")
        elif parsed.path == "/api/nearby":
            params = urllib.parse.parse_qs(parsed.query)
            try:
                lat = float(params.get("lat", [0])[0])
                lon = float(params.get("lon", [0])[0])
                stype = params.get("type", ["all"])[0]
                country = params.get("country", [None])[0]
                results = get_nearby_services(lat, lon, service_type=stype, country=country)
                self.send_json({"success": True, "data": results, "count": len(results)})
            except Exception as e:
                self.send_json({"success": False, "error": str(e)})
        elif parsed.path == "/api/all":
            results = get_all_services()
            self.send_json({"success": True, "data": results})
        elif parsed.path == "/api/emergency_numbers":
            params = urllib.parse.parse_qs(parsed.query)
            country = params.get("country", ["India"])[0]
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            c.execute("SELECT * FROM emergency_services WHERE city='All Cities' AND country=?", (country,))
            rows = c.fetchall()
            conn.close()
            cols = ["id","name","type","phone","address","city","state","country","lat","lon","available_24x7","trauma_level"]
            self.send_json({"success": True, "data": [dict(zip(cols, r)) for r in rows]})
        else:
            self.send_error(404)

    def serve_file(self, filename, content_type):
        try:
            with open(filename, "rb") as f:
                content = f.read()
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", len(content))
            self.end_headers()
            self.wfile.write(content)
        except FileNotFoundError:
            self.send_error(404)

    def send_json(self, data):
        content = json.dumps(data).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", len(content))
        self.end_headers()
        self.wfile.write(content)

    def log_message(self, format, *args):
        pass

if __name__ == "__main__":
    # This is optional. index.html works standalone.
    init_db()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server = HTTPServer(("0.0.0.0", 8080), RoadSoSHandler)
    print("RoadSoS server running at http://localhost:8080")
    server.serve_forever()
