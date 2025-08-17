import math
print('-' * 20)
print('CALCULADORA DE IMC')
print('-' * 20)
print('Insira seus dados abaixo!')

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
altura = float(input('Digite a sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / math.pow(altura, 2)
print(nome, 'seu IMC é de {:.2f}'.format(imc))