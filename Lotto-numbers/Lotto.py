from random import *

lista = []
new_set = set()
times = 0
while times < 10:
    for i in range(2):
        x = randrange(10, 19)
        while x in new_set:
            x = randrange(10, 19)
        new_set.add(x)
    for h_2 in range(2):
        y = randrange(20, 39)
        while y in new_set:
            y = randrange(20, 39)
        new_set.add(y)
        z = randrange(1, 10)
    while z % 2 != 0:
        z = randrange(1, 10)
    new_set.add(z)
    q = randrange(41, 49+1, 2)
    new_set.add(q)
    if new_set not in lista:
        lista.append(tuple(new_set))
        times += 1
    new_set.clear()
for i in lista:
    print("The Lotto numbers today are : ")
    print(i)
