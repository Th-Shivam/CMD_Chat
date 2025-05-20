# client.py
import socket
import threading

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            if message == 'NICK':
                sock.send(nickname.encode())
            else:
                print(message)
        except:
            print("[!] Connection lost.")
            sock.close()
            break

def send_messages(sock):
    while True:
        message = input()
        sock.send(message.encode())
        if message.lower() == "exit":
            sock.close()
            break

nickname = input("Enter your nickname: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect(('192.168.178.48', 9999))
except:
    print("Server is not available.")
    exit()

recv_thread = threading.Thread(target=receive_messages, args=(client,))
recv_thread.start()

send_thread = threading.Thread(target=send_messages, args=(client,))
send_thread.start()
