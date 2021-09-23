def primo(p):
    contador = 0
    for i in range(1, p + 1):
        if p % i == 0:
            contador = contador + 1
    if contador == 2:
        return True
    else:
        return False

def somaPrimos(n):
    cont = 1
    soma = 0
    primos = 0
    while True:
        if primo(cont) == True:
            soma += cont
            primos += 1
        if(primos == n):
            print('A soma dos {} primeiros números inteiros é: {}'.format(n, soma))
            break
        cont += 1

somaPrimos(3)
somaPrimos(7)
somaPrimos(100)