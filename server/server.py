import socket
import threading

from config import HOST, PORT, BUFFER_SIZE
import protocol

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

clients = {}  # username : socket

def broadcast(message, sender_socket):
    for sock in clients.values():
        if sock != sender_socket:
            sock.send(message.encode())

def handle_client(client_socket):
    username = None
    try:
        client_socket.send("ENTER_USERNAME".encode())
        username = client_socket.recv(BUFFER_SIZE).decode().strip()

        if not username:
            return

        clients[username] = client_socket
        print(f"[INFO] {username} joined")

        broadcast(f"{username} joined the chat", client_socket)

        while True:
            message = client_socket.recv(BUFFER_SIZE).decode().strip()

            if not message:
                break

            if message.lower() == "exit":
                break

            if protocol.is_private_message(message):
                receiver, msg = protocol.parse_private_message(message)

                if not receiver or not msg:
                    client_socket.send(
                        "Invalid private message format".encode()
                    )
                    continue

                if receiver in clients:
                    clients[receiver].send(
                        protocol.format_private(username, msg).encode()
                    )
                else:
                    client_socket.send("User not found".encode())
            else:
                broadcast(
                    protocol.format_broadcast(username, message),
                    client_socket
                )

    except Exception as e:
        print(f"[ERROR] {username}: {e}")

    finally:
        if username:
            print(f"[DISCONNECT] {username}")
            if username in clients:
                del clients[username]
                broadcast(f"{username} left the chat", client_socket)
        client_socket.close()


print("Server started... Waiting for clients")

while True:
    client_socket, addr = server_socket.accept()
    print(f"[CONNECTED] {addr}")

    thread = threading.Thread(
        target=handle_client,
        args=(client_socket,),
        daemon=True
    )
    thread.start()
