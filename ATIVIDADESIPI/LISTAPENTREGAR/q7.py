'''Questão 7
Faça um programa que leia 5 nomes de alunos e armazene-os em uma lista por ordem
alfabética. Ao final, exiba a lista ordenada com os nomes cadastrados.

Requisitos de Implementação

Entrada e Processamento:

Ler 5 nomes de alunos (cadeias de caracteres).

Armazenar os nomes em uma lista mantendo a ordem alfabética.

Formatação da Saída:
Exibir a lista final com os nomes ordenados alfabeticamente.
'''
nomes = []
for contador in range(5):
    nome = input('Digite um nome: ')
    nomes.append(nome)
    nomes.sort()
print(f' nomes: {nomes}')