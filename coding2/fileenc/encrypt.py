from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64

# Generate AES Key (256-bit) and Nonce (12 bytes for GCM)
key = os.urandom(32)
nonce = os.urandom(12)

# Print the key in Base64 format
key_b64 = base64.b64encode(key).decode()
print("AES Key (Base64):", key_b64)

def encrypt_png(input_path, output_path, key, nonce):
    with open(input_path, "rb") as f:
        data = f.read()

    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data) + encryptor.finalize()

    # Save the nonce + encrypted data (GCM doesn't need padding)
    with open(output_path, "wb") as f:
        f.write(nonce + encryptor.tag + encrypted_data)

    print("Encryption complete. File saved as", output_path)

encrypt_png("911.tar.gz", "encr911memes.aes", key, nonce)
