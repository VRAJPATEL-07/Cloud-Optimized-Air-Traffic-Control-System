import psycopg2
from flask import Flask, jsonify, request, render_template
import requests
import os

app = Flask(__name__)

# GCP PostgreSQL connection details
DB_HOST = os.getenv('34.47.236.87')  # Use the GCP instance host
DB_NAME = os.getenv('flightdb')
DB_USER = os.getenv('AirNav System')
DB_PASSWORD = os.getenv('OX-ajmODQZn%Ir~a')

# Connect to PostgreSQL
def connect_db():
    print("Starting connection attempt...")
    try:
        conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
        print("Connected to PostgreSQL successfully!")
        return conn
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

# Home route
@app.route('/')
def home():
    return render_template('index.html')  # Render the index.html from the templates folder

# API to fetch mock flight data
@app.route('/api/flight-data', methods=['GET'])
def get_flight_data():
    flights = [
        {"flight_id": "AI123", "status": "in-air", "location": "New York"},
        {"flight_id": "BA456", "status": "landed", "location": "London"},
        {"flight_id": "CA789", "status": "delayed", "location": "Beijing"}
    ]
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM flights;')
    flights = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(flights)

# API to fetch real-time flight data from OpenSky API
@app.route('/api/real-time-flight-data', methods=['GET'])
def fetch_real_time_flights():
    try:
        url = "https://console.cloud.google.com/apis/api/pubsub.googleapis.com/metrics?hl=en&project=organic-duality-445212-d3"
        response = requests.get(url)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": "Failed to fetch data from OpenSky API"}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API for congestion prediction (mock implementation)
@app.route('/api/congestion-prediction', methods=['GET'])
def get_congestion_prediction():
    predictions = {
        "areas": [
            {"region": "North America", "congestion_level": "High"},
            {"region": "Europe", "congestion_level": "Medium"},
            {"region": "Asia", "congestion_level": "Low"}
        ]
    }
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM congestion_prediction;')
    predictions = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(predictions)

# API for flight rerouting (mock implementation)
@app.route('/api/reroute', methods=['POST'])
def reroute_flight():
    try:
        data = request.get_json()
        flight_id = data.get("flight_id")
        new_route = data.get("new_route")
        if not flight_id or not new_route:
            return jsonify({"error": "Missing flight_id or new_route"}), 400
        conn = connect_db()
        cur = conn.cursor()
        cur.execute('INSERT INTO reroutes (flight_id, new_route) VALUES (%s, %s)', (flight_id, new_route))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"message": f"Flight {flight_id} successfully rerouted to {new_route}"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/contact', methods=['POST'])
def save_contact_info():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        message = data.get('message')

        if not name or not email or not phone:
            return jsonify({"error": "Missing required fields: name, email, or contact_message"}), 400
        
        # Here you could save the contact information to the database or send an email
        # For now, we'll just print it and return a success message.
        print(f"Contact Info received: Name: {name}, Email: {email}, Phone: {phone}, Message: {message}")
        
        conn = connect_db()
        cur = conn.cursor()
        cur.execute('INSERT INTO contacts (name, email, phone, message) VALUES (%s, %s, %s, %s)', 
                    (name, email, phone, message))
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({"message": "Contact information saved successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Favicon route to prevent 404 error
@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
