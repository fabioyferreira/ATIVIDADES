'''Listas (remoção) - Exercício

Uma loja de informática mantém a seguinte lista de produtos em estoque:
estoque = ["Mouse", "Teclado", "Monitor", "Headset", "Webcam"]
Tarefa:
1. Mostre a lista de produtos numerada (índice + produto).
2. Peça ao usuário que digite o número (índice) do produto que deseja
remover.
3. Use pop() para remover o produto da lista.
4. Mostre a lista atualizada.
'''
estoque = ["Mouse", "Teclado", "Monitor", "Headset", "Webcam"]

contador = 0
while contador<len(estoque):
    print(f'{contador} - {estoque[contador]}')
    contador=contador+1
numeroIndice = int(input('Digite um numero/indice para remover:'))
estoque.pop(numeroIndice)
print(f'{estoque}')