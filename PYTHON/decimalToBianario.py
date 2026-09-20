'''5. Escreva, em Python, uma função que envolva algum dos conteúdos trabalhados 
(intervalos reais e sistemas de numeração), à sua escolha. Alguns exemplos possíveis 
(não é obrigatório usar exatamente estes):  
- Uma função que converte um número decimal para binário, mas só 
realiza a conversão se o número estiver dentro de um intervalo 
válido definido por você.
'''
def converterDecimalToBinario():
    while True:
        numero = int(input('Digite um numero decimal entre 0 e 255:'))

        if numero > 0 and numero<255:
            restos = []

            if numero == 0:
                resto = 0
                restos.append(str(resto))

            while numero>0:
                resto = numero % 2
                restos.append(str(resto))
                numero = numero // 2
            print(restos)
            restos.reverse()
            print(restos)
            binario = int(''.join(restos))

            print ('O numero em binario eh:',binario)
            print (type(binario))
            break
        else:
            print('Numero fora do intervalo especificado')

    print('Programa encerrado') 

converterDecimalToBinario()