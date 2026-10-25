'''Questão 2
Desenvolva um programa que receba uma cadeia de caracteres (string) fornecida pelo
usuário e gere uma nova string com os caracteres na ordem inversa.
'''

cadeia = input('Digite uma cadeia de caracteres: ')
ordemInversa = cadeia[::-1]
print(f'Ordem inversa de cadeia : {cadeia} => {ordemInversa}')