import socket

def start_tcp_client():
    host = '127.0.0.1'
    port = 5051

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    message = input()
    client_socket.send(message.encode())
    response = client_socket.recv(1024).decode()
    print(f"Server Response: {response}")
    client_socket.close()

start_tcp_client()