from socket import *

IP = "0.0.0.0"
PORT = 9090

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind((IP, PORT))

print("UDP Server listening on port 9090...")

while True:
    data, addr = sock.recvfrom(1024)
    print("Received:", data, "from", addr)
    
    # Vulnerable: automatically echo back
    sock.sendto(data, addr)