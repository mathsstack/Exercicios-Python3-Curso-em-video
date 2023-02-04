#Exibe informações sobre uma string

print('\n\033[7;35m***TEXT ANALYZER***\n')

nome = input('Digite seu nome: ')

up = nome.upper()
low = nome.lower()

space = nome.count(' ')
leng = len(nome) - space

primeiro = nome.split()[0]

print(f'''\nO nome em maiúsculas é {up}
O nome em minúsculas é {low}
{nome} tem {leng} letras
O primeiro nome tem {len(primeiro)} letras\033[m\n''')
