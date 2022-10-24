
from socket import AF_INET, SOCK_STREAM, socket


def run_server():
    with socket(AF_INET,SOCK_STREAM)as s:
        s.bind(("0.0.0.0",5000))
        s.listen()
        client,client_address=s.accept()
        data=client.recv()
        print(data)
