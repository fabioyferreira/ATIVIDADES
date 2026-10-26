'''Todo navegador possui os botões de Voltar e Avançar. Por tras deles existe 
duas listas:
uma com o histórico das páginas já visitadas e outra com as páginas para onde 
é possivel avançar. Escreva um programa que simule esse comportamento. O navegador começa
na página inicio. O usuário digita comandos:

=> N para abrir uma nova página. O programa pede o nome da página, que passa a ser a página atual.
Ao abrir uma nova página, não é possivel avançar(a lista de avanço deve ser esvaziada).

=> V para voltar à página anterior. A página atual sai do histórico e vai para a lista de avanço.
Se não houver página anterior, exibir "Não é possivel voltar".

=> A para avançar. A ultima página que foi deixada ao voltar retorna ao histórico
e passa a ser a apágina atual. Se não houver pra onde avançar, exibir "Não é possivel
avançar".

=> S pra sair
Após cada comando, o programa deve exibir a apágina atual. Ao sair, deve exibir quantas páginas
novas foram abertas durante a navegação. Dica: a página atual é sempre o ultimo
elemento da lista de histórico. Use o método pop() para retirar o ultim elemento de
uma lista.
'''
hitorico =[]
avancar = []
contarPaginaAberta = 0

while True:
    comando = input('Entre N, A ou S pra sair: ')
    if comando == 's':
        break
    elif comando == 'N':
        site = input('Entre com endereço: ')
        hitorico.append(site)
        avancar = []
        contarPaginaAberta += 1
        print(f' A página atual eh {hitorico[-1]}')
    elif comando == 'V':
        if len(hitorico)==0:
            print('Não eh possivel voltar')
            print(f' A página atual eh {hitorico[-1]}')

        else:
            avancar = hitorico.pop(-1)
            #print(f' Avançar: {avancar}')
            print(f' A página atual eh {hitorico[-1]}')

    elif comando == 'A':
        if len(avancar)==0:
            print('Não é possivel avançar.')
            print(f' A página atual eh {hitorico[-1]}')

        else:
            hitorico.append(avancar)
            print(f' A página atual eh {hitorico[-1]}')

print(f'Numero de páginginas abertas:')
print(f'A quantidade de paginas abertas foram: {contarPaginaAberta}')
