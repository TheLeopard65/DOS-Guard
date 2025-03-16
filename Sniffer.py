import scapy.all as scapy

i = 1
def printer(packet):
    if scapy.IP in packet:
        ip_layer = packet[scapy.IP]
        global i
        print(f"{i} :: PACKET ID = {ip_layer.id} && SOURCE = {ip_layer.src} >> DESTINATION = {ip_layer.dst} && PAYLOAD = {packet[scapy.Raw].load}")
        i += 1

scapy.sniff(prn=printer)
