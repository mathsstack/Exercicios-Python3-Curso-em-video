#Calcula o aumento de um funcionário dependendo do seu salário

print('\n\033[7;31m***CALCULADORA DE AUMENTOS***\n')

sal = float(input('Digite seu salário: '))

bigsalary = sal > 1250
aumento = 0

if  bigsalary:
	aumento = sal * 1.1
else:
	aumento = sal * 1.15

print('\nO novo salário será R${:.2f}\033[m\n'.format(aumento))
