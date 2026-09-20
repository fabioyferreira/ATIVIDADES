'''Faça um programa que simule a utilização de um elevador.
O elevador começa com 0 e vai até 10.
O usuário digita comandos: S para subir, D para descer. P para parar. 
O programa simula o movimento andar a andar e exibe o andar a cada passo 
e no final mostra quantos andares foram percorridos
'''
cont=0
andar = 0
while cont<10:
    acao = input('Digite s para subir, d para descer, p para parar')

    
    if acao=='s':
        andar= andar+1
        print('Andar atual', andar)
    elif acao == 'd':
        andar= andar-1
        print('Andar atual', andar)
    elif acao == 'p':
        break
    

    cont=cont+1

print(f'Parado. Andares percorridos: {cont}')
