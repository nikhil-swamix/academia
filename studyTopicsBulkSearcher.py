import selenium
from mxproxy import mx

filename='ComputerNetworksEndsem'
filesuffix='.html'

syllabusstring='''Error detection and Error correction – VRC, LRC,
CRC, Stop and Wait Protocol, Sliding Window Protocol, Go-back-n ARQ,
Selective-Reject ARQ, HDLC, Channel Allocation, ALOHA Systems, CSMA Protocols,
Collision Free Protocols, Local Area Networks, Bridges, ATM, Routing: Flooding,
Spanning tree, Distance Vector routing, Link state routing, Bellman-Ford and
Dijkstra routing algorithms, Congestion control - Leaky Bucket and Token Bucket
algorithms , IP Protocol, IP Addressing, ARP, RARP, OSFP, BGP, TCP, UDP,
Application Protocols-DHCP, DNS, Telnet, SMPT, Network Security-RSA.'''
syllabusstring=syllabusstring.replace('\n','')

coursesuffix='in computer networks'
print(syllabusstring.split(','))