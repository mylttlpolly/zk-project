import configparser
import socket

from Crypto.Hash import MD5
from Crypto.PublicKey import RSA

from utils import db


def main(port=8080):
    print(db['example'])
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        with open('mykey.pem', 'r') as f:
            key = RSA.importKey(f.read())

        pub = RSA.generate(2048).publickey()

        with open('cl1key.pem', 'wb') as f:
            f.write(pub.exportKey('PEM'))

        sock.connect((socket.gethostbyname('localhost'), port))

        d = sock.recv(4096)
        e = int.from_bytes(d, 'big')

        h = MD5.new(b'test message')
        g = h.digest()
        x = key.encrypt((g * e), 1)

        sock.sendall((x[0]))

        print('Message sent successfully')

        reply = sock.recv(4096)
        print(reply.decode())


if __name__ == '__main__':
    parser = configparser.ConfigParser()
    parser.read('config.ini')
    main(int(parser['DEFAULT']['port']))
