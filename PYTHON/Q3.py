'''Escreva um programa que leia uma senha digitada pelo usuário 
e verifique se ela é igual a "python123". O usuário terá no máximo 
3 tentativas para acertar a senha. A cada tentativa incorreta, o programa 
deve informar quantas tentativas ainda restam. Ao final:
(i) Se o usuário acertar a senha, exibir: "Acesso liberado;
(ii) Se esgotar as tentativas. exibir: "Acesso bloqueado. 
Numero máximo de tentativas atingido." '''
tentativa = 3
while True:
    senha = input('Digite a senha: ')
    if senha == 'python123':
        print ('Acesso liberado')
        break
    else:
        tentativa = tentativa -1
        print(f'Você possui mais {tentativa} tentativas')
        if tentativa == 0:
            print('Acesso bloqueado. Numero máximo de tentativas atingido.')
            break


