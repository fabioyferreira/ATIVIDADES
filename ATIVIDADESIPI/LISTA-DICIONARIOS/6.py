clubes = {
    "robotica": [],
    "xadrez": [],
    "Teatro": [],
    "futebol": [],
    "musica":[]
}
print('Escolha um clube que deseja participar: ')
print('robotica')
print('xadrez')
print('Teatro')
print('futebol')
print('musica')
while True:
    aluno = input('Digite o nome do aluno:')
    if aluno == '0':
        break
    while True:
        clube = input(f'Digite o clube que o {aluno} se interessou: ')
        if clube in clubes:
            break
        else:
            print('Digite o nome de m clube existente: ')
    participantesClube = clubes[clube]
    if aluno in participantesClube:
        print('Nãoé possivel se increver mais de uma vez no clube!')
    elif len(participantesClube) >=5:
        print('Clube atingiu numero máxomo de participante: ')
    else:
        participantesClube.append(aluno)
        print('Participante incluido!')
        print(f'Lista dos participantes do clube {clube}:{participantesClube}')
print('Fim')