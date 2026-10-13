#Listas (iteração)

'''Dado lista_numeros = [10, 20, 30, 40], imprima a soma de todos os
elementos da lista
'''

lista_numeros = [10,20,30,40]
soma=0
contador = 0
while contador<4:
    soma = soma + lista_numeros[contador]
    contador+=1
print(f'A a soma de todos os elementos da lista_numeros eh {soma}')
