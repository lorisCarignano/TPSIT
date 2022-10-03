# 1 byte (username) | username | 2 byte (message) | message

class Packet:
    def __init__(self, username, message):
        #validazione
        self.username= username
        self.message= message

    def to_bytes(self):  #converte un oggetto packet in bytes
        
        username_bytes= self.username.encode()
        buffer=len(username_bytes).to_bytes(1, "big")   # l'1 indica quanti byte utilizzare
        buffer = buffer + username_bytes
        
        message_bytes = self.message.encode()
        buffer= buffer + len(message_bytes).to_bytes(2, "big")   # l'1 indica quanti byte utilizzare
        buffer = buffer + message_bytes
        return buffer
    @staticmethod #lo rendiamo statico come se fosse un main
    def from_bytes(buffer):
        username_size = int.from_bytes(buffer[0:1], 'big')
        username= buffer[1:username_size+1].decode()
        
        message_size = int.from_bytes(buffer[username_size+1:username_size+3], 'big')
        message= buffer[username_size+3:username_size+3+message_size].decode()
        return Packet(username, message)

def run_test():
    pkt0= Packet("user", "message")
    pkt1= Packet.from_bytes(pkt0.to_bytes())

    assert(pkt0.message==pkt1.message)
    assert(pkt0.username==pkt1.username)

    
if __name__ == "__main__":
    run_test()

