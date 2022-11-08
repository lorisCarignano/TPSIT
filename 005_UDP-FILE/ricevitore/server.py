from logging import exception
from socket import AF_INET, SOCK_DGRAM, SOCK_STREAM, socket, timeout




def chatserver():
    
    
    with  socket(AF_INET, SOCK_DGRAM) as s:
        host ="0.0.0.0"
        porta = 5005
        s.bind((host,porta))
        indirizzo = (host,porta)
        buf=4096
        
        dati,indirizzo = s.recvfrom(buf)
        print ("File ricevuto:",dati.strip())
        f = open(dati.strip(),'wb')

        dati,indirizzo = s.recvfrom(buf)
        try:
            while(dati):
                f.write(dati)
                s.settimeout(2)
                dati,indirizzo = s.recvfrom(buf)
        except timeout:
            f.close()
            print("File Trasferito")
            


    
  


if __name__ == "__main__":
    chatserver()