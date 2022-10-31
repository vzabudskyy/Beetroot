"""
Task 1

During the lesson, we have created a server and client,
which use TCP/IP protocol for communication via sockets.
In this task, you have to create a server and client,
which will use user datagram protocol (UDP) for communication.
"""

import socket

HOST = "127.0.0.1"
PORT = 32332

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    while True:
        packet = s.recvfrom(1024)
        message = packet[0]
        addr = packet[1]
        print(f"Connected by {addr}")
        s.sendto(message, addr)
