# app1_sender.py

import socket
import json
from rsa_utils import generate_keys, sign

HOST = "127.0.0.1"
PORT = 5001  # connects to proxy

public_key, private_key = generate_keys()

message = input("Enter message to sign: ")

signature = sign(message, private_key)

data = {
    "message": message,
    "signature": signature,
    "public_key": public_key
}

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.send(json.dumps(data).encode())

print("\nData sent to Proxy:")
print(data)

client.close()