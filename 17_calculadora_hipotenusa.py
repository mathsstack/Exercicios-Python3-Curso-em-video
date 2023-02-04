from math import pow, sqrt

#Lê os doia catetos de um triângulo e calcula a hipotenusa

print('\n\033[4;36m***CALCULADORA DE HIPOTENUSA***\n')

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

hip = sqrt(pow(co, 2) + pow(ca, 2))

print('\nA hipotenusa vale {:.2f}\033[m\n'.format(hip))
