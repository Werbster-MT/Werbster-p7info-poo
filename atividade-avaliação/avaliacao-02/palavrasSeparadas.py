def linhaTracejada():
    print('-' * 103)

def tabela(lista):
    linhaTracejada()
    print('|{:^50s}|{:^50s}|'.format('Exemplo de Entrada', 'Exemplo de Saída'))
    linhaTracejada()
    for i in range(0, len(lista) - 1):
        print('|{:^50s}|{:^50s}|'.format(lista[i][0], lista[i][1]))
    linhaTracejada()

def separar():
    maiorPalavra = ''
    maiorPalavraFrase = ''
    cont = 0
    linha = []
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

        if cont == 0:
            maiorPalavra = maiorPalavraFrase

        if len(maiorPalavraFrase) >= len(maiorPalavra):
            maiorPalavra = maiorPalavraFrase

        linha.append([frase, seq])

        if frase == '0':
            tabela(linha)
            print('Maior palavra: {}'.format(maiorPalavra))
            break
        cont += 1

separar()