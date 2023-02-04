#Analisador de textos

print('\n\033[31m***ANALISADOR DE STRINGS***\n')

algo = input('Digite algo: ')

print(f'\n{algo} é um/uma {type(algo)}')
print('É um número?', algo.isnumeric())
print('É uma letra?', algo.isalpha())
print('É alfanumérico?', algo.isalnum(),'\033[m\n')
