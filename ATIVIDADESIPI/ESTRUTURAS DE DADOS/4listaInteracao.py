#Listas (iteração)

'''Dado lista_numeros = [10, 20, 30, 40], ande por todos os elementos da
lista e imprima-os.
'''

lista_numeros = [10, 20, 30, 40]

contador =0
while contador<4:
    print(f' Elemento {contador} => {lista_numeros[contador]}')
    contador = contador+1

print(f'O ultimo indice da lista eh => {len(lista_numeros) -1}')
print(f'O ultimo indice da lista eh => {contador -1}')

print(f'O ultimo elementoda lista eh {lista_numeros[contador-1]}')

