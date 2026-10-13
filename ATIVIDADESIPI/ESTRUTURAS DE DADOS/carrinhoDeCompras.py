'''Você está desenvolvendo um e-commerce.
O usuário pode adicionar produtos ao carrinho digitando seus nomes, um
por vez.
Ao final, o sistema deve:
1. Mostrar todos os itens do carrinho
2. Dizer quantos itens foram adicionados
'''

carrinho = []

while True:
    produto = input('Nome do item para adicionar no carrinho ou s para sair:')
    if produto == 's':
            break
    carrinho.append(produto)
    print(f'Produtos no carrinho:{carrinho}')
    
print(f'Produtos adicionados no corrinho: {carrinho}')
print(f'Quantidade de produtos adiconado ao carrinho: {len(carrinho)}')