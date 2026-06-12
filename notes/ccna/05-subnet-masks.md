# CCNA Day 5 - Subnet Masks

# Introduction

An IP address alone is not enough for a device to understand which network it belongs to.

Every IPv4 address must be accompanied by a subnet mask.

The subnet mask tells a device:

* Which part of the IP address identifies the network
* Which part identifies the host

Without a subnet mask, routers and computers would not know how to communicate properly.

---

# What is a Subnet Mask?

A subnet mask is a 32-bit value used to divide an IPv4 address into:

1. Network Portion
2. Host Portion

Example:

IP Address:

```text
192.168.1.10
```

Subnet Mask:

```text
255.255.255.0
```

The subnet mask tells us that:

```text
192.168.1
```

is the network.

And:

```text
10
```

is the host.

---

# Why Do We Need Subnet Masks?

Imagine a university.

Every student has:

* Building Number
* Room Number

Example:

```text
Engineering Building
Room 205
```

The building identifies the location.

The room identifies the individual.

Subnet masks work the same way.

The network portion identifies the network.

The host portion identifies the device.

---

# Binary Review

Remember:

IPv4 addresses contain 32 bits.

Each octet contains 8 bits.

Example:

```text
255
```

in binary is:

```text
11111111
```

Example:

```text
0
```

in binary is:

```text
00000000
```

---

# Understanding 255.255.255.0

Subnet Mask:

```text
255.255.255.0
```

Binary:

```text
11111111.11111111.11111111.00000000
```

Notice:

```text
11111111
```

means:

Network Bits

and

```text
00000000
```

means:

Host Bits

Therefore:

```text
255.255.255.0
```

means:

```text
24 Network Bits
8 Host Bits
```

---

# CIDR Notation

Instead of writing:

```text
255.255.255.0
```

network engineers usually write:

```text
/24
```

This means:

```text
24 network bits
```

Examples:

| CIDR | Subnet Mask     |
| ---- | --------------- |
| /8   | 255.0.0.0       |
| /16  | 255.255.0.0     |
| /24  | 255.255.255.0   |
| /25  | 255.255.255.128 |
| /26  | 255.255.255.192 |

Memorize these.

They appear constantly in CCNA.

---

# Example 1

Address:

```text
192.168.1.50/24
```

Subnet Mask:

```text
255.255.255.0
```

Network:

```text
192.168.1.0
```

Broadcast:

```text
192.168.1.255
```

Valid Hosts:

```text
192.168.1.1
through
192.168.1.254
```

Total Hosts:

```text
254
```

---

# Network Address

The first address in a subnet.

Example:

```text
192.168.1.0
```

Purpose:

Identifies the network itself.

Cannot be assigned to a device.

---

# Broadcast Address

The last address in a subnet.

Example:

```text
192.168.1.255
```

Purpose:

Send traffic to all devices in the subnet.

Cannot be assigned to a device.

---

# Host Addresses

The addresses between:

Network Address

and

Broadcast Address

Example:

```text
192.168.1.1
to
192.168.1.254
```

These can be assigned to devices.

---

# How Routers Use Subnet Masks

Routers use subnet masks to determine:

```text
Local Network?
or
Remote Network?
```

Example:

Device A:

```text
192.168.1.10/24
```

Device B:

```text
192.168.1.20/24
```

Same network.

Direct communication is possible.

---

Example:

Device A:

```text
192.168.1.10/24
```

Device B:

```text
192.168.2.10/24
```

Different networks.

A router is required.

---

# Common Subnet Masks

## /24

```text
255.255.255.0
```

Hosts:

```text
254
```

Very common in small networks.

---

## /25

```text
255.255.255.128
```

Hosts:

```text
126
```

Splits a /24 into two equal networks.

---

## /26

```text
255.255.255.192
```

Hosts:

```text
62
```

Creates four subnets from a /24.

---

## /27

```text
255.255.255.224
```

Hosts:

```text
30
```

Common in branch offices.

---

## /28

```text
255.255.255.240
```

Hosts:

```text
14
```

Used for very small networks.

---

# Host Formula

A very important CCNA formula:

2^h - 2

Where:

```text
h = number of host bits
```

Why subtract 2?

Because:

* One address is the Network Address
* One address is the Broadcast Address

Neither can be assigned to hosts.

---

# Example Calculation

Subnet:

```text
/24
```

Host Bits:

```text
8
```

Calculation:

2^8 - 2

Result:

```text
254 hosts
```

---

# Real-World Example

Office Network:

```text
192.168.10.0/24
```

Devices:

```text
192.168.10.1
Router

192.168.10.10
PC

192.168.10.20
Laptop

192.168.10.30
Printer
```

All devices belong to the same subnet.

No router is needed for communication between them.

---

# Troubleshooting Example

A PC has:

```text
IP:
192.168.1.10

Mask:
255.255.255.0
```

Another PC has:

```text
IP:
192.168.1.20

Mask:
255.255.0.0
```

Problem:

Different subnet masks.

This may cause communication issues and incorrect routing decisions.

Always verify:

* IP Address
* Subnet Mask
* Default Gateway

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

Cisco IOS:

```cisco
show ip interface brief
```

---

# Common CCNA Questions

### What does a subnet mask do?

Separates network bits from host bits.

---

### What does /24 mean?

24 network bits.

---

### Can a network address be assigned to a host?

No.

---

### Can a broadcast address be assigned to a host?

No.

---

### Why do we subtract 2 in host calculations?

One address is reserved for the network.

One address is reserved for broadcast.

---

# Exam Tips

Memorize:

```text
/8  = 255.0.0.0
/16 = 255.255.0.0
/24 = 255.255.255.0
```

Understand:

* Network Address
* Broadcast Address
* Host Address
* CIDR Notation

These concepts appear throughout subnetting, routing, VLANs, OSPF, and many CCNA exam questions.

---

# Summary

Subnet masks determine which portion of an IP address identifies the network and which portion identifies the host. Understanding subnet masks is essential before learning subnetting, routing, VLANs, and advanced CCNA topics. A strong understanding of CIDR notation and host calculations will make future CCNA topics much easier.
