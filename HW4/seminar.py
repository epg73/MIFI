import scapy.all as scapy

scapy.arping('192.168.1.0/24')
a= scapy.get_if_addr('en0')
print(a)


