'''Questão 8. Cadastro de um consultório
Uma empresa contratou você para desenvolver, em Python, um programa de
cadastro de pacientes de um consultório.
Os dados devem ser armazenados em um dicionário de cadastros, no qual cada
pessoa será identificada pelo seu primeiro nome.
O valor associado a cada primeiro nome deve ser outro dicionário, contendo:
●​ Nome completo;
●​ CPF;
●​ Telefone.
Desenvolva um programa que atenda aos requisitos abaixo:
●​ No início, solicite a quantidade de pessoas que serão cadastradas.
●​ Para cada pessoa, solicite o nome completo, o CPF e o telefone.
●​ Armazene os dados em um dicionário interno e utilize o primeiro nome da
pessoa como chave no dicionário de cadastros.
●​ Após concluir todos os cadastros, solicite o primeiro nome de uma pessoa
para consultar seus dados.
Exiba o cadastro encontrado de forma organizada, com um campo por linha,
conforme o exemplo abaixo:
Nome completo: Ana Maria Silva
CPF: 12345678900
Telefone: 81999999999
Requisitos obrigatórios:
●​ Utilize um dicionário dentro de outro dicionário.
●​ Armazene CPF e telefone como strings, preservando possíveis zeros à
esquerda.
●​ A exibição de todos os dados da pessoa consultada deve ser feita com uma
única chamada à função print(), utilizando f-string.
Para esta questão, considere que todas as pessoas possuem primeiros nomes
diferentes.
O cliente também listou requisitos desejáveis, não são obrigatórios, mas vai
melhorar o sistema.
Requisitos desejáveis:
●​ Remover espaços extras: o usuário pode digitar espaços no início ou no fim
dos dados. (DICA: Pesquise sobre o método strip() para remover os
espaços.)
●​ Consultar sem diferenciar maiúsculas de minúsculas: permita que uma
pessoa cadastrada como Ana seja encontrada ao pesquisar por ana, ANA ou
Ana. (DICA: Pesquise sobre os métodos lower() e upper().)
●​ Listar as pessoas cadastradas: ao finalizar o programa, exiba o nome
completo de todas as pessoas cadastradas, uma por linha.
●​ Tratar consultas inexistentes: caso o primeiro nome pesquisado não esteja
cadastrado, exiba uma mensagem informativa, sem encerrar o programa com
erro.
Observação: a exigência de utilizar um único print() com f-string se aplica à exibição
dos dados do paciente consultado. A listagem final pode utilizar outras
chamadas de print().
'''
cadastrosPaciente = {}

numeroPessoas = int(input("Digite a quantidade de pessoas que serão cadastradas: "))

for i in range(numeroPessoas):
    print(f"Cadastro {i+1} ")
    nomeCompleto = input("Digite o nome completo: ").strip()
    cpf = input("Digite o CPF (apenas números): ").strip()
    telefone = input("Digite o telefone: ").strip()
    
    primeiroNome = nomeCompleto.split()[0].strip().lower()
    
    dadosPaciente = {
        "Nome completo": nomeCompleto,
        "CPF": cpf,
        "Telefone": telefone
    }
    
    cadastrosPaciente[primeiroNome] = dadosPaciente


pesquisa = input("Digite o primeiro nome do paciente que deseja consultar: ").strip().lower()

if pesquisa in cadastrosPaciente:
    p = cadastrosPaciente[pesquisa]
    print(f"\nNome completo: {p['Nome completo']}\nCPF: {p['CPF']}\nTelefone: {p['Telefone']}")
else:
    print("Informação: Paciente não encontrado com esse primeiro nome.")

print("pessoas que realizaram o cadastro:")
for p in cadastrosPaciente.values():
    print(p["Nome completo"])