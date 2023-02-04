#Calcula o preço do aluguel de um carro

print('\n\033[32;47m***QUANTO CUSTA O ALUGUEL?***\n')

km = float(input('Quantos Km rodou? '))
day = int(input('Por quantos dias? '))

preco = 0.15 * km + 60 * day

print('\nO preço a ser pago é R${:.2f}\033[m\n'.format(preco))
