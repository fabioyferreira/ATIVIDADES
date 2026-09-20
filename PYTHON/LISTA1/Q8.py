'''Questão 8. Escreva um programa que leia o ano de nascimento de uma pessoa e o ano atual, calcule a idade
aproximada e classifique em:
● Criança (0 a 11 anos)
● Adolescente (12 a 17 anos)
● Adulto (18 a 59 anos)
● Idoso (60 anos ou mais)
O programa deve validar se o ano de nascimento não é maior que o ano atual.
'''

anoNascimento = int(input('Digite o ano de nascimento: '))
anoAtual = int(input('Digite  ano atual:'))

if anoNascimento > anoAtual:
    print('Ano de nascimento inválido')
else:    
    idade = anoAtual - anoNascimento

    if idade >=0 and idade <=11:
        print('trata-se de uma criança (0 a 11 anos)')
    elif idade >=12 and idade <=17:
        print('Trata-se de um (a) Adolescente (12 a 17 anos)')
    elif idade >=18 and idade <60:
        print('Trata-se de Adulto (18 a 59 anos)')
    elif idade >= 60:
        print('Trata-se de um Idoso (60 anos ou mais)')
    