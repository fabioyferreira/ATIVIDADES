'''Questão 02. Agenda telefônica
Crie um programa que simula uma agenda telefônica.
O usuário poderá inserir até 10 contatos, informando nome e telefone (apenas
números). Caso o usuário queira encerrar o programa (e registrar menos que 10
contatos), ele deve digitar “0” para encerrar o cadastro de contatos.
Esses contatos devem ser armazenados em um dicionário, e, após encerrar o
cadastro, o sistema deve iniciar o processo de busca de contatos.
O programa deve buscar o número de um contato pelo nome. O usuário escreverá o
nome de um contato para que o programa devolva com o seu número. Caso o
contato não exista, exiba “Contato não encontrado.” O sistema só encerrará a busca
de contatos caso o usuário digite “0”.'''

agenda = {}

for i in range(10):
    nome = input(f'Digite o nome do contato (0 pra sair)')
    if nome == '0':
        break
    telefone = input('Digite o telefone de {nome}')
    agenda[nome] = telefone

while True:
    buscar =input('Digite o nome do contto para pesquisar:')
    if buscar == '0':
      print('Agenda encerrada...')
      break
    elif buscar in agenda:
        print(f'O telefone de {buscar}: {agenda[buscar]}')
    else:
            print('Contato não encontrado.')