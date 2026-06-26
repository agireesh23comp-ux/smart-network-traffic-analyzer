from scapy.all import rdpcap, IP, TCP, UDP, ICMP, DNS

# =====================================================
# Read PCAP File
# =====================================================

packets = rdpcap("sample_pcaps/sample2.pcap")

print("Reading PCAP...")
print("Total Packets:", len(packets))
print()

# =====================================================
# Variables
# =====================================================

ftp_detected = False
telnet_detected = False

icmp_count = 0
dns_count = 0

# Dictionary for Port Scan Detection
# Key   -> Source IP
# Value -> Set of destination ports

ip_ports = {}

# =====================================================
# Read Every Packet
# =====================================================

for packet in packets:

    # =================================================
    # TCP Analysis
    # =================================================

    if packet.haslayer(TCP):

        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport

        # FTP Detection
        if source_port == 21 or destination_port == 21:
            ftp_detected = True

        # Telnet Detection
        if source_port == 23 or destination_port == 23:
            telnet_detected = True

        # TCP Port Scan Detection
        if packet.haslayer(IP):

            source_ip = packet[IP].src

            if source_ip not in ip_ports:
                ip_ports[source_ip] = set()

            ip_ports[source_ip].add(destination_port)

    # =================================================
    # UDP Analysis (For Port Scan)
    # =================================================

    elif packet.haslayer(UDP):

        if packet.haslayer(IP):

            source_ip = packet[IP].src
            destination_port = packet[UDP].dport

            if source_ip not in ip_ports:
                ip_ports[source_ip] = set()

            ip_ports[source_ip].add(destination_port)

    # =================================================
    # ICMP Detection
    # =================================================

    if packet.haslayer(ICMP):
        icmp_count += 1

    # =================================================
    # DNS Detection
    # =================================================

    if packet.haslayer(DNS):
        dns_count += 1

# =====================================================
# Thresholds
# =====================================================

ICMP_THRESHOLD = 100
DNS_THRESHOLD = 100
PORT_SCAN_THRESHOLD = 20

# =====================================================
# Threat Detection Report
# =====================================================

print("=" * 60)
print("                THREAT DETECTION REPORT")
print("=" * 60)

# FTP

if ftp_detected:
    print("⚠ FTP Traffic            : DETECTED")
else:
    print("✓ FTP Traffic            : Not Detected")

# Telnet

if telnet_detected:
    print("⚠ Telnet Traffic         : DETECTED")
else:
    print("✓ Telnet Traffic         : Not Detected")

# ICMP

if icmp_count > ICMP_THRESHOLD:
    print(f"⚠ ICMP Flood             : DETECTED ({icmp_count} packets)")
else:
    print(f"✓ ICMP Flood             : Normal ({icmp_count} packets)")

# DNS

if dns_count > DNS_THRESHOLD:
    print(f"⚠ DNS Flood              : DETECTED ({dns_count} packets)")
else:
    print(f"✓ DNS Flood              : Normal ({dns_count} packets)")

# =====================================================
# Port Scan Detection
# =====================================================

port_scan_found = False

for ip, ports in ip_ports.items():

    if len(ports) >= PORT_SCAN_THRESHOLD:

        port_scan_found = True

        print()
        print("⚠ POSSIBLE PORT SCAN DETECTED")
        print(f"Source IP              : {ip}")
        print(f"Unique Destination Ports : {len(ports)}")
        print("Ports:")
        print(sorted(ports))
        print("-" * 60)

if not port_scan_found:
    print("✓ Port Scan             : Not Detected")