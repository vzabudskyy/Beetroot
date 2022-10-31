import socket
from caesar import Caesar


HOST = "127.0.0.1"
PORT = 32332

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    shift = None
    while shift is None :
        s.send(bytes("7", "utf8"))
        response = s.recv(1).decode("utf8")
        if int(response):
            shift = int(response)
    caesar = Caesar(shift)
    message = caesar.encrypt("Hello, world")
    s.sendall(bytes(message, "utf8"))
    data = s.recv(1024)

print(f"Received {caesar.decrypt(data.decode('utf8'))}")
