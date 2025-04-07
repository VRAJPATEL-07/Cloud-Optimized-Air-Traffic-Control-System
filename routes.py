from app import app, socketio
from flask import render_template, jsonify, request
import requests
from app.flight_data import get_flight_data, fetch_real_time_flights, get_congestion_prediction, reroute_flight
from app.flight_simulator import simulate_flight_updates

# Serve the index page
@app.route('/')
def index():
    return render_template('index.html')

# API to fetch mock flight data
@app.route('/api/flight-data', methods=['GET'])
def flight_data():
    return jsonify(get_flight_data())

# API to fetch real-time flight data from OpenSky API
@app.route('/api/real-time-flight-data', methods=['GET'])
def real_time_flight_data():
    return jsonify(fetch_real_time_flights())

# API for congestion prediction
@app.route('/api/congestion-prediction', methods=['GET'])
def congestion_prediction():
    return jsonify(get_congestion_prediction())

# API for flight rerouting
@app.route('/api/reroute', methods=['POST'])
def reroute():
    return jsonify(reroute_flight(request))

# Handle client connections
@socketio.on('connect')
def handle_connect():
    print("Client connected!")

# Emit flight updates
@socketio.on('flight-update')
def handle_flight_update(data):
    print(f"Received flight update: {data}")
    socketio.emit('update-map', data)  # Broadcast the update to all connected clients
