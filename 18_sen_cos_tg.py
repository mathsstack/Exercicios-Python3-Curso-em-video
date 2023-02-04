from math import sin, cos, tan

#Calcula o seno, o cosseno e a tangente de um ângulo

print('\n\033[34m***SENO, COSSENO E TANGENTE***\n')

num = float(input('Digite um número: '))

print('''\nO seno vale {:.2f}
O cosseno vale {:.2f}
E a tangente vale {:.2f}\033[m\n'''.format(sin(num), cos(num), tan(num)))


