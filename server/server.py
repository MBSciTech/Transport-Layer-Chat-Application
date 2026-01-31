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
    try:
        client_socket.send("ENTER_USERNAME".encode())
        username = client_socket.recv(BUFFER_SIZE).decode()

        clients[username] = client_socket
        print(f"{username} joined")

        broadcast(f"{username} joined the chat", client_socket)

        while True:
            message = client_socket.recv(BUFFER_SIZE).decode()
            if message == "EXIT":
                break


            if protocol.is_private_message(message):
                receiver, msg = protocol.parse_private_message(message)

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

    except:
        pass
    finally:
        client_socket.close()
        if username in clients:
            del clients[username]
            broadcast(f"{username} left the chat", client_socket)
            print(f"{username} disconnected")


print("Server started... Waiting for clients")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connected: {addr}")

    thread = threading.Thread(
        target=handle_client,
        args=(client_socket,)
    )
    thread.start()


