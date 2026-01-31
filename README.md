# Transport Layer Chat Application

## 📌 Project Overview

The **Transport Layer Chat Application** is a LAN-based multi-user chat system implemented using **Python socket programming**.
It demonstrates **Transport Layer concepts** such as TCP communication, client–server architecture, full-duplex data transfer, and basic application-layer protocol design.

The application supports:

* Public (broadcast) messaging
* Private (unicast) messaging
* Multiple clients connected simultaneously
* LAN / hotspot-based communication

---

## 🎯 Objectives

* To understand **TCP socket programming**
* To demonstrate **client–server communication**
* To design a **simple application-layer protocol**
* To handle **multiple clients using multithreading**
* To differentiate between **broadcast and private communication**

---

## 🧠 Computer Networking Concepts Used

* Transport Layer (TCP)
* Client–Server Model
* Sockets (`AF_INET`, `SOCK_STREAM`)
* Multithreading
* Full-Duplex Communication
* Application-Layer Protocol Design
* LAN / Hotspot Networking

---

## 📁 Project Structure

```
Transport-Layer-Chat-Application/
│
├── server/
│   ├── server.py
│   ├── config.py
│   └── protocol.py
│
├── client/
│   ├── client.py
│   ├── config.py
│   └── protocol.py
│
└── README.md
```

---

## ⚙️ Protocol Design

Since TCP only transfers raw bytes, a **custom application-layer protocol** is implemented.

### Message Formats

* **JOIN** → Username sent during connection
* **Broadcast Message**

  ```
  Hello everyone
  ```
* **Private Message**

  ```
  pvtmsg/username message
  ```
* **Exit Command**

  ```
  exit
  ```

---

## 🚀 How to Run the Project

### 1️⃣ Start the Server

```
cd server
python server.py
```

### 2️⃣ Start Clients (in multiple terminals)

```
cd client
python client.py
```

> All devices must be connected to the **same LAN or mobile hotspot**.

---

## 💬 Usage Instructions

### Broadcast Message

```
Hi everyone
```

➡ Visible to all connected users.

### Private Message

```
pvtmsg/Jay Hello Jay
```

➡ Visible only to the specified user.

### Exit Chat

```
exit
```

➡ Gracefully disconnects the client.

---

## 🧪 Sample Output

```
Maharshi joined the chat
Jay: Hi
[PRIVATE] Maharshi: Hello Jay
Jay left the chat
```

---

## 🛠 Technologies Used

* Python 3
* Socket Programming
* Threading Module
* TCP/IP Networking

---

## 📌 Key Features

* Multiple clients supported simultaneously
* Reliable communication using TCP
* Clear separation of logic, configuration, and protocol
* Works on LAN and mobile hotspot
* Easy to understand and explain in viva

---

## 🎓 Academic Relevance

This project demonstrates **Transport Layer functionality** without relying on high-level networking libraries, making it suitable for:

* Computer Networks Lab
* Mini Project
* Viva / Practical Examination

---

## 👨‍💻 Developed By

**Mohan (Maharshi)**
Computer Networking Project
