'''Questão 6. Uma loja oferece descontos com base no valor da compra:
● Compras acima de R$ 500,00 → 10% de desconto
● Compras entre R$ 200,00 e R$ 500,00 (inclusive) → 5% de desconto
● Compras abaixo de R$ 200,00 → sem desconto
Escreva um programa que leia o valor da compra e exiba o valor do desconto e o valor final a ser pago.
'''

valorCompra = float(input('Digite  valor da compra: '))

if valorCompra > 500:
    desconto = valorCompra * (10/100)
elif valorCompra >=200 and valorCompra <=500:
    desconto = valorCompra * (5/100)
elif valorCompra <200:
    desconto = 0

valorFinalPago = valorCompra - desconto

print(f' O valor do desconto foi R$ {desconto:.2f} e o valor final a ser pago foi R$ {valorFinalPago:.2f}')