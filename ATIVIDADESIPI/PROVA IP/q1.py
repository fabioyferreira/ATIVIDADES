'''Um album possui figurinhas numeradas de 1 a 10. Leia os numeros das figurinhas que uma pessoa tirou,
até que seja digitado zero(numeros fora de 1 a 10 devem ser ignorados). Ao final, exiba as figurinhas coladas no
album, as repetidas(para a troca) e as que faltam.'''

album = []
repetidas = []
coladas = []
faltam = []

while True:
    numero = int(input('Digite um numero da figurinha:'))
    if numero == 0:
            break
    
    elif numero < 1 or numero >10:
        numero = int(input('Digite um numero da figurinha:'))    
    
    else:        
        if numero not in album:
            album.append(numero)
            coladas.append(numero)

        else:
            repetidas.append(numero)

for i in range(1,10):
     if i not in album:
          faltam.append(i)

print(f'album: {album}')
print(f'coladas: {coladas}')
print(f'repetidas: {repetidas}')
print(f'faltam: {faltam}')
