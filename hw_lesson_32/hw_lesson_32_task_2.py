import socket
from caesar import Caesar


HOST = "127.0.0.1"
PORT = 32332


if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        shift = conn.recv(1)
        caesar = Caesar(int(shift.decode("utf8")))
        conn.send(shift)
        with conn:
            print(f"Connected by {addr}")
            while True:
                message = caesar.decrypt(conn.recv(1024).decode('utf8'))
                print(f"Received message: {caesar.decrypt(message)}")
                message += f" was decrypted by server {(HOST, PORT)} with shift {shift}"
                if not message:
                    break
                conn.sendall(bytes(caesar.encrypt(message), "utf8"))
