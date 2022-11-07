import socket
from time import sleep
from concurrent.futures import ThreadPoolExecutor


HOST = "127.0.0.1"
PORT = 32332


class TestClient:
    def __init__(self, host, port):
        self._host = host
        self._port = port

    def echo_to_server(self, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self._host, self._port))
            while True:
                s.send(message.encode())
                received = s.recv(1024)
                print(f"Received {received!r}")
                sleep(1)

    def run(self):
        with ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(self.echo_to_server, "Hello world from client thread 1")
            executor.submit(self.echo_to_server, "Hello world from client thread 2")


if __name__ == "__main__":
    TestClient(HOST, PORT).run()
