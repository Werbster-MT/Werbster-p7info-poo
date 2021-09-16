def printDecimal(num):
   return str('%d' % num)

def printOctal(num):
   return str('%o' % num)

def printHexaDecimal(num):
   return str('%x' % num)

def printBinario(num):
   return str('{0:b}'.format(num, 'binary'))

def linha():
   print('-' * 88)

def imprimirTabela():
   linha()
   print('|{:^20s}||{:^20s}||{:^20s}||{:^20s}|'.format('Decimal', 'Octal', 'Hexadecimal', 'Binário'))
   linha()
   for i in range(0, 256):
      print('|{:^20s}||{:^20s}||{:^20s}||{:^20s}|'.format(printDecimal(i), printOctal(i), printHexaDecimal(i), printBinario(i)))
      linha()

imprimirTabela()