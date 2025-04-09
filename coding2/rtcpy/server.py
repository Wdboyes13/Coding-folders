import socketio
from flask import Flask, render_template
import os

# Create a Flask app and Socket.IO instance
app = Flask(__name__)
sio = socketio.Server()

# Attach Socket.IO to Flask
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

# Serve the HTML file
@app.route('/')
def index():
    return render_template('index.html')  # Make sure index.html is in the templates folder

# Event for when a client connects
@sio.event
def connect(sid, environ):
    print(f"Client {sid} connected")

# Event for when a client disconnects
@sio.event
def disconnect(sid):
    print(f"Client {sid} disconnected")

# Event to handle joining rooms
@sio.event
def join_room(sid, room):
    sio.enter_room(sid, room)  # Join the specified room
    sio.emit('message', f"{sid} has entered the room {room}", room=room)

# Event to handle sending messages to a specific room
@sio.event
def send_message(sid, data):
    room = data['room']
    message = data['message']
    sio.emit('message', message, room=room)  # Send the message to the room

if __name__ == '__main__':
    # Ensure your templates directory is set up correctly
    app.run(port=8765)
