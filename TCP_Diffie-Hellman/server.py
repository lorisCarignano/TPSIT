#!/usr/bin/env python
import sys
from socket import socket, AF_INET, SOCK_STREAM
from random import randint
from math import log




def runServer():
    
    PORT=5005
    p=8
    B=randint(1,p-2)
    
    g=2
    num=str(g**B)

    with socket(AF_INET, SOCK_STREAM) as s:
        
        s.bind(("0.0.0.0", PORT))
        s.listen(1)
        print("in ascolto")
        while 1:
            
            conn, addr = s.accept()
        
            numClient=int(conn.recv(1024))
            


            conn.sendall(str(num).encode("utf-8"))
            chiaveServer=numClient**B
            print("B: ",B)
            print("numClient ",numClient)
            print("numServer ",num)
            print(chiaveServer)
            
            conn.sendall(str(chiaveServer).encode("utf-8"))
            msg=conn.recv(1024).decode("utf-8")
            print(msg)
            

        


if __name__ == "__main__":
    runServer()
