import socket

from utils import get_port


def main(name='Roma'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((socket.gethostbyname('localhost'), get_port()))
        sock.sendall(str.encode(name))
        print('Message sent successfully')
        reply = sock.recv(4096)
        return reply.decode()


if __name__ == '__main__':
    main()
