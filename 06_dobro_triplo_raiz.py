#Calculadora do dobro, do triplo e da raiz quadrada de um número

print('\n\033[1;35m***DOBRO, TRIPLO E RAIZ***\n')

numero = int(input('Digite um numero: '))
dobro = numero*2
triplo = numero*3
raiz = numero**(1/2)
print('\nO dobro de {} é {} \nO triplo de {} é {} \ne a raiz quadrada de {} é {:.1f}\033[m\n'.format(numero, dobro, numero, triplo, numero, raiz))
