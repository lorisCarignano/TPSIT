from logging import exception
from pdb import Restart
from socket import AF_INET, SOCK_DGRAM, socket
from packet import Packet




def chatclient():
    
    with  socket(AF_INET, SOCK_DGRAM) as s:
        host="127.0.0.1"
        porta = 5005
        buf =4096
        indirizzo = (host,porta)
        try:
            nomeFile=input(str("inserisci nome file: "))
            f=open(nomeFile.strip(),"rb")
            s.sendto(nomeFile.encode("utf-8"),indirizzo)
        
            dati = f.read(buf)
            while (dati):
                if(s.sendto(dati,indirizzo)):
                    print ("sto inviando ...")
                    dati = f.read(buf)
            f.close()
        except FileNotFoundError:
            print("file non trovato")
            chatclient()
        
        



if __name__ == "__main__":
    chatclient()