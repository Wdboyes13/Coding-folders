import socketio

# Create a Socket.IO server
sio = socketio.Server()

# Create a WSGI application
app = socketio.WSGIApp(sio)

clients = set()

# Event handler when a client connects
@sio.event
def connect(sid, environ):
    print(f"Client {sid} connected")
    clients.add(sid)

# Event handler when a client sends a message (from terminal or Discord)
@sio.event
def message(sid, data):
    print(f"Received message from {sid}: {data}")
    # Broadcast message to all clients (except the sender)
    for client in clients:
        if client != sid:
            sio.send(client, data)

# Event handler when a client disconnects
@sio.event
def disconnect(sid):
    print(f"Client {sid} disconnected")
    clients.remove(sid)

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    # Run the server on localhost:8765
    server = make_server('localhost', 8765, app)
    print("Server started at http://localhost:8765")
    server.serve_forever()
