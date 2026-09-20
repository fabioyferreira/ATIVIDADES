'''
Crie um programa em python que simule uma rodada do jogo "Pedra, Papel e Tesoura" entre dois jogadores. O programa deve:

=> Solicitar a jogada do jogador 1 ("Pedra", "Papel" e "Tesoura").
=> Solicitar a jogada do jogador 2 ("mesmas opções).

Verificar se as duas jogadas digitadas são válidas. Se qualquer uma delas for diferente de ("Pedra", "Papel" e 
"Tesoura"), exibir "Jogada inválida!" e não declara vencedor.

Caso as duas jogadas sejam válidas, aplicar as regras do jogo:
-Pedra vence tesoura
-Tesoura vence papel
-Papel vence pedra
Jogadas iguais resultam empate
Exibir o resultado da rodada "Jogador 1 venceu, "Jogador 2 venceu" ou "Empate!"
'''
jogador1 = input('Digite a jogada para o jogador1 Pedra, Papel, Tesoura: ')
jogador2 = input('Digite a jogada para o jogador2 Pedra, Papel, Tesoura: ')


if (jogador1 =='pedra' or jogador1 =='tesoura' or jogador1 =='papel') and (jogador2 =='pedra' or jogador2 =='tesoura' or jogador2 =='papel'):
    if jogador1 =='pedra' and jogador2 =='tesoura':
        print("Jogador 1 venceu")
    elif jogador1 == "tesoura" and jogador2 == 'papel':
        print("Jogador 1 venceu")
    elif jogador1 == 'papel' and jogador2 == 'pedra':
        print("Jogador 1 venceu")
    elif jogador1  == 'pedra'and jogador2 == 'pedra':
        print('Empate')
    elif jogador1  == 'papel'and jogador2 == 'papel':
        print('Empate')
    elif jogador1  == 'tesoura'and jogador2 == 'tesoura':
        print('Empate')
    else:
        print("Jogador 2 venceu")
else:
    print ('Jogada inválida')