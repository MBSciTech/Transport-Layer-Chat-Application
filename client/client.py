import socket
import threading
from config import HOST as DEFAULT_HOST, PORT, BUFFER_SIZE

host_input = input(f"Enter Server IP address [Default: {DEFAULT_HOST}]: ").strip()
HOST = host_input if host_input else DEFAULT_HOST

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    print(f"Connecting to {HOST}:{PORT}...")
    client_socket.connect((HOST, PORT))
    print("Connected to server successfully!")
except Exception as e:
    print(f"Error: Unable to connect to server at {HOST}:{PORT} ({e})")
    exit(1)

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
