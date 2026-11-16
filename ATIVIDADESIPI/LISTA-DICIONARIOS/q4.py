'''Questão 4. Controle de desempenho
O setor de RH de uma empresa te contratou para desenvolver um programa de
controle de desempenho dos funcionários de uma equipe.
Os 3 funcionários dessa equipe receberam, cada um, 3 notas de desempenho,
correspondentes aos últimos meses, e o programa deve armazenar tais notas em
um dicionário. 
Nesse dicionário, o valor de cada chave é uma lista que contém as
notas, conforme o exemplo abaixo:
{‘Ana’ : [10, 2, 3] , ‘Bruno’ : [1, 8 , 9], ‘Carol’ : [7, 9,
10]...}​

O programa deve:
●​ Pedir ao usuário o nome dos 3 funcionários e suas 3 notas de desempenho
(3 notas pra cada).
●​ Acessar a lista de notas de algum funcionário (escolhido pelo usuário).
●​ Calcular a média das notas de um funcionário (escolhido pelo usuário) e
exibir o resultado.
Se o usuário digitar o nome de um funcionário inválido, notifique-o e repita a
operação até que ele digite um nome válido.'''

funcionarios = {}
notas = []

for i in range(3):
    nome = input(f'Digite o nome do funcionario {i+1}:')
    for j in range(3):
        nota = float(input(f'Digite a nota {j+1}: '))
        notas.append(nota)

    funcionarios[nome] = notas
nome = input(('Digite o nome do funcionario para consultar:'))

while nome not in funcionarios:
    print('Funcionario não encontrado.')
    nome = input(('Digite o nome do funcionario para consultar:'))
print(f'Notas de {nome}: {funcionarios[nome]}')

media = sum(funcionarios[nome])/3
print(f'Media: {media}')