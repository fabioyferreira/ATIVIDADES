'''Questão 9. Entrada na Festa
Uma festa de formatura possui as seguintes regras para permitir a entrada:
● O convidado deve ter pelo menos 15 anos de idade.
● O convidado deve apresentar um convite (representado por 1 para sim e 0 para não).
Escreva um programa que leia a idade e se o convidado possui convite e, utilizando o operador and, informe
se ele pode ou não entrar na festa. Caso apenas uma das condições não seja atendida, informe qual requisito
está faltando.
'''
idade = int(input('Digite a idade do convidado: '))
convite = str(input('Apresente seu convite (1 - sim, 0 - para não): '))

if idade >= 15 and convite =='1':
    print('Pode entrar')
elif idade <15:
    print('Idade não atendida, não pode entrar na festa')
elif convite == '0':
    print('Não possui convite, não pode entrar na festa')