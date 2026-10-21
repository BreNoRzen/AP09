def converter_tempo(total_segundos):
    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos_restantes = total_segundos % 60

    return horas , minutos , segundos_restantes

tempo = int(input('digite o tempo em (Segundos):'))

horas , minutos , segundos_restantes = converter_tempo(tempo)

print("\n--- CONVERSÃO DO TEMPO DE PROVA ---")
print(f'Horas: {horas}')
print(f'Minutos: {minutos}')
print(f'Segundos restantes: {segundos_restantes}')
print("-----------------------------------")