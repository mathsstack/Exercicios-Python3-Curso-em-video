#Conversor de metros para centímetros e milímetros

print('\n\033[7;46m***CONVERSOR DE UNIDADES***\n')

c = float(input('Digite o comprimento em metros: '))

c_cm = c * 100
c_mm = c * 1000

print('\n{} metros equivale a {:.2f} centímetros e {:.2f} milímetros\033[m\n'.format(c, c_cm, c_mm))
