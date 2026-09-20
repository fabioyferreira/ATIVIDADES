'''1. Um sistema de cadastro só aceita idades entre 18 e 65 anos, 
incluindo os extremos. Escreva esse intervalo como uma expressão 
lógica que você escreveria em uma linguagem de programação,
explicando a correspondência entre o intervalo e os operadores usados.
'''

while True:

    idade = int(input('Digite um valor pra idade:'))

    if idade >=18 and idade <=65:
        print('Idade está na faixa correta')
        break
    else:
        print('Fora da faixa entre 18 e 65!')


print("Saiu do loop")



