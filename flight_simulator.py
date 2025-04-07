import time
from threading import Thread
from app import socketio

def simulate_flight_updates():
    while True:
        time.sleep(5)  # Simulate data every 5 seconds
        flight_data = {
            'flight_id': 'AI123',
            'latitude': 40.7128,
            'longitude': -74.0060,
            'status': 'On Time'
        }
        socketio.emit('update-map', flight_data)

# Start the simulation in a separate thread
def start_simulation():
    thread = Thread(target=simulate_flight_updates)
    thread.daemon = True
    thread.start()
