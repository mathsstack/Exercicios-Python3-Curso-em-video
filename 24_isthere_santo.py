#Verifica se o primeiro nome de uma cidade é 'Santo'

print('\n\033[4;44;31m***IS THERE SANTO IN NAME?***\n')

nome = input('Digite o nome da cidade: ')

chave = 'Santo'

listan = nome.split()
tem = chave in listan[0]

print(f'\n{tem}\033[m\n')
