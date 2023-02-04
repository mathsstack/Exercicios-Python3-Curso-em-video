#Avalia caracteristicas de 'a' dentro de uma string

print('\n\033[4;32;40m***-A- ANALIZER***\n')

frase = input('Digite uma frase: ')

veza = frase.lower().count('a')
posicaop = frase.lower().find('a')
posicaou = frase.lower().rfind('a')

print(f'\nA letra A aparece {veza} vezes')
print(f'A primeira letra A está na posicão {posicaop}')
print(f'A última letra A está na posição {posicaou}\033[m\n')
