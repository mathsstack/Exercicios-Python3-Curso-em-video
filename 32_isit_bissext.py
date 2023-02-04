#Calcula de determinado ano é bissexto

print('\n\033[4;35m***O ANO É BISSEXTO?***\n')

year = int(input('Digite o ano: '))

isbissext = (year - 2000) % 4 == 0

if isbissext:

	print(f'\nO ano {year} é bissexto\n')
else:
	print(f'\nO ano {year} não é bissexto\033[m\n')
