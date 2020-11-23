import socket
import random
import math


class Server:
    def __init__(self):
        self.num = random.randint(1, 1000000)
        self.sock = socket.socket()
        self.port = 1049
        self.sock.bind(('', self.port))
        print(f'socket binded to {self.port}')
        print(f'num is {self.num}')
        self.sock.listen(10)
        print('Socket is listening')
        self.conn, self.addr = self.sock.accept()
        with self.conn:
            print(f'Connected by {self.addr}')
            self.data = self.conn.recv(1024)
            if self.data == b'WHO':
                self.conn.send(b'CHEPIK ANDRIY VARIANT-26; \n '
                               b'TASK: CREATE DYHOTOMIA AND GOLDEN RATION SEARCHING PROGRAMS BASED ON SOCKETS')
            if self.data == b'D':
                self.dyhotomia()
            if self.data == b'G':
                self.golden_ratio()

    def dyhotomia(self):
        if self.data == b'D':
            self.conn.send(b'D')
        while True:
            self.data = self.conn.recv(1024)
            data = int.from_bytes(self.data, byteorder='big')
            if not data:
                print('socket disconnected')
                break
            if data < self.num:
                self.conn.send(b'MORE')
            if data > self.num:
                self.conn.send(b'LESS')
            if data == self.num:
                self.conn.send(b'YES')

    def golden_ratio(self):
        if self.data == b'G':
            self.conn.send(b'G')
        while True:
            self.data = self.conn.recv(1024)
            data = int.from_bytes(self.data, byteorder='big')
            if not data:
                print('socket disconnected')
                break
            if data < self.num:
                self.conn.send(b'MORE')
            if data > self.num:
                self.conn.send(b'LESS')
            if data == self.num:
                self.conn.send(b'YES')


if __name__ == '__main__':
    server = Server()

