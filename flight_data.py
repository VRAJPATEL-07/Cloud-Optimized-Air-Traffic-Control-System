import requests

# Mock flight data
def get_flight_data():
    return [
        {"flight_id": "AI123", "status": "in-air", "location": "New York"},
        {"flight_id": "BA456", "status": "landed", "location": "London"},
        {"flight_id": "CA789", "status": "delayed", "location": "Beijing"}
    ]

# Fetch real-time flight data from OpenSky API
def fetch_real_time_flights():
    try:
        url = "https://opensky-network.org/api/states/all"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to fetch data from OpenSky API"}
    except Exception as e:
        return {"error": str(e)}
    
# Congestion prediction mock function
def get_congestion_prediction():
    return {
        "areas": [
            {"region": "North America", "congestion_level": "High"},
            {"region": "Europe", "congestion_level": "Medium"},
            {"region": "Asia", "congestion_level": "Low"}
        ]
    }

# Flight rerouting mock function
def reroute_flight(request):
    try:
        data = request.get_json()
        flight_id = data.get("flight_id")
        new_route = data.get("new_route")
        if not flight_id or not new_route:
            return {"error": "Missing flight_id or new_route"}, 400
        return {"message": f"Flight {flight_id} successfully rerouted to {new_route}"}, 200
    except Exception as e:
        return {"error": str(e)}, 500
