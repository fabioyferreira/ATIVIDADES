'''Questão 10. Parque de diversões.
Um parque de diversões possui as seguintes regras para liberar o acesso a um brinquedo radical:

● A pessoa deve ter pelo menos 10 anos de idade e altura mínima de 1,40m.

Escreva um programa que leia a idade e a altura de uma pessoa e, utilizando o operador and, informe se ela
pode ou não entrar no brinquedo. Caso apenas uma das condições não seja atendida, informe qual requisito
está faltando.
'''

idade = int(input('Digite a idade da pessoa: '))
altura = float(input('Digite a altura da pessoa: '))

if idade >= 10 and altura >=1.4:
    print('Pode entrar no brinquedo')
#elif idade < 10 and altura <1.4: é uma opção, mas não é uma que a questão pede
    #print('Não pode entrar no brinquedo, tanto a altura quanto a idade são inferiores')
elif idade < 10:
    print('Não pode entrar no brinquedo, idade inferior a 10 anos.')
elif altura < 1.4:
    print('Não pode entrar no brinquedo, altura inferior a 1,4m.')
