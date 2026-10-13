'''playlist = ['la pele de jour', 'the inocente', 'madame satã', 'hallo', 'north start']
for indice in playlist:
    print(f'Tocando agor: {indice}')
print('Fim da playlist')
'''
carrinho = []

while True:
    produto = input('Digite o nome do produto:')
    if produto == 's':
        break
    carrinho.append(produto)
print(f'Produtos no carrinho: {carrinho}')
print(f'O ultimo produto inserio foi {carrinho[-1]}')