import socket
from random import randint

from Crypto.PublicKey import RSA

from utils import fill_config


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        print('Socket created')

        key = RSA.generate(2048)
        pub = key.publickey()

        with open('mykey.pem', 'wb') as f:
            f.write(pub.exportKey('PEM'))

        sock.bind(('localhost', 0))
        sock.listen()
        fill_config(port=sock.getsockname()[1])

        nons = {k: randint(0, 9) for k in (0, 1)}

        while True:
            answer = {k: None for k in (0, 1)}
            conn = {k: None for k in (0, 1)}

            with open('cl1key.pem', 'r') as f:
                cl1key = RSA.importKey(f.read())

            for i in answer:
                conn[i], addr = sock.accept()
                conn[i].send(bytes([nons[i]]))
                data = (conn[i].recv(1024))
                print(f'Connected with {addr[0]}:{addr[1]}')
                answer[i] = key.decrypt(data)

            response = b'equal' if answer[0] * nons[1] == answer[1] * nons[0] else b'not equal'
            for i in answer:
                conn[i].send(response)
            print('END')


if __name__ == '__main__':
    main()
