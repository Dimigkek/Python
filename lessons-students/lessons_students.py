from random import *
N = 24
lista = []
lista_temp = []
mathites = {mathitis for mathitis in range(1,N+1)}
i = 0
o = 0

for o in range(2):

    while i < int(N/2):
        for c in range(2):
            x = randrange(1, N + 1)
            while x not in mathites:
                x = randrange(1, N + 1)
            lista_temp.append("Mathitis "+ str(x))
            mathites.remove(x)
        lista.append(tuple(lista_temp))
        lista_temp.clear()
        i += 1
    if o == 0:
        print("Ta zeugaria gia to mathima Mathimatika einai einai : " + str(lista))
        lista.clear()
        mathites = {mathitis for mathitis in range(1, N + 1)}
        i = 0
    else:
        print("Ta zeugaria gia to mathima Geografia einai einai : " + str(lista))
