#Calcula o preco de uma viagem de acordo com a distancia

print('\n\033[1m***HOW MUCH IS THE TRAVELLING?***\n')

d = int(input('Insira a distancia, em km: '))
preco = 0.00

if d <= 200:

	preco = d * 0.5

else:

	preco = d * 0.45

print(f'\nA sua viagem custará R${preco}\033[m\n')
