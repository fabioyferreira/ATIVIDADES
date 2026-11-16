'''Questão 3. Controle de uma biblioteca
Você está responsável por desenvolver um sistema de controle dos livros de uma
biblioteca.
Primeiro, o programa vai registrar 5 livros na biblioteca (de sua escolha). Utilize um
dicionário para armazenar:
●​ Nome do livro;
●​ Autor do livro;
●​ Quantidade disponível na biblioteca.
As chaves do dicionário devem ser os nomes dos livros e os valores devem ser
outro dicionário, que possui as chaves “Autor” e “Quantidade” e os valores o nome
do autor e a quantidade de livros, conforme o exemplo abaixo:
{‘Dom Casmurro’ : {‘Autor’ : ‘Machado de Assis’ , ‘Quantidade’
: 10 }...}
Depois de registrar os livros, o programa começará a funcionar como uma
biblioteca. O programa deve permitir:
●​ Emprestar livros;
●​ Devolver livros;
●​ Consultar a quantidade disponível de um livro.
O programa só termina quando o usuário digitar “0”.
Ao final do programa, mostre o livro que mais foi emprestado.
'''

biblioteca = {"O Senhor dos Aneis": {"Autor": "Tolkien", "Quantidade":4},
            "Morte e Vida Severina": {"Autor": "João Cabral", "Quantidade": 2},
            "O Alienista": {"Autor": "Machado de Assis", "Quantidade":8},
            "O banquete": {"Autor": "Platão", "Quantidade":3},
            "O capital": {"Autor": "Karl marx", "Quantidade": 4}
            }
ContEmprestimo = {
    "O Senhor dos Aneis": 0,
    "Morte e Vida Severina":0,
    "O Alienista": 0,
    "O banquete": 0,
    "O capital":0
}

while True:
    print('Escolha uma opção')
    print('1 - Emprestar livros')
    print('2 - Devolver livros')
    print('3 - Consultar quaitidade disponível')
    print('0 - Sair')
    opcao = input('Escolha uma opção:')
    if opcao == '0':
        break
    elif opcao == '1':
        livro = input('Digite o nome do livro para empretimo:')
        if livro in biblioteca:
            if biblioteca[livro]["Quantidade"] > 0:
                biblioteca[livro]["Quantidade"] = biblioteca[livro]["Quantidade"] -1
                ContEmprestimo[livro] = ContEmprestimo[livro] +1
                print('emprestimo realizado')
            else: 
                print('Livro esgotado')
        else: 
            print('Livro não encontrado.')
    elif opcao =='2':
        livro = input('Digite o nome do livro para devolução:')
        if livro in biblioteca:
            biblioteca[livro]["Quantidade"] = biblioteca[livro]["Quantidade"]+1
            print('Devolucao realizada')
        else:
            print('Licro nãopertence ao catálogo.')
    elif opcao == '3':
        livro = input('Digite o nome do livro que deseja consultar:')
        if livro in biblioteca:
            quantidade = biblioteca[livro]["Quantidade"]
            print(f'O livro {livro} possui {quantidade} unidades disponiveis.')
        else:
            print('Livro não encontrado')
    else:
        print('Opcao inválida')

livroMaisEmprestado = ""
maiorQuantidade = -1

for livro, quantidade in ContEmprestimo.items():
    if quantidade > maiorQuantidade:
        maiorQuantidade = quantidade
        livroMaisEmprestado = livro
if maiorQuantidade > 0:
    print(f'O Mais emprestado foi: {livroMaisEmprestado}, com {maiorQuantidade} de emprestimo')
else:
    print('Não hove emprestimo')