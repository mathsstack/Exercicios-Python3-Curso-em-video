#Calcula o desconto sobre um produto

print('\n\033[4;33m***CALCULADORA DE DESCONTOS***\n')

preco = float(input('Digite o preço: '))
tx = int(input('Digite o percentual de desconto: '))

desconto = preco * ((100-tx)/100)

print('\nO preço com desconto fica R${:.2f}\033[m\n'.format(desconto))
