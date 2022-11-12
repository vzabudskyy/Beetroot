from concurrent.futures import ThreadPoolExecutor
import socket


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server


class Client:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = input('Enter your name: ')
        self.help = """
                        !change-name <new name> - changes your name
                        !exit - leave from chatroom
                    """

    @staticmethod
    def sending(sock):
        while True:
            user_input = input('>')
            sock.sendall(user_input.encode())

    @staticmethod
    def receiving(sock):
        while True:
            data = sock.recv(1024).decode()
            if data == 'server closed':
                raise Exception
            print(f">{data}")

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            try:
                s.sendall(self._name.encode())
                with ThreadPoolExecutor(2) as executor:
                    executor.submit(self.sending, s)
                    executor.submit(self.receiving, s)
            except Exception:
                print('server closed')


if __name__ == '__main__':
    Client(HOST, PORT).start()
