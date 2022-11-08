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

def runServer():
    random.seed(2*int(time.time()))
    A = random.randint(1,p-2)

    gab = 0
    ga = squareAndMuply(g,A)

    #print("Random: "+ str(rand))
    #print("Ga: "+ str(ga))

    with socket(AF_INET,SOCK_STREAM) as s:
        s.bind(("", 5000))
        s.listen(1)
        print("Server in ascolto!")
        while True:
            
            conn, addr = s.accept()
            conn.sendall(str(ga).encode("utf-8"))
            gb = int(conn.recv(1048576))

            gab = squareAndMuply(gb,A)
            #print("Gab: "+ str(gab))
            #print("Gb: " + str(gb))
            conn.sendall(str(gab).encode("utf-8"))
            
            print(conn.recv(1048576).decode())

if __name__ == "__main__":
    runServer()