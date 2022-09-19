from socket import AF_INET, SO_BROADCAST, SOCK_DGRAM, socket
from ssl import SOL_SOCKET   #usiamo from cosi ogni volta non dobbiamo scrivere socket.---



BUFFER_SIZE = 1024
PORT=int(input("inserisci una porta: "))

HOST = "0.0.0.0"

exit=False
# possibilità 
# localhost 127.0.0.1 / 0.0.0.0 da tutte le fonti

def chatserver(HOST,PORT):
    with  socket(AF_INET, SOCK_DGRAM) as s:  #usiamo with cosi si chiude in automatico
        s.bind((HOST, PORT))  
        while exit==False:
            
            msg = s.recvfrom(BUFFER_SIZE)
            
            msg = msg[0].decode()
            print(msg)

if __name__ == "__main__":
    chatserver(HOST,PORT)