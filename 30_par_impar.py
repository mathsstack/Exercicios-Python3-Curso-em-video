#Calcula se um número é par ou ímpar

print('\n\033[36m***PAR OU ÍMPAR?***\n')

num = int(input('Digite um número: '))

if num % 2 == 0:

	print(f'\nO número {num} é par\n')
else:
	print(f'\nO número {num} é ímpar\033[m\n')
