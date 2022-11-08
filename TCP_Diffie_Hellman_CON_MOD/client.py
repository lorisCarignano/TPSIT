from socket import socket, AF_INET, SOCK_STREAM
import random
import time

p = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff
g = 2

def squareAndMuply(base, power):
    risultato = 1
    while power > 0:
        if power % 2 == 1:
            risultato = (risultato * base) % p

        power = power // 2
        base = (base * base) % p

    return risultato

def runClient():
    random.seed(2*int(time.time()))
    B = random.randint(1,p-2)

    gab = 0
    gb = squareAndMuply(g,B)
    #print("Random: "+ str(rand))
    #print("Gb: "+ str(gb))

    print("Sto calcolando...")

    with socket(AF_INET,SOCK_STREAM) as s:
        
        host = "127.0.0.1"
        port = 5000
        client = host,port

        s.connect(client)
        ga = int(s.recv(1048576))
        #print("Ga: " + str(ga))
        gab = squareAndMuply(ga,B)
        #print("Gab: "+ str(gab))
        s.send(str(gb).encode("utf-8"))
        gba = int(s.recv(1048576))
        
        if (gab == gba):
            s.send("segreto".encode("utf-8"))
            print("Messaggio segreto inviato!")
        else:
            print("Le chiavi non coincidono")

if __name__ == "__main__":
    runClient()