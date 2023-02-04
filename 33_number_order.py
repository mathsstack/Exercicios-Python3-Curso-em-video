#Lê três números e diz qual o maior e o menor

print('\n\033[7;33m***MAIOR E MENOR***\n')

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais um número: '))

maior = 0
menor = 0

if n1 > n2:
	if n1 > n3:
		maior = n1
		if(n2 > n3): 
			menor = n3
		else:
			menor = n2
	else:
		maior = n3
		menor = n2

else: 
	if n2 > n3:
		maior = n2
		if n1 > n3:
			menor = n3
		else:
			menor = n1
	else: 
		maior = n3
		menor = n1

print(f'''\nO maior nùmero é o {maior}
O menor número é o {menor}\033[m\n''')
