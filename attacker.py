from scapy.all import *

spoofed_ip = "10.9.0.5"   # Pretend to be Server 1
target_ip = "10.9.0.6"    # Send to Server 2

packet = IP(src=spoofed_ip, dst=target_ip)/UDP(sport=9090, dport=9090)/b"PING"

send(packet)

print("Spoofed packet sent.")