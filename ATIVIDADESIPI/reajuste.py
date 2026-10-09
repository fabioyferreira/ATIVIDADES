'''QUESTÕES DE CONDIÇÃO
1. Faça um programa que recebe um salário de uma pessoa e calcule o reajuste
segundo a tabela:
● Salários até R$ 280,00 (incluindo) : aumento de 20%
● Salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
● Salários entre R$ 700,00 e R$ 1500,00 : aumento de 10
● Salários de R$ 1500,00 em diante : aumento de 5%
No fim, mostre:
● O salário antes do reajuste;
● O percentual de aumento aplicado;
● O valor do aumento;
● O novo salário, após o aumento.
'''
salario = float(input("Digite o salario: "))
if salario<=280:
    aumento = salario*20/100
    percentual = '20%'
elif salario>280 and salario<=700:
    aumento = salario*15/100
    percentual = '15%'
elif salario>700 and salario <=1500:
    aumento = salario *10/100
    percentual = '10%'
else:
    aumento = salario * 5/100
    percentual = '5%'
reajuste = salario + aumento

print(f'salario antes do reajuste: {salario}, o percentual: {percentual}, o valor do aumento {aumento}, novo salario {reajuste}')