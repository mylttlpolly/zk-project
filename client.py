import configparser
import socket

from utils import db


def main(port=8080):
    print(db['example'])
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((socket.gethostbyname('localhost'), port))

        sock.sendall(b'Polina;123')
        print('Message sent successfully')

        reply = sock.recv(4096)
        print(reply.decode())


if __name__ == '__main__':
    parser = configparser.ConfigParser()
    parser.read('config.ini')
    main(int(parser['DEFAULT']['port']))
