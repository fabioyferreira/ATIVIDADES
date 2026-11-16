'''Questão 7. Queima de estoque
Você foi contratado para fazer um sistema de uma loja que está fazendo uma
queima de estoque e quer vender todos os seus produtos disponíveis.
Os produtos devem ser armazenados em um dicionário que tem como chave o
produto, e o valor outro dicionário que contém quantidade no estoque e preço. O
programa deve atender um número indeterminado de clientes, até que todo o
estoque de todos os produtos seja vendido, isso significa que, após um cliente
finalizar a compra, outro entrará, até que todos os produtos da loja se esgotem.
Para cada cliente, o programa deve:
●​ Exibir os produtos que ainda tem na loja.
●​ Solicitar o nome do produto que o cliente quer comprar.
●​ Solicitar a quantidade do produto que o cliente quer comprar.
●​ Calcular o valor total da compra.
Caso o cliente escreva um produto inválido (que não existe ou que tenha o estoque
igual à zero), exiba uma mensagem de erro e peça novamente. Caso o cliente digite
uma quantidade inválida (quantidade > estoque), faça a mesma coisa.
O programa deve solicitar o nome de um produto até que o cliente digite “0”. Ao
digitar “0”, o atendimento à esse cliente encerra e o programa exibe o valor total da
compra.​
Quando todos os produtos se esgotarem, exiba “Estoque total esgotado!”, e encerre
os atendimentos. Ao encerrar, exiba a quantidade de clientes que fizeram compras
na loja.'''

estoqueLoja = {
    'camisa': {'quantidade': 3, 'preco': 30},
    'bermuda': {'quantidade': 2, 'preco': 50},
    'tenis': {'quantidade': 1, 'preco': 120}
}

quantidadeClientes = 0
while True:
   
    totalEstoque = 0
    for i in estoqueLoja.values():
        totalEstoque = totalEstoque + i["quantidade"]
        
    if totalEstoque == 0:
        print("Estoque total esgotado!")
        break
        
    
    totalCompra = 0
    
    while True:
        print("Produtos disponíveis na loja:")
        for produto, i in estoqueLoja.items():
            if i['quantidade'] > 0:
                print(f"- {produto}: {i['quantidade']} un. | R$ {i['preco']}")
                
        produtoComprado = input("Digite o nome do produto que deseja comprar (ou '0' para encerrar a compra): ")
        
        if produtoComprado == '0':
            break
            
        if produtoComprado not in estoqueLoja or estoqueLoja[produtoComprado]['quantidade'] == 0:
            print("Erro: Produto inválido ou esgotado! Escolha outro.")
            continue
            
        quantosComprou = int(input("Digite a quantidade que deseja comprar: "))
        
        temEstoque = estoqueLoja[produtoComprado]['quantidade']
        
        if quantosComprou <= 0 or quantosComprou > temEstoque:
            print(f"Erro: Quantidade inválida! Disponível em estoque: {temEstoque}.")
            continue
            
        preco_produto = estoqueLoja[produtoComprado]['preco']
        valor = quantosComprou * preco_produto
        
        estoqueLoja[produtoComprado]['quantidade'] =  estoqueLoja[produtoComprado]['quantidade'] - quantosComprou
        totalCompra = totalCompra + valor
        
        print(f"Item adicionado! Subtotal da compra: R$ {totalCompra:.2f}")
        
    if totalCompra > 0:
        quantidadeClientes = quantidadeClientes + 1
        print(f"Atendimento encerrado para este cliente.")
        print(f"Valor total da compra: R$ {totalCompra}")

print(f"\nTotal de clientes que fizeram compras na loja: {quantidadeClientes}")