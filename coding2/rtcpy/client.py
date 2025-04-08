import socketio
import sys

un = input("Enter a username: ")

sio = socketio.Client()

# Connect to the server
def connect_to_server(client_name):
    sio.connect('http://localhost:8765')

    # Join a room
    room = input("Enter the room name to join: ")
    sio.emit('join_room', room)  # Emit event to join room

    print(f"Joined room: {room}")

    while True:
        message = input(f"{client_name}: ")
        msg = f"{un}: {message}"
        sio.emit('send_message', {'room': room, 'message': msg})  # Send message to specific room

# Event for handling messages from the server
@sio.event
def message(data):
    print(f"Received from server: {data}")

# Event for when client connects
@sio.event
def connect():
    print("Connected to server")

# Event for when client disconnects
@sio.event
def disconnect():
    print("Disconnected from server")

if __name__ == "__main__":
    client_name = sys.argv[1] if len(sys.argv) > 1 else "Client"
    connect_to_server(client_name)
