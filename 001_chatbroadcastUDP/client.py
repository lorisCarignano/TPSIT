from socket import AF_INET, SOCK_DGRAM, socket
from server import PORT
from packet import Packet

utente=str(input("inserisci il nome utente: "))
INDIRIZZO=str(input("inserisci il tuo indirizzo: "))


def chatclient():
    
    
    
    with  socket(AF_INET, SOCK_DGRAM) as s:
        while True:
            msg= input("chat: ")
            messaggio   =   Packet(utente,msg)
            messaggio = messaggio.to_bytes()
            s.sendto(messaggio, (INDIRIZZO,PORT))


    
  


if __name__ == "__main__":
    chatclient()