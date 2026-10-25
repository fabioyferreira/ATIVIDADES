precoOriginal = float(input('Digite o preçao original:'))
desconto = float(input('Digite o percetual de desconto:'))
precoFinal = precoOriginal - (precoOriginal*desconto/100)
print(f'O preco final eh: {precoFinal}')