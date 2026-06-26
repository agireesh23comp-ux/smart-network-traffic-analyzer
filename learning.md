# Smart Network Traffic Analyzer & Threat Detection System

---

# Day 1 - Reading a PCAP File

## Concepts Learned

### 1. What is a Packet?
A packet is the smallest unit of data transmitted over a network. When we browse the internet, our data is broken into packets before being sent.

### 2. What is a PCAP File?
A PCAP (Packet Capture) file stores captured network packets. It is like a recording of all network communication.

### 3. Scapy
Scapy is a Python library used for packet manipulation and analysis.

### 4. rdpcap()
The rdpcap() function reads a PCAP file and loads all packets into Python.

### 5. Variables
Variables store data in memory.

Example:
packets = rdpcap("sample1.pcap")

### 6. len()
len() returns the total number of packets.

Result:
6067 packets loaded successfully.

---

# Day 2 - Exploring Packets

## Goal
Instead of only counting packets, inspect the packets one by one.

---

## Concepts Learned

### 1. for Loop

A for loop is used to iterate through every item in a collection.

Example

for fruit in fruits:
    print(fruit)

In this project:

for packet in packets:

means

"Take one packet at a time from the packets collection."

---

### 2. Packet Object

Every packet inside the packets variable is an object.

Example

Packet 1

Packet 2

Packet 3

Each packet contains information such as

- Ethernet Header
- IP Header
- TCP/UDP Header
- Payload

---

### 3. Packet Collection

The variable

packets

does not store a single packet.

It stores thousands of packets.

Example

packets

├── Packet 1
├── Packet 2
├── Packet 3
├── Packet 4
└── ...

---

### 4. Slicing

packets[:5]

returns only the first five packets.

Syntax

packets[start:end]

Examples

packets[:5] → First 5 packets

packets[5:10] → Packets 6–10

packets[-1] → Last packet

---

### 5. enumerate()

Normally

for packet in packets:

only gives the packet.

Using

enumerate()

gives

Packet Number

Packet

Example

1 → Packet 1

2 → Packet 2

3 → Packet 3

Syntax

for i, packet in enumerate(packets[:5], start=1):

i = Packet Number

packet = Actual Packet

---

### 6. print()

print(packet)

displays a summary of the current packet.

---

### 7. String Multiplication

Example

print("-" * 40)

Python repeats the "-" character forty times.

Output

----------------------------------------

It is used only to make the output easier to read.

---

## Program Flow

Read PCAP

↓

Store all packets

↓

Take first five packets

↓

Loop through packets

↓

Print packet summary

↓

Display separator

---

## Output Example

Reading PCAP...

Total Packets: 6067

Packet 1

Ether / IP / TCP ...

----------------------------------------

Packet 2

Ether / IP / UDP ...

----------------------------------------

---

## Key Takeaways

✓ Learned how a for loop works.

✓ Learned how to inspect packets one by one.

✓ Learned packet slicing.

✓ Learned enumerate().

✓ Learned string multiplication.

✓ Printed the first five packets from a PCAP file.

| Protocol Number | Protocol    |
| --------------- | ----------- |
| **1**           | ICMP        |
| **6**           | TCP         |
| **17**          | UDP         |
| **47**          | GRE         |
| **50**          | ESP (IPsec) |
| **51**          | AH (IPsec)  |
| **89**          | OSPF        |
# Smart Network Traffic Analyzer & Threat Detection System

---

# Day 3 - Packet Inspection

## Goal

Learn how to inspect individual packets inside a PCAP file.

---

## Concepts Learned

### 1. Network Packet

A packet is the smallest unit of data transmitted over a network.

A packet contains multiple layers.

Example

Ethernet
↓

IP
↓

TCP/UDP
↓

Application Data

---

### 2. IP Layer

The IP layer contains:

- Source IP Address
- Destination IP Address
- Protocol Number

Example

Source IP      : 192.168.1.5

Destination IP : 142.250.183.78

Protocol        : 6

---

### 3. haslayer()

Syntax

packet.haslayer(IP)

Purpose

Checks whether the current packet contains an IP layer.

Without this check, Python may throw an error if the packet is ARP or another non-IP protocol.

---

### 4. Accessing Packet Fields

Source IP

packet[IP].src

Destination IP

packet[IP].dst

Protocol Number

packet[IP].proto

Packet Length

len(packet)

---

### 5. Difference Between packets and packet

