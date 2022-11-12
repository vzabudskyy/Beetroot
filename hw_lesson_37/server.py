from concurrent.futures import ThreadPoolExecutor
import socket
from typing import Dict


HOST = '127.0.0.1'  # Standard loop-back interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


class Server:
    def __init__(self, port, host):
        self._port = port
        self._host = host
        self.__clients: Dict[socket.socket, str] = {}

    def broadcast(self, msg, current_conn = None):
        for client in self.__clients.keys():
            if current_conn is None or client != current_conn:
                client.sendall(msg.encode())

    def change_client_name(self, data, conn):
        new_name = data[12:].strip()
        msg = f'{self.__clients[conn]} has new name {new_name}'
        self.__clients[conn] = new_name
        return msg

    def serving_client(self, conn):
        with conn:
            print('Connected by', self.__clients[conn])
            while True:
                data = conn.recv(1024).decode()
                if data == '!exit':
                    break
                elif data[:12] == "!change-name":
                    msg = self.change_client_name(data, conn)
                else:
                    msg = f'{self.__clients[conn]}: {data}'
                self.broadcast(msg, conn)

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((HOST, PORT))
            s.listen(1)
            futures = []
            try:
                with ThreadPoolExecutor() as executor:
                    while True:
                        conn, addr = s.accept()
                        name = conn.recv(1024).decode()
                        self.__clients[conn] = name
                        futures.append(executor.submit(self.serving_client, conn))
            except KeyboardInterrupt:
                self.broadcast('server closed')
                print('server closed')


if __name__ == '__main__':
    Server(HOST, PORT).start()