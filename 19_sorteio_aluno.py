import random

#Sorteia um aluno aleatoriamente

print('\n\033[7;34;47m***SORTEIO DO ALUNO***\n')

a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o nome do segundo aluno: ')
c = input('Digite o nome do terceiro aluno: ')
d = input('Digite o nome do quarto aluno: ')

lista = [a, b, c, d]

sorteio = random.choice(lista)

print(f'\nO aluno {sorteio} foi escolhido\033[m\n')
