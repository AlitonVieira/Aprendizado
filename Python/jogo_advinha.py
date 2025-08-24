import random
from time import sleep

print('-' * 20)
print('BEM VINDO AO JOGO...')
print('-' * 20)
print('É só você adivinhar em que número estou pensando e você ganha!')
print('x=' * 31)


print('Estou pensando em um número de 1 a 10...')
sleep(3.0)
print('=' * 30)    
N = int(input('Em que número eu pensei entre 1 e 10? '))
number_int = random.randint(1, 10)
print('O número que eu pensei foi {}!'.format(number_int))
if N == number_int:
    print('Você é mais esperto do que eu imaginava, Parabéns!')
else:
    print('HAHAHA! PERDEDOR!')

