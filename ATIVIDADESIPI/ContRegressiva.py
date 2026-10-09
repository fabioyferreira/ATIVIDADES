'''3. Faça um programa que peça um número inteiro ao usuário, e imprima uma
contagem regressiva desse número até 0, escrevendo “Fim!” ao acabar a contagem.
Ao final, exiba a soma dos números que apareceram na contagem.
'''
soma=0
numeroInteiro = int(input('Digite um numero: '))
while numeroInteiro >=0:
    
    soma = soma+numeroInteiro
    print(f'{numeroInteiro}')
    numeroInteiro = numeroInteiro-1

print('Fim!')
print(f'{soma}')