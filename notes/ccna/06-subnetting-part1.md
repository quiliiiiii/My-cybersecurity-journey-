# CCNA Day 6 - Subnetting Part 1

# Introduction

Subnetting is one of the most important skills in networking and one of the most challenging topics for new CCNA students.

Many networking concepts such as routing, VLAN design, network planning, and IP address management depend on subnetting.

The purpose of subnetting is to divide a large network into smaller and more manageable networks.

By the end of this lesson, you should understand:

* Why subnetting exists
* How networks are divided
* Network addresses
* Broadcast addresses
* Host ranges
* Basic subnet calculations

---

# What is Subnetting?

Subnetting is the process of dividing one network into multiple smaller networks.

For example:

Without subnetting:

```text
192.168.1.0/24
```

One network

254 hosts

With subnetting:

```text
192.168.1.0/25
192.168.1.128/25
```

Two networks

126 hosts each

---

# Why Do We Subnet?

Imagine a company with:

* HR Department
* Finance Department
* IT Department
* Management

Putting every device into one large network creates problems:

* Excessive broadcasts
* Poor performance
* Difficult management
* Security concerns

Subnetting allows us to create separate networks.

Benefits:

* Better security
* Better performance
* Easier troubleshooting
* More efficient IP usage

---

# Understanding Borrowing Bits

A subnet mask contains:

Network Bits

and

Host Bits

Example:

```text
/24
```

Binary:

```text
11111111.11111111.11111111.00000000
```

Network Bits:

24

Host Bits:

8

When subnetting, we borrow bits from the host portion.

---

# Starting Network

Let's begin with:

```text
192.168.1.0/24
```

Hosts available:

2^8-2

Result:

```text
254 hosts
```

---

# Example 1: Convert /24 to /25

Original:

```text
192.168.1.0/24
```

New:

```text
192.168.1.0/25
```

Subnet Mask:

```text
255.255.255.128
```

Binary:

```text
11111111.11111111.11111111.10000000
```

We borrowed:

```text
1 bit
```

---

# How Many Subnets?

Formula:

2^n

Where:

```text
n = borrowed bits
```

Borrowed:

```text
1 bit
```

Calculation:

2^1

Result:

```text
2 subnets
```

---

# How Many Hosts Per Subnet?

Remaining host bits:

```text
7
```

Formula:

2^7-2

Result:

```text
126 hosts
```

---

# Subnet #1

Network:

```text
192.168.1.0/25
```

Network Address:

```text
192.168.1.0
```

First Host:

```text
192.168.1.1
```

Last Host:

```text
192.168.1.126
```

Broadcast:

```text
192.168.1.127
```

---

# Subnet #2

Network:

```text
192.168.1.128/25
```

First Host:

```text
192.168.1.129
```

Last Host:

```text
192.168.1.254
```

Broadcast:

```text
192.168.1.255
```

---

# Visual Representation

```text
Subnet 1

Network:
192.168.1.0

Hosts:
192.168.1.1
to
192.168.1.126

Broadcast:
192.168.1.127
```

```text
Subnet 2

Network:
192.168.1.128

Hosts:
192.168.1.129
to
192.168.1.254

Broadcast:
192.168.1.255
```

---

# The Magic Number

The easiest way to subnet is using the "Magic Number".

Formula:

```text
256 - subnet mask value
```

Example:

```text
255.255.255.128
```

Magic Number:

```text
256 - 128 = 128
```

Start counting:

```text
0
128
256
```

Networks:

```text
192.168.1.0
192.168.1.128
```

---

# Example 2: /26

Mask:

```text
255.255.255.192
```

Magic Number:

```text
256 - 192 = 64
```

Count:

```text
0
64
128
192
256
```

Networks:

```text
192.168.1.0
192.168.1.64
192.168.1.128
192.168.1.192
```

Total:

```text
4 subnets
```

---

# Hosts in /26

Host Bits:

```text
6
```

Formula:

2^6-2

Result:

```text
62 hosts
```

---

# Quick Reference Table

| CIDR | Mask            | Hosts |
| ---- | --------------- | ----- |
| /24  | 255.255.255.0   | 254   |
| /25  | 255.255.255.128 | 126   |
| /26  | 255.255.255.192 | 62    |
| /27  | 255.255.255.224 | 30    |
| /28  | 255.255.255.240 | 14    |

Memorize this table.

It appears constantly in CCNA.

---

# Exam Tips

When you see a subnetting question:

Step 1:

Identify CIDR notation.

Step 2:

Determine subnet mask.

Step 3:

Find magic number.

Step 4:

Identify network address.

Step 5:

Identify broadcast address.

Step 6:

Determine usable host range.

Never rush.

Subnetting mistakes usually happen because students skip steps.

---

# Practice Questions

## Question 1

Network:

```text
192.168.1.0/25
```

What is the broadcast address?

Answer:

```text
192.168.1.127
```

---

## Question 2

Network:

```text
192.168.1.128/25
```

What is the first usable host?

Answer:

```text
192.168.1.129
```

---

## Question 3

How many hosts are available in a /26 network?

Answer:

```text
62
```

---

# What I Learned

Subnetting allows a network administrator to divide large networks into smaller, more efficient networks. By borrowing host bits and calculating network ranges, it becomes possible to improve performance, security, and IP address management. Understanding subnet masks, CIDR notation, host calculations, and the magic number method is essential for success in CCNA and real-world networking.

---

# Summary

Subnetting is the foundation of IP network design. A network can be divided into multiple smaller subnets by borrowing host bits. Understanding how to calculate network addresses, broadcast addresses, and host ranges is one of the most important skills for every network engineer and cybersecurity professional.
