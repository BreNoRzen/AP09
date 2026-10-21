def saudacao(nome):
    print(f'olá carao {nome}, seja bem vindo.')


def valor_inscricao(inscricao , taxa = 10):
    print(f'o valor base da inscricao: {inscricao}.')
    valor_total = inscricao * (taxa * inscricao // 100)

    return valor_total

def tempo_segundos(tempo):
    horas = tempo // 3600
    minutos = (tempo % 3600) // 60
    tempo_segundos = tempo % 60
    
    return horas , minutos , tempo_segundos

def resumo_textual():
    horas , minutos , tempo_segundos = tempo_segundos(tempo_alunos)
    frase = f"Participante {nome_aluno}: {horas} hora(s), {minutos} minuto(s) e {tempo_alunos} segundo(s)."

def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

def faixa_numeros(inicio, fim):
    contador = 0
    for i in range(inicio, fim + 1):
        if eh_par(i):
            contador += 1
    return contador



print("--- SISTEMA DE INSCRIÇÕES DA CORRIDA ---")
n_participantes = int(input('Digite o número de participantes (N): '))

for i in range(1, n_participantes + 1):
    print(f"\n--- Dados do {i}º Participante ---")
    
    nome_aluno = input('Digite seu nome: ')
    valor_base_inscricao = float(input('Digite o valor base da inscrição: '))
    tempo_aluno = int(input('Digite o tempo da prova em segundos: '))
    inicio_faixa = int(input('Digite o início da faixa de números de peito: '))
    fim_faixa = int(input('Digite o final da faixa de números de peito: '))
    
    saudacao(nome_aluno)
    total_pagar = valor_inscricao(valor_base_inscricao)
    frase_resumo = resumo_textual(nome_aluno, tempo_aluno)
    total_pares = faixa_numeros(inicio_faixa, fim_faixa)
    
    print("\n[Resumo do Participante]")
    print(f"Nome: {nome_aluno}")
    print(f"Valor total da inscrição: R$ {total_pagar:.2f}")
    print(frase_resumo)
    print(f"Quantidade de números pares na faixa: {total_pares}")