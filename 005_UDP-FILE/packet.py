class Packet:
    NEW_FILE = 0
    GO_ON = 1
    END_FILE = 2
   
    def __init__(self, status, data):
        
        self.status = status
        self.data = data

    def to_bytes(self): 
        
        status = self.status.to_bytes(1,"big")
        size = len(self.data)
        size = size.to_bytes(2,"big")
        buffer = status + size + self.data

        return buffer
    
    @staticmethod 
    def from_bytes(buffer):

        status = int.from_bytes(buffer[:1],"big")
        size = int.from_bytes(buffer[1:3],"big")
        data = buffer[3:3]

        return Packet(status, data)