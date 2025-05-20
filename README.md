# 🖥️ CMD Chat - Offline Terminal Chat App

CMD Chat is a simple yet powerful **LAN-based terminal chat application** that allows two or more devices to chat with each other **without the internet** — using only a **hotspot or local WiFi**.

This project was born while experimenting with **socket programming** during the development of a backdoor tool, and the idea hit:  
💡 *"If we can control a system via sockets, why not chat through them too?"*

## 🚀 Features

- 📶 **Offline communication** using LAN or mobile hotspot (no internet required)
- ⚙️ Built using Python's raw **socket module**
- 💬 Chat directly through the **terminal/command line**
- 🔗 Supports 1-to-1 and (soon) multi-client messaging
- 📱 Future plan: Mobile app version coming soon
- 🌐 Long-range support possible using **NodeMCU ESP8266** as repeater nodes

## 🛠️ How It Works

CMD Chat uses TCP sockets to establish a connection between devices on the same network (e.g., hotspot or WiFi). One system acts as the **server**, while the others connect as **clients**.

## 🧰 Requirements

- Python 3.x
- Devices connected to the same LAN (WiFi or hotspot)
- Basic understanding of command line (for now)

## 🔧 Setup & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/cmd-chat.git
cd cmd-chat
```

### 2. Start the Server

On one device:
```
python server.py
```
### 3. Connect as a Client

On the second device (same LAN):
```
python client.py
```
Enter the server IP when prompted (e.g., 192.168.43.1)
### 4. Start Chatting!

Chat via the terminal — all offline!


### 📦 Future Scope

    📱 Mobile app version (Android)

    🌐 Mesh network support using ESP8266 (NodeMCU)

    🧠 Encrypted communication

    👥 Multi-client chatroom support

### 🙌 Author

Shivam Singh
Built with 💻 + ❤️ + ☕ during late-night experiments.
### 📄 License

This project is licensed under the MIT License.
