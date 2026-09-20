'''Questão 5. Escreva um programa que leia o salário bruto de um funcionário e calcule o desconto do Imposto
de Renda conforme a tabela abaixo:

Faixa Salarial Alíquota
Até R$ 1.903,98 Isento
De R$ 1.903,99 a R$ 2.826,65 7,5%
De R$ 2.826,66 a R$ 3.751,05 15%
Acima de R$ 3.751,05 22,5%
Exiba o valor do desconto e o salário líquido usando f-string.
'''

salarioBruto = float(input('Digite o salario bruto: '))

if salarioBruto <= 1903.98:
    desconto = 0
    print('Isento')
elif salarioBruto > 1903.98 and salarioBruto <= 2826.65:
    desconto = salarioBruto * (7.5/100)
elif salarioBruto >= 2826.66 and  salarioBruto <=3751.05:
    desconto = salarioBruto * (15/100)
elif salarioBruto > 3751.05:
    desconto = salarioBruto * (22.5/100)

salarioLiquido = salarioBruto - desconto

print(f'O valor do desconto é R${desconto:.2f} e o salario líquido é R${salarioLiquido:.2f}')