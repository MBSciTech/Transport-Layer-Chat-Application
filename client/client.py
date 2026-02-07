import socket
import threading
from config import HOST, PORT, BUFFER_SIZE

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            message = client_socket.recv(BUFFER_SIZE).decode()
            if not message:
                break

            if message == "ENTER_USERNAME":
                continue

            print("\n" + message)
            print("> ", end="", flush=True)

        except:
            print("\nServer closed the connection.")
            break

def send_messages():
    while True:
        msg = input("> ")
        client_socket.send(msg.encode())
        if msg.lower() == "exit":
            break

username = input("Enter username: ")
client_socket.send(username.encode())

print("\nYou joined the chat.")
print("Commands:")
print("pvtmsg/username message  -> private message")
print("exit                     -> leave chat")

receive_thread = threading.Thread(target=receive_messages, daemon=True)
receive_thread.start()

send_messages()
client_socket.close()
