from socket import *
import time

host = "localhost"
port = 7777
sock = ( host, port )

key = "school"
id2 = "3a4a5a"
s_id = ""
s_pw = ""

alpa = "!@#$%^&*()-_=+\|`~0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for a in range(len(alpa)):
    id2 = list(id2)
    id2[4] = alpa[a]
    for i in range(len(id2)):
        s_id += id2[i]

    for i in range(0,6):
        s_pw += chr(ord(s_id[i]) ^ ord(key[i]))

    s = socket(AF_INET, SOCK_STREAM)
    s.connect(sock)

    s.recv(1024)
    s.send(s_id + "\n")
    
    s.recv(1024)
    s.send(s_pw + "\n")
    
    s.recv(1024)
    time.sleep(0.1)
    ch = s.recv(1024)
    if ch.find("687b8") > 1:
        print ch
        print s_id
        break
    
    s_id = ""
    s_pw = ""
    s.close()
