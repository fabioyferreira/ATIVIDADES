'''Questão 01. Alunos aprovados
Você está responsável por criar o sistema de notas dos alunos do IFPE.
O programa deve receber o nome de 10 alunos e suas respectivas notas. Esses
dados devem ser armazenados num dicionário, e, a partir dele, você deve exibir
quantos alunos e o nome dos alunos que foram aprovados na média (7,0 ou mais).'''

alunos = {}
contAprovados=0
nomeAprovados = []
for contador in range(4):
    nome = input('Digite o nome do aluno:')
    nota = float(input('Digite a nota do aluno:'))
    alunos[nome] = nota
for nome, nota in alunos.items():
    if nota >= 7:
        contAprovados = contAprovados +1
        nomeAprovados.append(nome)
print (f'Total de aprovados: {contAprovados}')
for nome in nomeAprovados:
    print(f'{nome}')
