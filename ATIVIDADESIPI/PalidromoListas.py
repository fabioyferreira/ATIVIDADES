'''Faça um programa que leia uma lista de inteiros (o
tamanho é informado pelo usuário) e verifique se ela é
um palíndromo, ou seja, se ela é igual a si mesma
quando lida de trás para frente. Exiba "É palíndromo"
ou "Não é palíndromo".
Exemplo: [1, 2, 3, 2, 1] → É palíndromo.
[1, 2, 3, 4] → Não é palíndromo.
'''

numeros = []

tamanho = int(input('Digite o tamanho da lista: '))

contador = 0
while contador < tamanho:
    numero = int(input('Digite um numero: '))
    numeros.append(numero)
    contador = contador+1
invertida = numeros[::-1]
if numeros == invertida:
    print('É palidromo')
else:
    print(f'Não é palidromo')