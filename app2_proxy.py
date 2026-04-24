# app2_proxy.py

import socket
import json

HOST = "127.0.0.1"
PORT_RECEIVE = 5001
PORT_FORWARD = 5002

# --- RECEIVE FROM APP1 ---
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT_RECEIVE))
server.listen(1)

print("Proxy waiting for App1...")

conn, addr = server.accept()
data = conn.recv(4096).decode()
conn.close()

received = json.loads(data)

print("\n--- Data Received from Sender ---")
print(received)

# --- TAMPER ---
choice = input("\nModify signature? (y/n): ")

if choice.lower() == 'y':
    new_sig = int(input("Enter new fake signature: "))
    received["signature"] = new_sig
    print("Signature modified!")

# --- FORWARD TO APP3 ---
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT_FORWARD))

client.send(json.dumps(received).encode())

print("\nData forwarded to Verifier.")

client.close()
server.close()