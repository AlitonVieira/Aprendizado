import random

print('-' * 20)
print('BEM VINDO AO JOGO...')
print('-' * 20)
print('É só você adivinhar em que número estou pensando e você ganha!')
print('x=' * 31)


    
N = int(input('Em que número estou pensando de 1 a 10? '))
number_int = random.randint(1, 10)
print('O número que eu pensei foi {}!'.format(number_int))
if N == number_int:
    print('Você é mais esperto do que eu imaginava, Parabéns!')
else:
    print('HAHAHA! PERDEDOR!')

