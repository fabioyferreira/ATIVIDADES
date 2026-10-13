'''Exercício

1. Uma loja registrou as vendas (em reais) de cada dia de uma semana
em uma lista. Escreva um programa em Python que, dada a lista
abaixo, exiba:
● a quantidade de dias registrados;
● o maior valor de venda da semana;
● o menor valor de venda da semana;
● a soma total das vendas.

vendas = [120, 340, 90, 560, 230, 410, 75]
'''
vendas = [120, 340, 90, 560, 230, 410, 75]
print(f' Quantidade de dias {len(vendas)}')
print(f'Moaior valor das vendas {max(vendas)}')
print(f'O menor valor das vendas {min(vendas)}')
print(f'Soma total das vendas {sum(vendas)}')