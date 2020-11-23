import socket
import math
import sys
import time

s = socket.socket()

port = 1049

s.connect(('127.0.0.1', port))

def dyhotomia():
    num = 500000
    inc = 500000
    start = time.time()
    print(start)
    s.send(num.to_bytes(3, 'big'))
    data = s.recv(1024).decode('utf-8')
    i = -1
    while True:
        i += 1
        if data == 'YES':
            waiting = time.time() - start
            print(f'NUMBER IS {num}')
            print(f'NUMBER OF ITERATIONS IS {i}')
            print(f'TIME IS {waiting}')
            break
        if data == 'MORE':
            num += round(inc // 2)
        elif data == 'LESS':
            num -= round(inc // 2)
        inc = round(inc // 2)
        if inc == 1:
            inc += 1
        s.send(num.to_bytes(3, 'big'))
        data = s.recv(1024).decode('utf-8')
        print(data)

def golden_ratio():
    fi = (1 + math.sqrt(5)) / 2
    a = 0
    b = 1000000
    i = 0
    start = time.time()
    while True:
        x1 = round(b - ((b - a) / fi))
        x2 = round(a + ((b - a) / fi))
        s.send(x1.to_bytes(3, 'big'))
        i += 1
        data = s.recv(1024).decode('utf-8')
        if data == 'YES':
            waiting = time.time() - start
            print(f'NUMBER IS {x1}')
            print(f'NUMBER OF ITERATIONS IS {i}')
            print(f'TIME IS {waiting}')
            break
        if data == 'LESS':
            b = x1
        elif data == 'MORE':
            s.send(x2.to_bytes(3, 'big'))
            i += 1
            data = s.recv(1024).decode('utf-8')
            if data == 'YES':
                waiting = time.time() - start
                print(f'NUMBER IS {x2}')
                print(f'NUMBER OF ITERATIONS IS {i}')
                print(f'TIME IS {waiting}')
                break
            if data == 'MORE':
                a = x2
            else:
                a = x1
                b = x2
        print(data)

param = sys.argv[1]
s.send(bytes(param, 'utf-8'))

data = s.recv(1024).decode('utf-8')
if data == 'D':
    dyhotomia()
elif data == 'G':
    golden_ratio()
else:
    print(data)