packets

- Collection of all packets inside the PCAP file.

packet

- A single packet taken from the packets collection during iteration.

Example

for packet in packets:

Python processes one packet at a time.

---

### 6. enumerate()

Syntax

for i, packet in enumerate(packets[:5], start=1):

Purpose

Provides both

- Packet Number (i)
- Packet Object (packet)

---

### 7. Packet Length

Syntax

len(packet)

Returns the size of one packet in bytes.

Example

74 Bytes

1514 Bytes

512 Bytes

---

## Program Flow

Read PCAP

↓

Loop through packets

↓

Check IP Layer

↓

Extract Source IP

↓

Extract Destination IP

↓

Extract Packet Length

↓

Display Packet Information

---

## Key Takeaways

✓ Understood packet structure.

✓ Learned how to access packet fields.

✓ Learned packet iteration.

✓ Learned packet length.

✓ Learned difference between packets and packet.
---

# Day 4 - Protocol Analysis

## Goal

Count how many packets belong to each protocol.

---

## Concepts Learned

### 1. Protocol Number

Every IP packet contains a Protocol field.

This number tells the operating system what protocol comes after the IP header.

Examples

1  → ICMP

6  → TCP

17 → UDP

These numbers are standardized by IANA (Internet Assigned Numbers Authority).

---

### 2. Protocol Mapping

Instead of displaying numbers,

convert them into readable names.

Example

6

↓

TCP

17

↓

UDP

1

↓

ICMP

---

### 3. Dictionary

A dictionary stores information as

Key → Value

Example

{
    "TCP": 79,
    "UDP": 5986,
    "ICMP": 2
}

Key

Protocol Name

Value

Number of Packets

---

### 4. Empty Dictionary

Syntax

protocol_count = {}

Purpose

Create an empty dictionary before processing packets.

---

### 5. Counting Packets

Syntax

protocol_count[protocol] = protocol_count.get(protocol, 0) + 1

Explanation

Step 1

Check whether the protocol already exists.

Example

TCP

↓

Exists?

↓

Yes

↓

Current Count = 79

↓

79 + 1

↓

80

If it doesn't exist

TCP

↓

No

↓

Default Value = 0

↓

0 + 1

↓

1

---

### 6. Dictionary.get()

Syntax

dictionary.get(key, default_value)

Example

protocol_count.get("TCP", 0)

If TCP exists

↓

Return current value

Otherwise

↓

Return 0

---

### 7. Dictionary.items()

Syntax

for protocol, count in protocol_count.items():

Purpose

Returns both

Key

and

Value

Example

TCP → 79

UDP → 5986

ICMP → 2

---

### 8. Two Different Loops

Loop 1

Purpose

Inspect packets.

Example

for packet in packets[:5]

Only first five packets.

Loop 2

Purpose

Count protocols.

Example

for packet in packets

Processes every packet inside the PCAP file.

---

## Program Flow

Read PCAP

↓

Create Empty Dictionary

↓

Loop Through All Packets

↓

Check IP Layer

↓

Read Protocol Number

↓

Convert Number to Protocol Name

↓

Increase Count

↓

Print Final Statistics

---

## Output Example

Reading PCAP...

Total Packets : 6067

Protocol Analysis

UDP : 5986

TCP : 79

ICMP : 2

---

## Key Takeaways

✓ Learned IP Protocol Numbers.

✓ Learned dictionaries.

✓ Learned dictionary.get().

✓ Learned dictionary.items().

✓ Counted protocols.

✓ Understood why packet inspection and protocol analysis use separate loops.

# Day 5 - Top Talkers Analysis

## Goal

Identify the devices sending and receiving the most network traffic.

---

## Concepts Learned

### 1. Source IP

The IP address that sends a packet.

Example:

192.168.0.146

Access using:

packet[IP].src

---

### 2. Destination IP

The IP address that receives a packet.

Example:

49.44.76.49

Access using:

packet[IP].dst

---

### 3. Dictionary Counting

A dictionary stores data in the form:

Key → Value

Example:

{
    "192.168.0.146": 5188,
    "49.44.76.49": 664
}

To increase the count:

dictionary[key] = dictionary.get(key, 0) + 1

The .get() method:
- Returns the current value if the key exists.
- Returns 0 if the key does not exist.

---

### 4. Source IP Counter

Dictionary:

source_ip_count = {}

Stores:

Source IP → Packet Count

Example:

