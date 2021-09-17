def separar():
    maiorPalavra = ''
    maiorPalavraFrase = ''
    cont = 0
    while True:
        maiorNum = 0
        seq = ''
        frase = str(input('Informe uma frase: '))
        lista = frase.split()
        for x in lista:
            if(len(x) > maiorNum):
                maiorNum = len(x)
                maiorPalavraFrase = x
            seq = seq + '{}-'.format(len(x))
        seq = seq[:-1]
        print(seq)
        sair = str(input('Pressione qualquer tecla para continuar ou 0 para sair!'))
        if cont == 0:
            aux = maiorPalavraFrase
            if len(aux) > len(maiorPalavra):
                maiorPalavra = maiorPalavraFrase
        if len(maiorPalavraFrase) >= len(maiorPalavra):
            maiorPalavra = maiorPalavraFrase
        if sair == '0':
            print('Maior palavra: {}'.format(maiorPalavra))
            break
        cont += 1
separar()