import sys
from socket import socket, AF_INET, SOCK_STREAM
from random import randint
from math import log








def runClient():
    HOST = "127.0.0.1" 
    PORT = 5005
    p=8
    A=randint(1,p-2)
    
    g=2
    num=g**A

    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        
        msg="messaggio segretissimo"
        
        s.send(str(num).encode("utf-8"))
        
        numServer=int(s.recv(1024))
        
        chiaveClient=numServer**A
        print("A:",A)
        print("numClient:",num)
        print("numServer ",numServer)
        print(chiaveClient)
        chiaveServer=int(s.recv(1024))
        #print(chiaveServer)
        if(chiaveClient==chiaveServer):
            s.send(msg.encode("utf-8"))
            print("messaggio segreto mandato")


if __name__ == "__main__":
    runClient()
