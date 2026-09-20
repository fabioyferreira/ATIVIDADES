'''Questão 1. Escreva um programa em Python que leia o nome, a idade e a altura (em metros) de uma
pessoa. Em seguida, exiba na tela uma mensagem formatada usando f-string com o seguinte modelo:
Olá, meu nome é João, tenho 22 anos e minha altura é 1.75m.
'''

nome = str(input('Digite um nome: '))
idade = int(input('Digite a idade: '))
altura = float(input('Digite a altura: '))

print (f'Olá, meu nome é {nome}, tenho {idade} anos e minha altura é {altura}m')