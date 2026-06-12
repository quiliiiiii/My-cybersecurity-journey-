# OSI Model

## What is the OSI Model?

The Open Systems Interconnection (OSI) model is a conceptual framework that describes how data travels across a network.

It contains seven layers.

---

## Layer 7 – Application

Provides network services directly to users and applications.

Examples:

* HTTP
* HTTPS
* DNS
* FTP

Devices:

* Web servers
* DNS servers

---

## Layer 6 – Presentation

Responsible for:

* Data formatting
* Encryption
* Compression

Examples:

* SSL/TLS
* JPEG
* PNG

---

## Layer 5 – Session

Creates, maintains, and terminates communication sessions between devices.

Examples:

* NetBIOS
* RPC

---

## Layer 4 – Transport

Provides end-to-end communication.

Protocols:

* TCP
* UDP

TCP:

* Reliable
* Connection-oriented

UDP:

* Faster
* Connectionless

PDU:
Segment

---

## Layer 3 – Network

Responsible for routing packets between networks.

Protocol:

* IP

Devices:

* Routers

PDU:
Packet

---

## Layer 2 – Data Link

Responsible for MAC addressing and frame forwarding.

Devices:

* Switches

PDU:
Frame

Address:
MAC Address

---

## Layer 1 – Physical

Responsible for transmitting bits across physical media.

Examples:

* Ethernet cables
* Fiber optic cables
* Radio signals

PDU:
Bits

---

## OSI Layer Summary

| Layer | Name         | PDU     |
| ----- | ------------ | ------- |
| 7     | Application  | Data    |
| 6     | Presentation | Data    |
| 5     | Session      | Data    |
| 4     | Transport    | Segment |
| 3     | Network      | Packet  |
| 2     | Data Link    | Frame   |
| 1     | Physical     | Bits    |

---

## Mnemonic

All People Seem To Need Data Processing

Application
Presentation
Session
Transport
Network
Data Link
Physical

---

## Exam Tips

Remember:

* Routers operate at Layer 3
* Switches operate at Layer 2
* TCP and UDP operate at Layer 4
* IP operates at Layer 3
* MAC addresses operate at Layer 2
