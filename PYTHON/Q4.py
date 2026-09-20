'''Um matemático curioso deseja estudar a famosa Conjectura de 
Collatz (também conhecida como "problema 3n+1"). A regra é simples: dado 
um numero inteiro positivo n, aplique repetidamente as seguintes operações:
=> Se n for par, divida por 2.
=> Se n for ímpar, multiplique por 3 e some 1.

A conjectura afirma que, independente do numero inicial, a sequencia sempre 
chegará ao valor 1.
Escreva um programa em python que:
1. Solicite ao usuário um numero inteiro positivo n(maior que 1). 
Caso seja inválido o programa deve pedir novamente até receber um valor 
válido.
2. Exiba toda a sequencia gerada. desde n até chegar em 1.
Exemplo para n = 6: 6,3,10,5,16,8,4,2,1'''
numPositivo = int(input('Digite um numero inteiro positivo mior que 1: '))
i=0
while numPositivo>1:

    if numPositivo>1:
        sequencia = []
        while numPositivo >=1:
            if numPositivo %2 ==0:
                numPositivo = numPositivo/2
                sequencia.append(numPositivo) 
                print(numPositivo)          

            else:
                numPositivo = (numPositivo*3)+1
                sequencia.append(numPositivo)
                print(numPositivo)
            numPositivo = numPositivo-1

        print(sequencia)   
        
       
    else:
        numPositivo = int(input('Digite um numero inteiro positivo maor que 1'))
i=i+1
