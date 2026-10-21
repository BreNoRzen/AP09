def classificar_desempenho(nota):
    if nota >= 90 and nota <= 100:
        classificacao = 'Exelente'
    elif nota >= 70 and nota <= 89:
        classificacao = 'Bom'
    elif nota >= 60 and nota <= 69:
        classificacao = 'Regular'
    else:
        classificacao = 'Insuficiente'

    return classificacao

def caluclular_situacao(nota):
    if nota >= 70:
        situacao = 'Aprovado'
    if nota >= 50 and nota <= 69:
        situacao = 'Recuperação'
    else:
        situacao = 'Reprovado'
    
    return situacao

def gerar_resumo_correcao(nota):
    desempenho = classificar_desempenho(nota)
    situacao = caluclular_situacao(nota)

    return desempenho, situacao

nota_aluno = float(input('nota:'))

classificacao_final, situacao_final = gerar_resumo_correcao(nota_aluno) 

print("\n--- RESUMO DA CORREÇÃO ---")
print(f'Classificação: {classificacao_final}')
print(f'Situação Final: {situacao_final}')
print("--------------------------")