{
    "192.168.0.146": 854
}

---

### 5. Destination IP Counter

Dictionary:

destination_ip_count = {}

Stores:

Destination IP → Packet Count

Example:

{
    "192.168.0.146": 5188
}

---

### 6. .items()

Returns both the key and value of a dictionary.

Example:

dictionary.items()

Output:

("192.168.0.146", 5188)

("49.44.76.49", 664)

---

### 7. sorted()

Used to sort a dictionary.

Syntax:

sorted(dictionary.items())

---

### 8. key=lambda item:item[1]

Each dictionary item looks like:

("192.168.0.146", 5188)

Index 0 → IP Address

Index 1 → Packet Count

item[1] means:

Sort using the packet count.

---

### 9. reverse=True

Sorts from largest value to smallest value.

Without reverse=True:

10
20
30

With reverse=True:

30
20
10

---

### 10. Slicing

sorted_source[:5]

Returns only the first five results.

---

### 11. f-String Formatting

Example:

print(f"{'IP Address':<20} {'Packets'}")

<20 means reserve 20 spaces.

Output:

IP Address          Packets
-------------------------------
192.168.0.146       5188

---

### 12. Top Talkers

Top Source IP

The device sending the most packets.

Top Destination IP

The device receiving the most packets.

SOC analysts use this to identify:

• Malware
• Port Scans
• DDoS
• Data Exfiltration
• Unusual Network Activity

---

## Python Concepts Learned

✓ Dictionary

✓ .get()

✓ .items()

✓ sorted()

✓ reverse=True

✓ lambda (basic understanding)

✓ f-string formatting

---

## Cybersecurity Concepts Learned

✓ Source IP

✓ Destination IP

✓ Top Talkers Analysis

✓ Packet Counting

✓ Traffic Analysis
📖 LEARNING.md (Day 6)
# Day 6 - DNS Analysis

## Goal

Extract the domain names requested in the PCAP file.

Example:

google.com

youtube.com

github.com

---

## Concepts Learned

### 1. DNS

DNS stands for

Domain Name System.

It converts:

Domain Name

↓

IP Address

Example:

google.com

↓

142.250.xxx.xxx

---

### 2. DNS Layer

Check whether a packet contains DNS.

Syntax:

packet.haslayer(DNS)

Returns:

True

or

False

---

### 3. DNS Question Record (DNSQR)

DNS packets contain different sections.

Question Section

↓

Stores the requested domain.

Check using:

packet.haslayer(DNSQR)

---

### 4. qname

Returns the requested domain.

Example:

packet[DNSQR].qname

Output:

b'google.com.'

Notice:

The value is stored as bytes.

---

### 5. decode()

Converts bytes into readable text.

Example:

b'google.com.'

↓

google.com.

Syntax:

.decode()

---

### 6. rstrip()

Removes characters from the end of a string.

Example:

google.com.

↓

google.com

Syntax:

domain.rstrip(".")

---

### 7. Domain Counter

Dictionary:

domain_count = {}

Stores:

Domain Name → Request Count

Example:

{
    "google.com": 12,
    "youtube.com": 8
}

---

### 8. Reverse DNS

Sometimes computers ask:

IP Address

↓

Host Name

Example:

192.168.0.126

↓

192.168.0.126.in-addr.arpa

This is called a Reverse DNS Lookup.

---

### 9. Forward DNS

Normal DNS works as:

google.com

↓

142.250.xxx.xxx

This is called a Forward Lookup.

---

### 10. Why Only Reverse DNS Appeared?

Modern browsers often use:

• DNS Cache
• DNS over HTTPS (DoH)
• HTTP/3 (QUIC)

Because of this, normal DNS packets may not appear in Wireshark.

Your code is still correct.

---

## Python Concepts Learned

✓ packet.haslayer()

✓ DNS

✓ DNSQR

✓ qname

✓ decode()

✓ rstrip()

✓ Dictionary Counting

✓ sorted()

---

## Cybersecurity Concepts Learned

✓ DNS

✓ Domain Resolution

✓ Forward DNS

✓ Reverse DNS

✓ DNS Requests

✓ DNS Packet Analysis

---

## Real World Use Cases

SOC Analysts use DNS Analysis to:

✓ Detect malware communication

✓ Find suspicious domains

✓ Identify Command & Control (C2) servers

✓ Investigate phishing websites

✓ Analyze browsing activity

✓ Perform threat hunting