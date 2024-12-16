import socket

def start_udp_server():
    host = '127.0.0.1'
    port = 5001

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"UDP Server listening on {host}:{port}")

    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Message from {addr}: {data.decode()}")
        server_socket.sendto("Message received".encode(), addr)

start_udp_server()
