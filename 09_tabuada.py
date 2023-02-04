#Mostra a tabuada de um número inteiri

print('\n\033[45m***TABUADA***\n')

x = int(input('Digite um número: '))

print(f'\nA tabuada do {x} é: \n')
print('{} x 1 = {:<8} {} x 2 = {}'.format(x, x, x, x*2))
print('{} x 3 = {:<8} {} x 4 = {}'.format(x, x*3, x, x*4))
print('{} x 5 = {:<8} {} x 6 = {}'.format(x, x*5, x, x*6))
print('{} x 7 = {:<8} {} x 8 = {}'.format(x, x*7, x, x*8))
print('{} x 9 = {:<8} {} x 10 = {} \033[m\n'.format(x, x*9, x, x*10))
