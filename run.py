from app import app, socketio
from app.flight_simulator import start_simulation

# Start the flight simulator
start_simulation()

# Run the app
if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)
