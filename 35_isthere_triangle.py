#Verifica se é possivel construir um triangulo dado certas medidas

print('\033[4;32m\n***IS THERE THE TRIANGLE?***\n')

l1 = float(input('Digite o valor do primeiro lado: '))
l2 = float(input('Digite o valor do segundo lado: '))
l3 = float(input('Digite o valor do terceiro lado: '))

isthere = True

if l1 + l2 <= l3:
	isthere = False
else:
	if l1 + l3 <= l2:
		isthere = False
	else:
		if l2 + l3 <= l1:
			isthere = False


if  isthere == True:
	print('\nO triângulo existe\033[m\n')
else:
	print('\nEsse triângulo nao pode existir\033[m\n')
