'''4. Faça um programa que calcule o fatorial de um número inteiro digitado pelo usuário.
Ex.: 4! (fatorial de 4) = 4 x 3 x 2 x 1 = 24.
'''

numero = int(input('Digite um numero: '))
4
fatorial = 1
contador = 1
while contador<=numero:
    fatorial = fatorial*contador  
    contador=contador+1                 
print(f'{fatorial}')
   
    
