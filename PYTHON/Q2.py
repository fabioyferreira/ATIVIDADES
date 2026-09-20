'''Dado um numero inteiro positivo, exiba todos os divisores em ordem
 crescente e, ao final, quantos divisores ele possui.
 Exemplo: n = 12 saída = 1 2 3 4 6 12. Total = 16'''

inteiroPositivo = int(input('Digite um inteiro positivo: '))

total = 0
divisor = 1
while divisor<=inteiroPositivo:
    if inteiroPositivo % divisor == 0:
        resultado = divisor
        print(f'Divisor: {divisor}')
        total = total +1
    divisor=divisor+1
print (f'total {total}')
