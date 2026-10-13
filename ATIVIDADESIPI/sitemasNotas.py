'''Listas (adição) - Exercício

Você foi contratado para desenvolver um sistema simples de controle de
notas de uma turma. Crie um programa em Python que:
1. Peça ao usuário para digitar o nome de um aluno (ou "fim" para
encerrar).
2. Para cada aluno digitado, solicite também sua nota.
3. Armazene os nomes em uma lista chamada alunos e as notas em
uma lista chamada notas.
4. Ao final, exiba:
○ A lista completa de alunos e notas.
○ A média da turma.
'''

alunos = []
notas = []
mediaTurma = 0
while True:
    nome = input('Digite o nome do aluno | digite fim pra sair: ')
    if nome == 'fim':
        break
    alunos.append(nome)
    nota = float(input('Digite a nota do aluno: '))
    notas.append(nota)
if len(notas)>0:
    mediaTurma = sum(notas)/len(notas)


print(f'Alunos {alunos}')
print(f'Notas: {notas}')
print(f'Media da turma {mediaTurma}')
