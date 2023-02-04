import math

#Decompõe um número através de bibliotecas matemáticas

print('\n\033[37m***NUMBER TRUNCER***\n')

num = int(input('Digite um número entre 0 e 9999: '))

m = math.trunc(num/1000)
mil = m * 1000

c = math.trunc((num - mil)/100)
cem = c * 100

d = math.trunc((num - mil - cem)/10)
dez = d * 10

u = num - mil - cem - dez

print(f'''\nUnidade: {u}
Dezena: {d}
Centena: {c}
Unidade de milhar: {m}\033[m\n''')
