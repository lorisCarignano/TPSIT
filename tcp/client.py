from socket import AF_INET, SOCK_STREAM, socket


def run_client(receiver):
    with socket(AF_INET, SOCK_STREAM)as s:
        s.connect(receiver)
        s.send(b"avanti;3")
