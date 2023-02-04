from random import randint

#A máquina chuta um número e o jogador tenta adivinhar

print('\n\033[36m***JOGO DE ADIVINHACAO***\n')

secrtnum = randint(0, 5)

chute = int(input('Qual é o seu chute? '))

if chute == secrtnum:
	print('\nPARABENS! Voce acertou! \n')
else:
	print('\nF,voce errou!\n')

print('***FIM DE JOGO***\033[m\n')
