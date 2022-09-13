from socket import AF_INET, SOCK_DGRAM, socket

def chatclient():
    with  socket(AF_INET, SOCK_DGRAM) as s:
        msg= "carig"
        msg = msg.encode()
        s.sendto(msg, ("192.168.95.255",5000))

if __name__ == "__main__":
    chatclient()