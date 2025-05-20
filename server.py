# server.py
import socket
import threading

clients = []
nicknames = []

def broadcast(message, sender_client=None):
    for client in clients:
        if client != sender_client:
            try:
                client.send(message.encode())
            except:
                client.close()
                clients.remove(client)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode()
            index = clients.index(client)
            nickname = nicknames[index]
            final_msg = f"[{nickname}] {message}"
            print(final_msg)
            broadcast(final_msg, client)
        except:
            index = clients.index(client)
            nickname = nicknames[index]
            print(f"[-] {nickname} disconnected.")
            clients.remove(client)
            nicknames.remove(nickname)
            client.close()
            broadcast(f"[Server] {nickname} has left the chat.")
            break

def receive_connections():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.178.48', 9999))
    server.listen()

    print("[*] Chat server started on port 9999...")

    while True:
        client, address = server.accept()
        print(f"[+] Connected with {str(address)}")

        client.send("NICK".encode())
        nickname = client.recv(1024).decode()
        nicknames.append(nickname)
        clients.append(client)

        print(f"[+] Nickname of {str(address)} is {nickname}")
        broadcast(f"[Server] {nickname} joined the chat.")
        client.send("✅ Connected to the chat server!".encode())

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive_connections()
