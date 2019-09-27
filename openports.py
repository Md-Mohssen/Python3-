#! /usr/local/bin/python3
import socket
import time
start = time.time()
#s = input('enter the Host name to scan\n: ')
rmip = '192.168.10.30'
portlist = [21,23,80,135,443,8080,8020,8022,9200]
for port in portlist:
    sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result = sock.connect_ex((rmip,port))
    if result == 0:
        print(port,": OPEN")
    else:
        print(port, "error no.:", result)
    sock.close()
print("Time of scan %.2f"% ( time.time() - start))
      
