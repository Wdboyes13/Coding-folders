import socketio

# Create a Socket.IO client
sio = socketio.Client()

# Event handler for when a message is received from the server
@sio.event
def message(data):
    print(f"Message from Discord: {data}")

# Function to connect to the Socket.IO server
def connect_to_socketio():
    sio.connect("http://localhost:8765")  # Connect to the server

    while True:
        message = input("You (Terminal): ")
        if message.lower() == "exit":
            break
        # Send message to the Socket.IO server
        sio.send(message)

# Connect and start interacting
if __name__ == "__main__":
    connect_to_socketio()
