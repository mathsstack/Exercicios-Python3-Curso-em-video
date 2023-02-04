#Calculadora da média de duas notas

print('\n\033[33;45m***CALCULADORA DE MÉDIAS***\n')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2

print('\nA media das notas é {:.1f}\033[m\n'.format(media))
