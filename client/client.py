import socket
import threading
import sys

from config import SERVER_IP, PORT, BUFFER_SIZE
import protocol

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))

username_set = False
username = ""

lock = threading.Lock()

def receive_messages():
    global username_set, username

    while True:
        try:
            message = client_socket.recv(BUFFER_SIZE).decode()
            if not message:
                print("\nServer closed the connection.")
                break


            with lock:
                if message == "ENTER_USERNAME":
                    username = input("Enter username: ")
                    client_socket.send(username.encode())
                    username_set = True
                    print("\nYou joined the chat.")
                    print(protocol.help_message(), end="")
                else:
                    # move cursor to new line before printing
                    sys.stdout.write("\n" + message + "\n> ")
                    sys.stdout.flush()

        except:
            break

def send_messages():
    global username_set

    while not username_set:
        pass  # wait until username is entered

    while True:
        try:
            message = input("> ")

            if message.lower() == "exit":
                client_socket.send("EXIT".encode())
                break


            client_socket.send(message.encode())

        except:
            break

recv_thread = threading.Thread(target=receive_messages, daemon=True)
send_thread = threading.Thread(target=send_messages, daemon=True)

recv_thread.start()
send_thread.start()

recv_thread.join()
send_thread.join()
