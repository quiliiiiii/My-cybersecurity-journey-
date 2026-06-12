# CCNA Day 4 - IPv4 Addressing

# Introduction

Every device connected to a network needs an address so that other devices can identify and communicate with it.

In networking, this address is called an **IP Address**.

An IP address serves a similar purpose to a home address.

For example:

* A house address helps a mail carrier deliver mail.
* An IP address helps network devices deliver data.

Without IP addresses, communication across networks would not be possible.

---

# What is IPv4?

IPv4 stands for:

**Internet Protocol Version 4**

It is the most widely used logical addressing system in computer networks.

IPv4 addresses are:

* 32 bits long
* Written in decimal notation
* Divided into four octets

Example:

```text
192.168.1.10
```

Each octet contains:

```text
8 bits
```

Total:

```text
8 × 4 = 32 bits
```

---

# Binary and Decimal

Computers understand only binary.

Humans prefer decimal.

Example:

| Decimal | Binary   |
| ------- | -------- |
| 192     | 11000000 |
| 168     | 10101000 |
| 1       | 00000001 |
| 10      | 00001010 |

Therefore:

```text
192.168.1.10
```

becomes:

```text
11000000.10101000.00000001.00001010
```

---

# IPv4 Address Structure

An IPv4 address consists of two parts:

1. Network Portion
2. Host Portion

Example:

```text
192.168.1.10/24
```

Network:

```text
192.168.1
```

Host:

```text
10
```

Think of it like:

```text
University Building = Network

Room Number = Host
```

The network identifies the location.

The host identifies the device inside that location.

---

# Why Do We Need Network and Host Portions?

Imagine a city containing thousands of houses.

If every house existed without neighborhoods, finding destinations would be extremely difficult.

Networking works the same way.

Routers use the network portion to determine where traffic should go.

The host portion identifies the specific device.

---

# Classes of IPv4 Addresses

Historically, IPv4 addresses were divided into classes.

Although CIDR is used today, Cisco still tests basic class concepts.

---

## Class A

Range:

```text
1.0.0.0 – 126.255.255.255
```

Default Mask:

```text
255.0.0.0
```

CIDR:

```text
/8
```

Large organizations.

---

## Class B

Range:

```text
128.0.0.0 – 191.255.255.255
```

Default Mask:

```text
255.255.0.0
```

CIDR:

```text
/16
```

Medium-sized organizations.

---

## Class C

Range:

```text
192.0.0.0 – 223.255.255.255
```

Default Mask:

```text
255.255.255.0
```

CIDR:

```text
/24
```

Small organizations and home networks.

---

# Public vs Private IP Addresses

One of the most important CCNA concepts.

---

## Public IP Addresses

Public addresses are routable on the Internet.

They are globally unique.

Example:

```text
8.8.8.8
```

Google DNS Server.

Public addresses are assigned by Internet Service Providers (ISPs).

---

## Private IP Addresses

Private addresses are used internally.

They cannot be routed directly on the Internet.

Three private ranges exist.

### Range 1

```text
10.0.0.0 – 10.255.255.255
```

### Range 2

```text
172.16.0.0 – 172.31.255.255
```

### Range 3

```text
192.168.0.0 – 192.168.255.255
```

These are extremely important for the CCNA exam.

Memorize them.

---

# Why Private Addresses Exist

Imagine every phone, laptop, smart TV, printer, and camera needed a public address.

IPv4 addresses would run out quickly.

Private addressing allows millions of devices to share a smaller pool of public addresses through NAT.

---

# Special IPv4 Addresses

---

## Loopback Address

```text
127.0.0.1
```

Purpose:

Testing the local TCP/IP stack.

Command:

```bash
ping 127.0.0.1
```

If successful:

* Network card is working
* TCP/IP stack is functioning

---

## APIPA Address

Automatic Private IP Addressing.

Range:

```text
169.254.0.0 – 169.254.255.255
```

Occurs when:

* DHCP fails
* Device assigns itself an address

Common troubleshooting clue.

If you see:

```text
169.254.x.x
```

Check DHCP immediately.

---

# Network Address

Represents the network itself.

Example:

```text
192.168.1.0/24
```

Network Address:

```text
192.168.1.0
```

Cannot be assigned to a device.

---

# Broadcast Address

Used to communicate with all hosts in a network.

Example:

```text
192.168.1.255
```

All devices in that network receive the broadcast.

Cannot be assigned to a host.

---

# Host Addresses

The usable addresses between:

Network Address

and

Broadcast Address

Example:

```text
Network:
192.168.1.0

Broadcast:
192.168.1.255
```

Usable:

```text
192.168.1.1
through
192.168.1.254
```

Total:

254 hosts

---

# Real-World Example

Home Router:

```text
192.168.1.1
```

Laptop:

```text
192.168.1.10
```

Phone:

```text
192.168.1.20
```

Printer:

```text
192.168.1.30
```

All belong to:

```text
192.168.1.0/24
```

network.

The router uses NAT to access the Internet.

---

# Common CCNA Questions

### Can two devices have the same IP address?

No.

This creates an IP conflict.

---

### Is 127.0.0.1 routable?

No.

It is a loopback address.

---

### Is 192.168.10.15 public or private?

Private.

Because it belongs to:

```text
192.168.0.0/16
```

---

### What does APIPA indicate?

DHCP failure.

---

# Commands You Should Know

Windows:

```cmd
ipconfig
```

Linux:

```bash
ip addr
```

Cisco:

```cisco
show ip interface brief
```

---

# Key Terms

| Term            | Meaning                     |
| --------------- | --------------------------- |
| IPv4            | Internet Protocol Version 4 |
| Network Portion | Identifies the network      |
| Host Portion    | Identifies the device       |
| Public IP       | Internet-routable address   |
| Private IP      | Internal-use address        |
| Loopback        | 127.0.0.1                   |
| APIPA           | 169.254.0.0/16              |
| Broadcast       | Message to all devices      |

---

# Summary

IPv4 addressing is the foundation of networking. Every device requires a unique IP address to communicate. Understanding public and private addressing, network and host portions, loopback addresses, APIPA, and special address types is essential before learning subnetting, routing, VLANs, and advanced CCNA topics.
