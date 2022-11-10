"""
Task 2

Echo server with threading

Create a socket echo server which handles each connection in a separate Thread
"""
import socket
from concurrent.futures import ThreadPoolExecutor


class ThreadServer:
    def __init__(self, port, host):
        self._port = port
        self._host = host
        self.__clients = []

    def serve_client(self, conn, addr):
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    self.__clients.__delitem__(conn)
                    break
                conn.sendall(data)

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self._host, self._port))
            s.listen(1)
            with ThreadPoolExecutor() as executor:
                while True:
                    conn, addr = s.accept()
                    self.__clients.append(executor.submit(self.serve_client, conn, addr))
                    print(f"Connected from [{addr}]")


if __name__ == "__main__":
    ThreadServer(32332, "127.0.0.1").run()
