import socket

def start_tcp_server():
    host = '127.0.0.1'  # Localhost
    port = 5051         # Port to listen on

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"TCP Server listening on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Received: {data}")
        conn.send("Message received".encode())
    conn.close()

start_tcp_server()