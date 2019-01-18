#!/usr/bin/env python3
import socket
import time

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SOREUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)

            full_data = b""
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data: break
                full_data += data
                conn.send(data)

            time.sleep(0.5)
            conn.sendall(full_data)
            conn.close()


if __name__ == "__main__":
    main()