#Calcula a quantidade de tinta necessária para pintar uma parede

print('\n\033[7;34m***CALCULADORA DE TINTA***\n')

comp = float(input('Digite o comprimento da parede: '))
lar = float(input('Digite a largura da parede: '))

area = comp*lar
ltinta = area/2

print('\nVocê precisa de {:.2f} litros de tinta\033[m\n'.format(ltinta))
