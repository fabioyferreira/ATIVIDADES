'''1. Crie uma função que receba uma quantidade de horas e minutos e retorne o tempo total equivalente em segundos. '''

def convHoraSegundo(hora,minuto):
    segundoMinuto = minuto * 60
    segundoHora = hora * 3600
    return segundoMinuto + segundoHora

total = convHoraSegundo(2,30)
print (f'A quantidade de segundo eh {total}')

pr
