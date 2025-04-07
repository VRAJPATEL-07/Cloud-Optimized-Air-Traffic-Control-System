from flask import Flask
from flask_socketio import SocketIO

# Initialize Flask app
app = Flask(__name__)

# Initialize SocketIO
socketio = SocketIO(app, async_mode='eventlet')

# Import routes after app initialization to avoid circular import
from app import routes
