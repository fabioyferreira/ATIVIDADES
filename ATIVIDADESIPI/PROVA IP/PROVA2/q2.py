quantidadePassaGeiro = []
n = int(input('Quantas paradas vai passar:'))
for i in range(1,n):
    
    descer = int(input('Digite o numero dos que vão descer: '))
    subir = int(input('Digite a quantidade dos que vão subir: '))
    if descer < 0 or descer > len(quantidadePassaGeiro):
        print('Não pode Subir mais do que os que estão dentro do bus.')
        continue
    elif subir > (40 - len(quantidadePassaGeiro)):
        quantidadePassaGeiro.append(subir)
