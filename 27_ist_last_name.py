#Mostra o primeiro e o último nome de alguém

print('\n\033[7;37m***WHAT IS THE 1ST AND THE LAST NAME***\n')

nome = input('Digite seu nome completo: ')

nome = nome.split()
ult = len(nome) - 1

print(f'''\nO primeiro nome é {nome[0]}
O ultimo nome é {nome[ult]}\033[m\n''')

