#Mostra quantos dólares é possível comprar com x reais

print('\n\033[1;32m***CONVERSOS REAL/DÓLAR***\n')

money = float(input('Quanto dinheiro você tem? '))
dolar = money/3.27

print('\nVocê pode comprar US${:.2f} dólares\033[m\n'.format(dolar))
