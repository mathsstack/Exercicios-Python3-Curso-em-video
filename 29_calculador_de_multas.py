#Calcula a multa de um automóvel que ultrapassa 80km/h

print('\n\033[33m***CALCULADORA DE MULTAS***\n')

v = int(input('Insira a velocidade do veículo: '))

if v<=80:
	
	print('\nSua velocidade esta dentro do limite\n')

else:

	valor = (v - 80)* 7
	print(f'\nA multa será de R${valor}\033[m\n')
