import socket

#create a tcp socket
def create_tcp_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created successfully')
    return s

#get host information
def get_remote_ip(host):
    remote_ip = socket.gethostbyname( host )
    print (f'Ip address of {host} is {remote_ip}')
    return remote_ip

#send data to server
def send_data(serversocket, payload):
    serversocket.sendall(payload.encode())
    print("Payload sent successfully")

def main():
        #define address info, payload, and buffer size
        host = 'www.google.com'
        port = 80
        payload = f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'
        buffer_size = 4096

        #make the socket, get the ip, and connect
        s = create_tcp_socket()

        remote_ip = get_remote_ip(host)

        s.connect((remote_ip , port))
        print (f'Socket Connected to {host} on ip {remote_ip}')
        
        #send the data and shutdown
        send_data(s, payload)
        s.shutdown(socket.SHUT_WR)

        #continue accepting data until no more left
        full_data = b""
        while True:
            data = s.recv(buffer_size)
            if not data:
                 break
            full_data += data
        print(full_data)
        s.close()

if __name__ == "__main__":
    main()

