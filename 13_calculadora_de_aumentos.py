#Calcula o aumento do salário de um funcionário

print('\n\033[1;42m***CALCULADORA DE AUMENTOS***\n')

salario = float(input('Digite o salário do funcionário: R$ '))
tx = int(input('Digite o percentual de aumento: R$ '))

aumento = salario * ((100+tx)/100)

print('\nO novo salário será de R$ {:.2f}\033[m\n'.format(aumento))
