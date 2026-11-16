'''Questão 5. Caixa de supermercado
Você foi contratado para desenvolver um protótipo de sistema de caixa de
supermercado.
Inicialmente, crie um dicionário com pelo menos 5 produtos e seus respectivos
preços, conforme o exemplo abaixo:
{‘feijão’ : 6.50, ‘arroz’ : 4.80, ‘macarrão’ : 4.20 ...}
O programa deverá apresentar um menu pelo qual o cliente poderá informar o
produto que deseja comprar e a quantidade. O sistema deverá verificar se o produto
está cadastrado, calcular o valor da compra e adicionar esse valor ao total
acumulado.
O programa deverá seguir as seguintes regras:
●​ O cliente poderá comprar vários produtos, e o programa deverá continuar
funcionando até que ele escolha finalizar a compra.
●​ Caso o produto informado não exista no dicionário, o programa deverá exibir
uma mensagem de erro e permitir que o cliente escolha outro produto.
●​ Caso o cliente informe uma quantidade menor ou igual a zero, o programa
deverá informar que a quantidade é inválida.
●​ Após cada produto adicionado, o programa deverá mostrar o subtotal da
compra até aquele momento.
●​ Ao finalizar a compra, o sistema deverá informar a quantidade total de itens
comprados e o valor total da compra.
●​ Caso o valor total da compra seja superior a R$ 100,00, o cliente receberá
um desconto de 10%.
●​ Ao final, o cliente deverá informar o valor pago. O programa deverá verificar
se o dinheiro é suficiente e, caso seja, calcular o troco. Caso contrário,
deverá informar quanto ainda falta pagar.'''

produtos = {
    'feijão': 6.50,
    'arroz': 4.80,
    'macarrão': 4.20,
    'açúcar': 4.00,
    'café': 12.00
}

acumuloTotal = 0
itensTotal = 0

print("CAIXA DE SUPERMERCADO")
print("Produtos disponíveis:")

for prod, preco in produtos.items():
    print(f"- {prod}: R$ {preco}")

while True:
    
    produto = input("Digite o produto que deseja comprar (ou 'fim' para encerrar): ").lower()
    
    if produto == 'fim':
        break
        
    if produto not in produtos:
        print("Erro: Produto não cadastrado! Escolha outro produto.")
        continue
        
    quantidade = int(input("Digite a quantidade desejada: "))
    
    if quantidade <= 0:
        print("Erro: Quantidade inválida! Deve ser maior que zero.")
        continue
        
    valorUnitario = produtos[produto]
    subtotalItem = valorUnitario * quantidade
    
    acumuloTotal = acumuloTotal + subtotalItem
    itensTotal = itensTotal+ quantidade
    
    print(f"Subtotal da compra até o momento: R$ {acumuloTotal}")

print("FECHAMENTO DA COMPRA:")
print(f"Quantidade total de itens comprados: {itensTotal}")
print(f"Valor bruto da compra: R$ {acumuloTotal}")

if acumuloTotal > 100.00:
    desconto = acumuloTotal * 0.10
    acumuloTotal = acumuloTotal - desconto
    print(f"Desconto aplicado (10%): -R$ {desconto}")
    print(f"Valor com desconto: R$ {acumuloTotal}")

while True:
    valorPago = float(input("Informe o valor pago em dinheiro (R$): "))
    
    if valorPago >= acumuloTotal:
        troco = valorPago - acumuloTotal
        print(f"Pagamento aceito! Seu troco é: R$ {troco}")
        print("Obrigado pela preferência e volte sempre!")
        break
    else:
        falta = acumuloTotal - valorPago
        print(f"Dinheiro insuficiente! Ainda falta pagar: R$ {falta}")