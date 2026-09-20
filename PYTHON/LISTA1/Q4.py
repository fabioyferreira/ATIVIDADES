'''Questão 4. Escreva um programa que leia três números inteiros e exiba o maior deles. O programa deve
funcionar corretamente mesmo que dois ou mais números sejam iguais.
'''

num1 = int(input('Digite primeiro numero: '))
num2 = int(input('Digite segundo numero: '))
num3 = int(input('Digite terceiro numero: '))

caixa = num1

if num2 > caixa:
    caixa = num2
if num3 > caixa:
    caixa = num3

print(f'O maior numero é o {caixa}')

maior = caixa

print (f'O maior numero é o {maior}')







