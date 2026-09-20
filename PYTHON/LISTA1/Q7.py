'''Questão 7. Escreva um programa que funcione como uma calculadora simples. O programa deve ler dois
números e um operador (+, -, *, /). Em seguida, deve exibir o resultado da operação. Caso o operador seja / e
o segundo número seja zero, o programa deve exibir a mensagem: "Erro: divisão por zero não é permitida."
Se o operador for inválido, exiba: "Operador inválido."
'''
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
operador = input('Digite um operador (+, -, *, /): ')

if operador == '+':
    resultado = num1+num2
    print(f'Resultado da soma de {num1} + {num2} eh {resultado}')
elif operador == '-':
    resultado = num1 - num2
    print(f'Resultado da diferença de {num1} - {num2} eh {resultado}')
elif operador == '*':
    resultado = num1 * num2
    print(f'Reusltado do produto de {num1} * {num2} eh {resultado}')
elif operador == '/':
    if num2 == 0:
        print('Erro: divisão por zero não é permitida.')
    else:
        resultado = num1 / num2
        print(f'Resultado da divivisão de {num1} / {num2} eh {resultado}')
else:
    print('Operador inválido.')