import random

numeros = []

def sortear(lista):
    for i in range(0,6):
        num = random.randint(1, 60)
        numeros.append(num)
    return numeros

print(sortear(numeros))


