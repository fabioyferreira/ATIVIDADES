'''Questão 3. Escreva um programa que leia a nota final de um aluno (de 0 a 10) e exiba a situação conforme
os critérios abaixo:
● Nota >= 7.0 → "Aprovado"
● Nota >= 5.0 e < 7.0 → "Recuperação"
● Nota < 5.0 → "Reprovado"
'''
notaFinal = float(input('Digite a nota final do aluno (0 a 10): '))

if notaFinal >= 7:
    print('Aprovado')
elif notaFinal >= 5 and notaFinal <7:
    print('Recuperação')
else:
    print('Reprovado')
