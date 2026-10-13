'''range()

Função que serve para gerar objetos que representam listas rapidamente
'''
#range(inicio,fim)
#range(inicio, fim, passo)

range(0,10)

print(f'{range(0,5)}')

intervalo = range(0,10)

print(f'{intervalo}')

for contador in range(4,10):
    print(f'{contador}')

for contador in range(10,0,-1):
    print(f'{contador}')