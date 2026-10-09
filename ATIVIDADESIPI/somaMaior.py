'''2. Faça um programa que leia N números inteiros (definido pelo usuário) e imprima se
a soma desses números é maior que o maior número digitado pelo usuário.'''

nInteiros = int(input('Digite um nmero inteiro:'))
maior = 0
contador = 0
soma = 0
while contador <nInteiros:
    nDigitado = int(input('Digite um numero'))
    soma = soma +nDigitado
    if nDigitado>maior:
        maior = nDigitado
    contador=contador+1
if soma>maior:
    print(f'Soma: {soma}')
print(f'{maior}')