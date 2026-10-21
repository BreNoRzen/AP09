def converter_tempo(total_segundos):
    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos_restantes = total_segundos % 60

    return horas, minutos, segundos_restantes

def gerar_resumo_tempo(nome, total_segundos):
    horas, minutos, segundos = converter_tempo(total_segundos)
    frase = f"Participante {nome}: {horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)."
    
    return frase

nome_participante = input('Digite o nome do participante: ')
tempo_segundos = int(input('Digite o tempo total em segundos: '))

resumo = gerar_resumo_tempo(nome_participante, tempo_segundos)

print(resumo)