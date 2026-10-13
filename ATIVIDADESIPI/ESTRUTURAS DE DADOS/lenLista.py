''''Crie euma lista chamada frutas que contenha 
pelo menos cinco nomes de frutas. Em seguida, use um laço
while e função len() para exibir cada fruta da lista,
uma por linha.

Fruta 1: maçã
Fruta 2: uva
Fruta 3: pera
Fruta 4: manga
'''
frutas = ['maçã', 'uva', 'pera', 'manga','morango']

contador = 0
while contador<len(frutas):
    print(f'Fruta {contador+1}: {frutas[contador]}')
    contador=contador+1
