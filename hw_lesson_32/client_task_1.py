import socket

HOST = "127.0.0.1"
PORT = 32332

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b"Hello, world", (HOST, PORT))
    packet = s.recvfrom(1024)
    message = packet[0]
    addr = packet[1]

print(f"Received {message!r}")