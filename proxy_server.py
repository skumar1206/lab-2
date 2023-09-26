import socket
from threading import Thread

BUFFER_SIZE = 4096
PROXY_SERVER_HOST = "127.0.0.1"
PROXY_SERVER_PORT = 8080

# Send some data(request) to host:port
def send_request (host, port, request):
# Create a new socket in with block to ensure it's closed once we're done
    with socket. socket (socket .AF_INET, socket .SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.send(request)
        client_socket.shutdown(socket.SHUT_WR)
#wait to read data until its available and recieve it until the buffer_size
        data = client_socket.recv(BUFFER_SIZE)
        result = b'' + data
        while len (data) > 0: # Keep reading data until connection terminates
            data = client_socket.recv(BUFFER_SIZE)
            result += data
        return result
    
def handle_connection (conn, addr):
    with conn:
        print(f"Connected by {addr}")
        request = b''
        while True:
            data = conn.recv(BUFFER_SIZE) # read some data from the client socket
            if not data:
                break
            print(data) # otherwise, print the data to the screen
            request += data
        response = send_request("www.google.com", 80, request) # and send it as a request to www. google.com
        conn.sendall(response)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((PROXY_SERVER_HOST, PROXY_SERVER_PORT)) 
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        server_socket. listen(2) # Allow queuing of up to 2 connections
        while True:
            conn, addr = server_socket.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()

if __name__ == "__main__":
    main()