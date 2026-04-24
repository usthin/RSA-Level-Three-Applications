# app3_verifier.py

import socket
import json
from rsa_utils import verify

HOST = "127.0.0.1"
PORT = 5002

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Verifier waiting for Proxy...")

conn, addr = server.accept()
data = conn.recv(4096).decode()
conn.close()

received = json.loads(data)

message = received["message"]
signature = received["signature"]
public_key = tuple(received["public_key"])

print("\n--- Data Received ---")
print(received)

# --- VERIFY ---
is_valid = verify(message, signature, public_key)

print("\n--- VERIFICATION RESULT ---")
if is_valid:
    print("✅ Signature is VALID")
else:
    print("❌ Signature is INVALID (TAMPERED)")

server.close()