import socket

BUFFER_SIZE = 4096

def get (host, port):
    request = b"GET / HTTP/1.1\nHost: www.google.com\n\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.send(request)

        s.shutdown(socket.SHUT_WR)
        chunk = s.recv(BUFFER_SIZE)

        result = b'' + chunk

        while(len(chunk) > 0):
            chunk = s.recv(BUFFER_SIZE)
            result += chunk
        s.close ()
        return result

def main() :
    print(get ("127.0.0.1", 8080))

if __name__ == "__main__":
    main()