import socket

from utils import fill_config, validate


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        print('Socket created')

        sock.bind(('localhost', 0))
        sock.listen()
        fill_config(port=sock.getsockname()[1])

        while True:
            conn, addr = sock.accept()
            print(f'Connected with {addr[0]}:{addr[1]}')

            user = conn.recv(1024).decode()
            print(f'username: {user}')

            valid = validate(user)
            conn.send(b'ok' if valid else b'not ok')
            print('validation completed')


if __name__ == '__main__':
    main()
