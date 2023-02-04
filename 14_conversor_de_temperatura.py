#Comverte a temperatura de °C para °F

print('\n\033[7m***CONVERSOR DE TEMPERATURAS***\n')

temp_c = float(input('Digite a temperatura: em °C: '))

temp_f = (temp_c * 9 + 160)/5

print('\nA temperatura de {}°C corresponde a {:.1f}°F\033[m\n'.format(temp_c, temp_f))

