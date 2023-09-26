import socket
from threading import Thread

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def handle_conection(conn, addr):
    with conn:
        print (f"Connected by {addr}")
        while True:
            data = conn.recv(BUFFER_SIZE) #wait to read data until its available and recieve it until the buffer_size
            if not data:
                break
            print (data)
            conn.sendall(data)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        
        s.listen(2) # Allow backlog of up to 2 connections => queue [ waiting conni, waiting conn2 1
        while True:
            conn, addr = s.accept()
            thread = Thread(target= handle_conection, args=(conn, addr))
            thread.run()

if __name__ == "__main__":
    main()