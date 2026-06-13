# CCNA Day 9 - Ethernet, MAC Addresses, and Switching Fundamentals

# Introduction

When devices communicate on the same local network, they do not use IP addresses alone.

While IP addresses help devices communicate across networks, local communication relies heavily on Ethernet and MAC addresses.

Understanding Ethernet and switching is fundamental to networking because nearly every modern LAN is built using Ethernet technology.

In this lesson, we will explore:

* Ethernet
* MAC addresses
* Ethernet frames
* Switches
* MAC address tables
* Frame forwarding

These concepts form the foundation of local area network communication.

---

# What is Ethernet?

Ethernet is the most widely used LAN technology in the world.

It defines:

* How devices communicate
* How data is formatted
* How frames are transmitted
* How devices access the network

Ethernet operates primarily at:

```text
OSI Layer 1 (Physical)
OSI Layer 2 (Data Link)
```

Most home, university, and enterprise networks use Ethernet.

---

# What is a MAC Address?

MAC stands for:

```text
Media Access Control
```

A MAC address is a unique identifier assigned to a network interface card (NIC).

Example:

```text
00:1A:2B:3C:4D:5E
```

or

```text
00-1A-2B-3C-4D-5E
```

---

# Characteristics of MAC Addresses

A MAC address:

* Is 48 bits long
* Is written in hexadecimal
* Operates at Layer 2
* Identifies devices within a LAN

Example:

```text
00:1A:2B:3C:4D:5E
```

Each pair represents one byte.

Total:

```text
6 bytes = 48 bits
```

---

# MAC Address Structure

A MAC address contains two parts:

### OUI

Organizationally Unique Identifier

The first 24 bits identify the manufacturer.

Example:

```text
00:1A:2B
```

Could identify a specific vendor.

---

### Device Identifier

The last 24 bits identify the specific device.

Example:

```text
3C:4D:5E
```

This portion should be unique.

---

# Why Do We Need MAC Addresses?

Imagine a switch connecting several devices:

```text
PC1
PC2
PC3
Printer
```

Each device needs a unique identifier.

Within the local network, switches use MAC addresses to determine where traffic should go.

Without MAC addresses, switches would not know which device should receive a frame.

---

# Ethernet Frames

At Layer 2, data is transmitted using:

```text
Frames
```

An Ethernet frame contains:

```text
Destination MAC
Source MAC
Type
Data
FCS
```

---

# Ethernet Frame Structure

Simplified example:

```text
-------------------------------------------------
Destination MAC
Source MAC
Type
Data
Frame Check Sequence (FCS)
-------------------------------------------------
```

The most important fields are:

### Destination MAC

Where the frame is going.

### Source MAC

Who sent the frame.

---

# What is FCS?

FCS stands for:

```text
Frame Check Sequence
```

Purpose:

* Detect transmission errors
* Verify frame integrity

If the calculated value does not match the received value, the frame is discarded.

---

# What is a Switch?

A switch is a Layer 2 device that connects devices within the same network.

Example:

```text
PC1
  |
PC2 --- Switch --- Printer
  |
PC3
```

The switch learns MAC addresses and forwards frames intelligently.

---

# How Switches Learn

Every time a frame enters a switch:

The switch records:

```text
Source MAC Address
Incoming Port
```

Example:

```text
MAC Address            Port

00:11:22:33:44:55     Fa0/1
AA:BB:CC:DD:EE:FF     Fa0/2
```

This information is stored inside:

```text
MAC Address Table
```

---

# MAC Address Table

Also called:

```text
CAM Table
```

The table maps:

```text
MAC Address
→
Switch Port
```

Example:

| MAC Address       | Port  |
| ----------------- | ----- |
| 00:11:22:33:44:55 | Fa0/1 |
| AA:BB:CC:DD:EE:FF | Fa0/2 |

---

# Frame Forwarding

Suppose:

```text
PC1 → PC2
```

The switch checks:

```text
Destination MAC
```

If the MAC exists in the table:

```text
Forward directly
```

This is called:

```text
Known Unicast
```

---

# Unknown Unicast

What happens if the switch does not know the destination MAC?

The switch:

```text
Floods the frame
```

to all ports except the incoming port.

This is called:

```text
Unknown Unicast Flooding
```

Once the destination replies, the switch learns the MAC address.

---

# Broadcast Frames

A broadcast is sent to:

```text
All devices
```

Broadcast MAC:

```text
FF:FF:FF:FF:FF:FF
```

Every device on the network receives the frame.

Common examples:

* ARP Requests
* DHCP Discover Messages

---

# Unicast vs Broadcast

### Unicast

One sender

One receiver

Example:

```text
PC1 → PC2
```

---

### Broadcast

One sender

All devices

Example:

```text
PC1 → Everyone
```

---

# Collision Domains

In older networks using hubs:

Multiple devices shared the same collision domain.

Result:

* More collisions
* Lower performance

Switches improve performance because:

Each switch port becomes its own collision domain.

---

# Broadcast Domains

By default:

A switch creates:

```text
One Broadcast Domain
```

Every broadcast reaches all devices.

Later we will learn how:

```text
VLANs
```

create multiple broadcast domains.

---

# Switch Commands

View MAC table:

```cisco
show mac address-table
```

View interfaces:

```cisco
show interfaces status
```

Basic switch information:

```cisco
show version
```

---

# Real-World Example

University Network:

```text
Student PCs
Faculty PCs
Printers
Servers
```

All connected to switches.

The switches:

* Learn MAC addresses
* Build MAC tables
* Forward frames efficiently

Without switches, modern LANs would not function effectively.

---

# Common CCNA Questions

### At which layer does a switch operate?

Layer 2

---

### What address does a switch use?

MAC Address

---

### What is the length of a MAC address?

48 bits

---

### What is the broadcast MAC address?

```text
FF:FF:FF:FF:FF:FF
```

---

### What does a switch learn?

Source MAC addresses

---

# What I Learned

Ethernet is the foundation of modern local area networks. Devices use MAC addresses to communicate at Layer 2, while switches use MAC address tables to forward frames efficiently. Understanding Ethernet, frame forwarding, broadcasts, and MAC learning is essential before studying ARP, VLANs, and advanced switching technologies.

---

# Summary

Ethernet is the most common LAN technology and relies on MAC addresses for local communication. Switches use MAC address tables to learn device locations and forward frames efficiently. These concepts form the basis of modern network communication and are essential knowledge for both CCNA students and cybersecurity professionals.
