'''2. Crie 4 funções que recebem 2 parâmetros cada: somar, subtrair,
multiplicar e dividir. Em seguida crie uma calculadora que solicita os
valores e a operação, quando a operação for selecionada chame as
funções criadas anteriormente.
'''

def somar(p1,p2):
    return p1 + p2
def subtrair(p1,p2):
    if p1<p2:
        return print('Não ehe possivel efetuar a difeença de um numero menor po um maior')
    else:
        return p1-p2
def multiplicar(p1,p2):
    return p1*p2
def dividir(p1,p2):
    if p2 == 0:
        print('Erro divisão por 0')
    else:
        return p1/p2

print('----CALCULADORA----')
print(" + para somar")
print(" - pra subtrair")
print(" * para multiplicar")
print('/ - pra dividir')

opcao = input('Selecione uma operação:')
if opcao in ['+','-','*', '/']:
    num1 = float(input('Digite um numero:'))
    num2 = float(input('Digite o utro numero:'))

    if opcao == '+':        
        print(f'A soma eh: ',somar(num1,num2))
    elif opcao == '-':
        print(f'A difeença eh: ',subtrair(num1,num2))
    elif opcao == '*':
        print(f'A multiplicação eh: ',multiplicar(num1,num2))
    elif opcao == '/':
        print(f'A divisão eh: ',dividir(num1,num2))
else:
    print("Opção inválida")