'''Questão 2. Escreva um programa que leia o nome de um produto, sua quantidade em estoque e seu preço
unitário. Calcule o valor total em estoque (quantidade × preço) e exiba o resultado formatado com f-string,
utilizando duas casas decimais para os valores monetários. Exemplo de saída:
Produto: Caneta
Quantidade: 150 unidades
Preço unitário: R$ 2.50
Valor total em estoque: R$ 375.00
'''

nomeProduto = str(input('Digite o nome do produto: '))
quantidadeEstoque = int(input('Digite sua quantidade: '))
precoUnitario = float(input('Digite seu preça unitário: '))

valorTotalEstoque = quantidadeEstoque * precoUnitario

print(f'Produto: {nomeProduto}\nQuantidade: {quantidadeEstoque} unidades\nPreço unitário: R$ {precoUnitario:.2f}\nValor total estoque: R$ {valorTotalEstoque:.2f}')
