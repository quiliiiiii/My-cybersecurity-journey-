# CCNA Day 7 - Subnetting Part 2: Mastering /27, /28, and /29 Networks

# Introduction

In the previous lesson, we learned how subnetting works and how to calculate /25 and /26 networks.

In this lesson, we will focus on smaller subnet sizes that commonly appear in CCNA exams and real-world network designs.

By the end of this lesson, you should be able to:

* Calculate subnet ranges quickly
* Identify network addresses
* Identify broadcast addresses
* Determine usable host ranges
* Use the Magic Number method confidently

---

# Review: The Magic Number

The fastest subnetting method for CCNA is:

```text
256 - interesting octet
```

Example:

```text
255.255.255.224
```

Magic Number:

```text
256 - 224 = 32
```

Count by 32:

```text
0
32
64
96
128
160
192
224
256
```

These are your subnet boundaries.

---

# Understanding /27

CIDR:

```text
/27
```

Subnet Mask:

```text
255.255.255.224
```

Binary:

```text
11111111.11111111.11111111.11100000
```

Host Bits:

```text
5
```

Hosts:

2^5-2

Result:

```text
30 hosts
```

---

# /27 Subnets

Starting Network:

```text
192.168.1.0/27
```

Magic Number:

```text
32
```

Subnets:

```text
192.168.1.0
192.168.1.32
192.168.1.64
192.168.1.96
192.168.1.128
192.168.1.160
192.168.1.192
192.168.1.224
```

---

# Example

Network:

```text
192.168.1.64/27
```

Next subnet:

```text
192.168.1.96
```

Broadcast:

```text
192.168.1.95
```

Host Range:

```text
192.168.1.65
through
192.168.1.94
```

---

# Understanding /28

CIDR:

```text
/28
```

Mask:

```text
255.255.255.240
```

Magic Number:

```text
256 - 240 = 16
```

Host Bits:

```text
4
```

Hosts:

2^4-2

Result:

```text
14 hosts
```

---

# /28 Subnets

Count by 16:

```text
0
16
32
48
64
80
96
112
128
144
160
176
192
208
224
240
256
```

Example:

```text
192.168.1.80/28
```

Network:

```text
192.168.1.80
```

Broadcast:

```text
192.168.1.95
```

Hosts:

```text
192.168.1.81
through
192.168.1.94
```

---

# Understanding /29

CIDR:

```text
/29
```

Mask:

```text
255.255.255.248
```

Magic Number:

```text
256 - 248 = 8
```

Host Bits:

```text
3
```

Hosts:

2^3-2

Result:

```text
6 hosts
```

---

# /29 Subnets

Count by 8:

```text
0
8
16
24
32
40
48
56
64
72
80
88
96
...
```

Example:

```text
192.168.1.40/29
```

Network:

```text
192.168.1.40
```

Broadcast:

```text
192.168.1.47
```

Hosts:

```text
192.168.1.41
through
192.168.1.46
```

---

# Quick Method for Any Question

Suppose you see:

```text
192.168.10.77/27
```

Step 1:

Determine mask:

```text
255.255.255.224
```

Step 2:

Magic Number:

```text
32
```

Step 3:

Count by 32:

```text
0
32
64
96
128
...
```

Step 4:

Find where 77 belongs:

```text
64 <= 77 < 96
```

Therefore:

Network:

```text
192.168.10.64
```

Broadcast:

```text
192.168.10.95
```

Host Range:

```text
192.168.10.65
to
192.168.10.94
```

---

# Real-World Example

Suppose a company needs:

| Department | Hosts |
| ---------- | ----- |
| HR         | 25    |
| Finance    | 20    |
| IT         | 10    |

Possible design:

```text
HR      /27
Finance /27
IT      /28
```

This conserves IP addresses while meeting requirements.

This concept later becomes:

```text
VLSM
```

which is heavily tested on CCNA.

---

# Common CCNA Mistakes

### Mistake #1

Forgetting to subtract 2.

Remember:

* Network Address
* Broadcast Address

cannot be assigned.

---

### Mistake #2

Using the wrong magic number.

Always calculate:

```text
256 - mask value
```

---

### Mistake #3

Confusing Network and Broadcast addresses.

Network:

First address

Broadcast:

Last address

---

# Memorization Table

| CIDR | Mask            | Hosts | Magic Number |
| ---- | --------------- | ----- | ------------ |
| /24  | 255.255.255.0   | 254   | 256          |
| /25  | 255.255.255.128 | 126   | 128          |
| /26  | 255.255.255.192 | 62    | 64           |
| /27  | 255.255.255.224 | 30    | 32           |
| /28  | 255.255.255.240 | 14    | 16           |
| /29  | 255.255.255.248 | 6     | 8            |

Memorizing this table will save you a huge amount of time during the CCNA exam.

---

# Practice Questions

## Question 1

IP:

```text
192.168.1.35/27
```

Find:

* Network Address
* Broadcast Address
* Host Range

Answer:

Network:

```text
192.168.1.32
```

Broadcast:

```text
192.168.1.63
```

Hosts:

```text
192.168.1.33
to
192.168.1.62
```

---

## Question 2

IP:

```text
10.0.0.150/28
```

Answer:

Network:

```text
10.0.0.144
```

Broadcast:

```text
10.0.0.159
```

Hosts:

```text
10.0.0.145
to
10.0.0.158
```

---

# What I Learned

Subnetting becomes much easier when using the Magic Number method. By identifying the subnet mask, calculating the magic number, and locating the correct subnet boundary, it is possible to quickly determine the network address, broadcast address, and host range for any IPv4 subnet.

---

# Summary

Subnetting is a fundamental networking skill. Understanding /27, /28, and /29 networks is essential for the CCNA exam and real-world network administration. The Magic Number method provides a fast and reliable way to solve subnetting questions and should become second nature through practice.
