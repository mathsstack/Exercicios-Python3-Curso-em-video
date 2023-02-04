from math import trunc

#Lê um número e tira sua parte decimal

print('\n\033[4;33m***QUEBRADOR DE NÚMEROS***\n')

num = float(input('Digite um número: '))

print(f'\nA parte inteira do {num} é {trunc(num)}\033[m\n') 
