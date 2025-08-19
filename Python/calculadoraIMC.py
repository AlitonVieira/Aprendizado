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

if imc < 18.5:
    print(nome, 'seu IMC é de {:.2f} e você está abaixo do peso, recomendo buscar um nutricionista.'.format(imc))
elif imc < 24.9:
    print(nome, 'seu IMC é de {:.2f} e você está com o peso normal.'.format(imc))
elif imc < 29.9:
    print(nome, 'seu IMC é de {:.2f} e você está com sobrepeso, recomendo buscar um nutricionista.'.format(imc))
elif imc < 34.9:
    print(nome, 'seu IMC é de {:.2f} e você está com obesidade grau I, recomendo buscar um nutricionista.'.format(imc))
elif imc < 39.9:
    print(nome, 'seu IMC é de {:.2f} e você está com obeseidade grau II, recomendo buscar um nutricionista.'.format(imc))
else:
    print(nome, 'seu IMC é de {:.2f} e você está com obesidade grau III(mórbida), recomendo buscar um nutricionsta.'.format(imc))
