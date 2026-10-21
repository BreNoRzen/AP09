def caluclular_situacao(nota):
    if nota >= 70:
        classificacao = 'Aprovado'
    if nota >= 50 and nota <= 69:
        classificacao = 'Recuperação'
    else:
        classificacao = 'Reprovado'
    
    return classificacao

nota_aluno = int(input('nota:'))

resultado = caluclular_situacao(nota_aluno)
print(f'Classificação do aluno: {resultado}')