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

nota_aluno = float(input('not:'))

resultado = classificar_desempenho(nota_aluno)

print(f'Classificação do aluno: {resultado}')