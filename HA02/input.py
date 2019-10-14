import sys
import time
from socket import *

if(len(sys.argv) != 6):
    print("Usage format: input.py <numberOfPorts> <baseValueOfPorts> <bufferSize in bytes> <UDP port of switching fabric> <transmitRate>\n")
    exit(1)

name=sys.argv[0]#file name
n= int(sys.argv[1]) #number of ports
b=int(sys.argv[2])  #base
buffer=int(sys.argv[3])   #buffersize
PS=int(sys.argv[4])   #UDP port of switchin fabric
T=sys.argv[5] # Transmit Rate

usn=56
ports=[]

t1=time.time()
for i in range(n):
    ports.append(b+100*i+usn) #assigning n no. of ports as per baseadress+100*N+USN

while True:
    for i in range(n):
        s = socket(AF_INET, SOCK_DGRAM)
        s.setsockopt(SOL_SOCKET,SO_RCVBUF,int(buffer))
        #s.settimeout(0.03)
        s.bind(('localhost',int(ports[i])))
        s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        data = s.recv(1024)
        if data:
            print(data.decode("ascii"),':',ports[i])
        s.close()
    if (time.time()-t1)>60: #if the receiver is active for more than 60 sec program terminates after every port is listened
        sys.exit(0)
