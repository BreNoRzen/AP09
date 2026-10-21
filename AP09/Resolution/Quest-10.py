def saudacao(nome):
    print(f'Aluno(a): {nome}')

def nota_valida(nota):
    if nota >= 0 and nota <= 100:
        return True
    else:
        return False

def classificar_desempenho(nota):
    if nota >= 90 and nota <= 100:
        return 'Excelente'
    elif nota >= 70 and nota <= 89:
        return 'Bom'
    elif nota >= 60 and nota <= 69:
        return 'Regular'
    else:
        return 'Insuficiente'

def calcular_situacao(nota):
    if nota >= 70:
        return 'Aprovado'
    elif nota >= 50 and nota <= 69:
        return 'Recuperação'
    else:
        return 'Reprovado'



for i in range(1, 4):
    print(f"\n--- ALUNO {i} ---")
    nome_aluno = input('Nome do aluno: ')
    nota_aluno = float(input('Nota obtida (0 a 100): '))
    
    saudacao(nome_aluno)
    
    if nota_valida(nota_aluno):
        print('Nota válida: Sim')
        
        desempenho = classificar_desempenho(nota_aluno)
        situacao = calcular_situacao(nota_aluno)
        
        print(f'Classificação de desempenho: {desempenho}')
        print(f'Situação final: {situacao}')
    else:
        print('Nota válida: Não (Valor fora do intervalo permitido)')