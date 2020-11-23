import math, random

num = random.randint(0, 1000000)
print(num)

fi = (1+math.sqrt(5))/2
a = 0
b = 1000000

while True:
    x1 = round(b - ((b - a) / fi))
    x2 = round(a + ((b - a) / fi))
    if num == x1:
        print(f'num is {x1}')
        break
    if num == x2:
        print(f'num is {x2}')
        break
    if num < x1:
        b = x1
    elif num > x2:
        a = x2
    else:
        a = x1
        b = x2
