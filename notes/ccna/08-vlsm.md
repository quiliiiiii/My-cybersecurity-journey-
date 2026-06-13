# CCNA Day 8 - VLSM (Variable Length Subnet Masking)

# Introduction

In previous subnetting lessons, every subnet was the same size.

For example:

```text
192.168.1.0/24
```

could be divided into:

```text
192.168.1.0/26
192.168.1.64/26
192.168.1.128/26
192.168.1.192/26
```

Each subnet contains:

```text
62 hosts
```

This works, but it is often wasteful.

Imagine a company where:

* HR needs 50 hosts
* IT needs 20 hosts
* Management needs 10 hosts

Giving each department 62 addresses wastes many IP addresses.

VLSM solves this problem.

---

# What is VLSM?

VLSM stands for:

```text
Variable Length Subnet Masking
```

It allows network administrators to create subnets of different sizes within the same network.

Instead of giving every subnet the same number of hosts, VLSM allows us to allocate addresses based on actual requirements.

Benefits:

* Better IP utilization
* Less waste
* Improved scalability
* More efficient network design

---

# Why VLSM Exists

Suppose we own:

```text
192.168.10.0/24
```

Total hosts:

```text
254
```

Department requirements:

| Department | Hosts Needed |
| ---------- | ------------ |
| HR         | 50           |
| IT         | 25           |
| Finance    | 12           |
| Management | 5            |

Without VLSM:

All departments receive:

```text
/26
```

Each gets:

```text
62 hosts
```

Result:

Many addresses wasted.

---

# VLSM Design Rule

Always subnet from:

```text
Largest
to
Smallest
```

This is one of the most important VLSM rules.

Never start with the smallest subnet.

---

# Step 1: Determine Required Subnet Sizes

Requirements:

```text
HR = 50 hosts
IT = 25 hosts
Finance = 12 hosts
Management = 5 hosts
```

Now determine the smallest subnet capable of supporting each group.

---

# HR Network

Needs:

```text
50 hosts
```

Possible subnets:

| CIDR | Hosts |
| ---- | ----- |
| /27  | 30    |
| /26  | 62    |

Choose:

```text
/26
```

Provides:

```text
62 hosts
```

---

# IT Network

Needs:

```text
25 hosts
```

Possible subnets:

| CIDR | Hosts |
| ---- | ----- |
| /28  | 14    |
| /27  | 30    |

Choose:

```text
/27
```

Provides:

```text
30 hosts
```

---

# Finance Network

Needs:

```text
12 hosts
```

Choose:

```text
/28
```

Provides:

```text
14 hosts
```

---

# Management Network

Needs:

```text
5 hosts
```

Choose:

```text
/29
```

Provides:

```text
6 hosts
```

---

# Step 2: Assign Networks

Starting network:

```text
192.168.10.0/24
```

Largest subnet first.

---

## HR

Subnet:

```text
192.168.10.0/26
```

Network:

```text
192.168.10.0
```

Broadcast:

```text
192.168.10.63
```

Hosts:

```text
192.168.10.1
to
192.168.10.62
```

---

## IT

Next available network:

```text
192.168.10.64
```

Subnet:

```text
/27
```

Network:

```text
192.168.10.64
```

Broadcast:

```text
192.168.10.95
```

Hosts:

```text
192.168.10.65
to
192.168.10.94
```

---

## Finance

Next available network:

```text
192.168.10.96
```

Subnet:

```text
/28
```

Network:

```text
192.168.10.96
```

Broadcast:

```text
192.168.10.111
```

Hosts:

```text
192.168.10.97
to
192.168.10.110
```

---

## Management

Next available network:

```text
192.168.10.112
```

Subnet:

```text
/29
```

Network:

```text
192.168.10.112
```

Broadcast:

```text
192.168.10.119
```

Hosts:

```text
192.168.10.113
to
192.168.10.118
```

---

# Final VLSM Design

| Department | Network        | CIDR | Hosts |
| ---------- | -------------- | ---- | ----- |
| HR         | 192.168.10.0   | /26  | 62    |
| IT         | 192.168.10.64  | /27  | 30    |
| Finance    | 192.168.10.96  | /28  | 14    |
| Management | 192.168.10.112 | /29  | 6     |

---

# Advantages of VLSM

## Efficient Address Usage

Only allocate addresses when needed.

---

## Better Network Planning

Supports future growth.

---

## Reduced Waste

Fewer unused addresses.

---

## Industry Standard

Most modern networks use VLSM.

---

# Common CCNA Exam Question

Given:

```text
10.10.10.0/24
```

Requirements:

```text
60 hosts
25 hosts
12 hosts
5 hosts
```

Question:

Design a VLSM addressing scheme.

Solution:

Always:

1. Sort largest to smallest
2. Find appropriate subnet size
3. Allocate sequentially
4. Calculate network and broadcast addresses

---

# Common Mistakes

## Mistake #1

Starting with the smallest subnet.

Wrong:

```text
5 hosts
12 hosts
25 hosts
60 hosts
```

Correct:

```text
60 hosts
25 hosts
12 hosts
5 hosts
```

---

## Mistake #2

Using subnet sizes that are too small.

Example:

Need:

```text
25 hosts
```

Choosing:

```text
/28
```

Wrong.

A /28 only supports:

```text
14 hosts
```

---

## Mistake #3

Overlapping Networks

Always verify that one subnet ends before the next begins.

---

# Real-World Example

A company may use:

```text
VLAN 10
HR

VLAN 20
Finance

VLAN 30
IT

VLAN 40
Management
```

Each VLAN receives a different subnet size depending on the number of users.

This is one of the most common uses of VLSM in enterprise environments.

---

# What I Learned

VLSM allows network engineers to allocate IP addresses efficiently by creating subnets of different sizes based on actual requirements. Instead of assigning equal subnet sizes to every department, VLSM helps reduce wasted addresses and supports scalable network design. The most important rule is to allocate networks from the largest requirement to the smallest.

---

# Summary

Variable Length Subnet Masking (VLSM) is a practical subnetting technique that allows multiple subnet sizes to exist within the same network. By carefully assigning subnet sizes according to host requirements, organizations can maximize address utilization and create more efficient network designs. VLSM is a fundamental skill for CCNA students and an essential concept in real-world networking.
