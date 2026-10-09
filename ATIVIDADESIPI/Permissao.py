'''2. Faça um programa que verifica a permissão para a entrada de um brinquedo radical
em um parque de diversões.
Regras:
● A pessoa deve ter pelo menos 12 anos para entrar.
● Se ela tiver 12 anos ou mais, verifique sua altura:
● Se a altura for 1,40 m ou mais, ela pode entrar no brinquedo radical.
● Caso contrário, ela pode entrar apenas nas atrações infantis.
● Se tiver menos de 12 anos, não pode entrar no parque sem um responsável.
'''

idade = int(input('Digite a idade da peasoa: '))
altura = float(input('Digite a altura da pessoa: '))

if idade<12:
    print('Proibida a entrada sem um responsavel')
elif altura>=1.4:
    print('Pode entrar no brinquedo radical')
else: 
    print('Pode entrar apenas anas atações infantis')