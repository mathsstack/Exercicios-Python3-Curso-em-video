import random

#sorteia a ordem de apresentacão de um trabalho

print('\n\033[1;35;40m***SORTEIO DA ORDEM DE APRESENTACAO***\n')

a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o nome do segundo aluno: ')
c = input('Digite o nome do terceiro aluno: ')
d = input('Digite o nome do quarto aluno: ')

lista = [a, b, c ,d]

primeiro = random.choice(lista)
lista.remove(primeiro)
segundo = random.choice(lista)
lista.remove(segundo)
terceiro = random.choice(lista)
lista.remove(terceiro)
quarto = lista[0]

print(f'''\nO primeiro aluno será o {primeiro}
O segundo aluno será o {segundo}
O terceiro aluno será o {terceiro}
E o quarto aluno será o {quarto}\033[m\n''')


