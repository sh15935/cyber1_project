import socket

def start_udp_client():
    host = '127.0.0.1'
    port = 5001

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = "Hello, UDP Server!"
    client_socket.sendto(message.encode(), (host, port))
    response, _ = client_socket.recvfrom(1024)
    print(f"Server Response: {response.decode()}")
    client_socket.close()

start_udp_client()