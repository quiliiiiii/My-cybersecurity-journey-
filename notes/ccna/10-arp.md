# CCNA Day 10 - Address Resolution Protocol (ARP)

# Introduction

By now, we know that devices use:

* IP Addresses at Layer 3
* MAC Addresses at Layer 2

But this creates an important question:

How does a device know the MAC address associated with a destination IP address?

For example:

```text
PC1
IP: 192.168.1.10

wants to communicate with

PC2
IP: 192.168.1.20
```

PC1 knows the destination IP address.

However, Ethernet communication requires a destination MAC address.

This is where ARP comes in.

---

# What is ARP?

ARP stands for:

```text
Address Resolution Protocol
```

ARP is responsible for mapping:

```text
IP Address
      ↓
MAC Address
```

In simple terms:

ARP helps a device discover the MAC address associated with an IP address.

---

# Why Do We Need ARP?

Imagine you know someone's house address but not their apartment number.

You can find the building, but not the specific person.

Networking works similarly.

A device may know:

```text
192.168.1.20
```

but Ethernet requires:

```text
AA:BB:CC:DD:EE:FF
```

ARP provides the missing information.

---

# ARP Process Overview

Suppose:

```text
PC1
IP: 192.168.1.10
MAC: 00:11:22:33:44:55
```

wants to reach:

```text
PC2
IP: 192.168.1.20
MAC: AA:BB:CC:DD:EE:FF
```

PC1 knows:

```text
192.168.1.20
```

but does not know:

```text
AA:BB:CC:DD:EE:FF
```

ARP solves this problem.

---

# Step 1: ARP Request

PC1 sends:

```text
Who has 192.168.1.20?
Tell 192.168.1.10
```

This message is called:

```text
ARP Request
```

---

# ARP Requests Are Broadcasts

The request is sent to:

```text
FF:FF:FF:FF:FF:FF
```

which is the Ethernet broadcast address.

Meaning:

```text
Everyone receives the request
```

All devices on the local network inspect the message.

---

# Step 2: ARP Reply

Only the device owning:

```text
192.168.1.20
```

responds.

PC2 sends:

```text
192.168.1.20 is
AA:BB:CC:DD:EE:FF
```

This is called:

```text
ARP Reply
```

---

# ARP Replies Are Unicast

Unlike requests:

ARP replies are sent directly to the requester.

Example:

```text
PC2 → PC1
```

Only PC1 receives the response.

---

# Step 3: ARP Cache

PC1 stores the information.

Example:

| IP Address   | MAC Address       |
| ------------ | ----------------- |
| 192.168.1.20 | AA:BB:CC:DD:EE:FF |

This table is called:

```text
ARP Cache
```

or

```text
ARP Table
```

---

# Why Use an ARP Cache?

Without caching:

Every communication would require a new ARP request.

This would create unnecessary traffic.

Instead:

Devices temporarily remember mappings.

Benefits:

* Faster communication
* Reduced broadcasts
* Improved efficiency

---

# Viewing the ARP Table

Windows:

```cmd
arp -a
```

Linux:

```bash
ip neigh
```

Cisco IOS:

```cisco
show arp
```

---

# Example ARP Table

```text
Internet Address      Physical Address

192.168.1.1          00-AA-BB-11-22-33
192.168.1.20         AA-BB-CC-DD-EE-FF
```

This means:

The device already knows those MAC addresses.

No new ARP request is required.

---

# ARP and the OSI Model

ARP operates between:

```text
Layer 2
and
Layer 3
```

Why?

Because:

ARP takes:

```text
Layer 3 IP Address
```

and converts it into:

```text
Layer 2 MAC Address
```

---

# ARP Packet Structure

Important fields include:

* Sender IP Address
* Sender MAC Address
* Target IP Address
* Target MAC Address

These fields allow devices to identify each other and establish communication.

---

# Communication Example

Network:

```text
PC1
192.168.1.10

PC2
192.168.1.20

Switch
```

Process:

1. PC1 needs PC2's MAC.
2. PC1 sends ARP Request.
3. Switch floods the request.
4. PC2 receives it.
5. PC2 sends ARP Reply.
6. PC1 updates ARP Cache.
7. Communication begins.

---

# ARP and Routers

ARP only works:

```text
Inside the local network
```

It cannot cross routers.

Example:

```text
192.168.1.10
```

wants to reach:

```text
8.8.8.8
```

Google DNS.

The device does NOT ARP for:

```text
8.8.8.8
```

Instead it ARPs for:

```text
Default Gateway
```

because the router will forward the traffic.

This is a very common CCNA exam concept.

---

# Gratuitous ARP

A device may send an ARP announcement about itself.

Purpose:

* Detect duplicate IP addresses
* Update neighboring ARP tables

Commonly seen during:

* Failover events
* Virtual IP migrations
* Network changes

---

# ARP Spoofing

One security risk involving ARP is:

```text
ARP Spoofing
```

or

```text
ARP Poisoning
```

An attacker sends fake ARP messages to convince devices that the attacker's MAC address belongs to another IP address.

Possible results:

* Traffic interception
* Man-in-the-Middle attacks
* Credential theft

This is why network security controls are important.

---

# Real-World Example

At UAEU, when your laptop joins Wi-Fi:

1. It receives an IP address.
2. It learns the gateway address.
3. It sends ARP requests.
4. It learns MAC addresses.
5. Normal communication begins.

This process happens automatically and usually within milliseconds.

---

# Common CCNA Questions

### What does ARP do?

Maps IP addresses to MAC addresses.

---

### Are ARP Requests Broadcast or Unicast?

Broadcast.

---

### Are ARP Replies Broadcast or Unicast?

Unicast.

---

### What is the Ethernet Broadcast Address?

```text
FF:FF:FF:FF:FF:FF
```

---

### Does ARP cross routers?

No.

ARP only works within the local network.

---

### What command displays the ARP table?

Windows:

```cmd
arp -a
```

Cisco:

```cisco
show arp
```

---

# What I Learned

ARP is the protocol that connects Layer 3 addressing with Layer 2 communication. Although users typically only see IP addresses, actual Ethernet communication depends on MAC addresses. ARP allows devices to discover those MAC addresses and maintain efficient communication within a local network. Understanding ARP is essential for network troubleshooting, CCNA studies, and cybersecurity analysis.

---

# Summary

Address Resolution Protocol (ARP) is responsible for resolving IP addresses into MAC addresses. It uses broadcast requests and unicast replies to build ARP tables that allow efficient communication on local networks. ARP is a fundamental networking protocol and a critical concept for both CCNA certification and cybersecurity professionals.
