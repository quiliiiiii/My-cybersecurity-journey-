# CCNA Day 3 - TCP/IP Model and Encapsulation

## What is the TCP/IP Model?

The TCP/IP model is the networking model used on the Internet today.

Unlike the OSI model, which has 7 layers, TCP/IP has 4 layers.

---

## TCP/IP Layers

### 4. Application Layer

Provides services directly to applications.

Protocols:

* HTTP
* HTTPS
* DNS
* FTP
* SMTP
* SSH

Examples:

* Web browsing
* Email
* File transfers

---

### 3. Transport Layer

Responsible for end-to-end communication.

Protocols:

* TCP
* UDP

Functions:

* Segmentation
* Reliability
* Error recovery
* Flow control

---

### 2. Internet Layer

Responsible for logical addressing and routing.

Protocols:

* IPv4
* IPv6
* ICMP

Functions:

* Packet forwarding
* Routing

Devices:

* Routers

---

### 1. Network Access Layer

Responsible for sending data across the physical network.

Technologies:

* Ethernet
* Wi-Fi

Functions:

* MAC addressing
* Framing
* Physical transmission

Devices:

* Switches
* Network Interface Cards (NICs)

---

## OSI vs TCP/IP

| OSI          | TCP/IP         |
| ------------ | -------------- |
| Application  | Application    |
| Presentation | Application    |
| Session      | Application    |
| Transport    | Transport      |
| Network      | Internet       |
| Data Link    | Network Access |
| Physical     | Network Access |

---

## Encapsulation

When data is transmitted through a network, each layer adds its own header.

This process is called:

**Encapsulation**

---

## Encapsulation Process

### Step 1 - Application Data

Example:

```text
GET /index.html
```

At this stage it is simply data.

---

### Step 2 - Transport Layer

TCP adds a TCP header.

Result:

```text
TCP Segment
```

Information added:

* Source Port
* Destination Port
* Sequence Number

---

### Step 3 - Internet Layer

IP adds an IP header.

Result:

```text
IP Packet
```

Information added:

* Source IP
* Destination IP

---

### Step 4 - Network Access Layer

Ethernet adds a Frame Header.

Result:

```text
Ethernet Frame
```

Information added:

* Source MAC
* Destination MAC

---

### Step 5 - Physical Transmission

The frame is converted into:

```text
Bits
```

and transmitted across the network.

---

## Decapsulation

At the receiving device, headers are removed layer by layer.

This process is called:

**Decapsulation**

---

## Protocol Data Units (PDUs)

| Layer          | PDU     |
| -------------- | ------- |
| Application    | Data    |
| Transport      | Segment |
| Internet       | Packet  |
| Network Access | Frame   |
| Physical       | Bits    |

---

## TCP

Transmission Control Protocol

Characteristics:

* Reliable
* Connection-oriented
* Error checking
* Acknowledgments

Used by:

* HTTP
* HTTPS
* SSH
* FTP

---

## UDP

User Datagram Protocol

Characteristics:

* Faster
* Connectionless
* No acknowledgments

Used by:

* DNS
* VoIP
* Streaming
* Online gaming

---

## TCP vs UDP

| TCP                  | UDP                |
| -------------------- | ------------------ |
| Reliable             | Faster             |
| Connection-oriented  | Connectionless     |
| Uses acknowledgments | No acknowledgments |
| More overhead        | Less overhead      |

---

## Exam Tips

Remember:

* The Internet uses the TCP/IP model.
* Encapsulation adds headers as data moves down the stack.
* Decapsulation removes headers.
* Routers make decisions using IP addresses.
* Switches forward frames using MAC addresses.
* TCP is reliable.
* UDP is fast.

---

## Summary

The TCP/IP model is the foundation of modern networking. Understanding encapsulation, TCP, UDP, packets, frames, and the relationship between OSI and TCP/IP is essential for success in CCNA and cybersecurity.
