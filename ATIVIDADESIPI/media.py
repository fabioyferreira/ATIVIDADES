'''
1. Faça um programa que leia 5 números inteiros e imprima sua média.
'''
i=0
soma=0
while i<5:
    numero = int(input('Digite um numero'))
    soma =  soma+numero
    i=i+1

media = soma/i
print(f'{media}')