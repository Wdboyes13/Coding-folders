import socket
import struct

def send(host, port, int1, int2, int3, text):
    # Create a connection to the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        
        # Pack the integers (16-digit values into 64-bit unsigned integers)
        int1_bytes = struct.pack('!Q', int1)  # 16-digit integer (Big Endian)
        int2_bytes = struct.pack('!Q', int2)
        int3_bytes = struct.pack('!Q', int3)

        
        # Convert the text to bytes and pad it to 500 bytes if necessary
        text_bytes = text.encode('utf-8', errors='ignore')
        text_length = len(text_bytes)
        text_bytes = text_bytes.ljust(500, b'\0')  # Pad with null bytes to ensure it's 500 bytes
        
        # Send the data in the custom protocol format
        s.send(int1_bytes + int2_bytes + int3_bytes + text_bytes)
        print(f"Sent data: int1={int1}, int2={int2}, text={text}, int3={int3}")

def receive(host, port):
    # Create a TCP socket to listen for incoming connections
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        
        print(f"Listening on {host}:{port}...")
        conn, addr = s.accept()
        with conn:
            print(f"Connection from {addr}")
            data = conn.recv(1024)  # Read the incoming data
            
            print(f"Received raw data: {data}")
            if len(data) < 24:  # Ensure that we have at least the 3 integers (24 bytes)
                print("Error: Received insufficient data.")
                return
            
            # Unpack the integers (3 * 8 bytes = 24 bytes)
            int1, int2, int3 = struct.unpack('!QQQ', data[:24])
            
            # Extract the text (up to 500 bytes after the integers)
            text_bytes = data[24:524].strip(b'\0')  # Strip null padding
            try:
                text = text_bytes.decode('utf-8')
            except UnicodeDecodeError:
                print("Error: Unable to decode the text.")
                text = None

            # Print the received values
            print(f"Received int1: {int1}")
            print(f"Received int2: {int2}")
            print(f"Received text: '{text}'")
            print(f"Received int3: {int3}")