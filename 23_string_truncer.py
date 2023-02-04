#Decompõe um número através de manipulação de strings

print('\n\033[37m***STRING TRUNCER***\n')

number = '0001'
num = input('Digite um número de 0 a 9999: ')

number = number.replace('1', num)
tam = len(number) - 1

print(f'''\nUnidade: {number[tam]}
Dezena: {number[tam - 1]}
Centena: {number[tam - 2]}
Unidade de milhar: {number[tam - 3]}\033[m\n''')


