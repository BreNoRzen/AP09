matriz_alunos = []

for i in range(5):
    linhas_alunos = []
    for j in range(4):
        nota = int(input('digite sua nota:'))
        linhas_alunos.append(nota)
    matriz_alunos.append(linhas_alunos)

media_alunos = []
for i in range(5):
    for j in range(4):    
        soma =+ matriz_alunos[i][j]
        media_aluno = soma / 4
    media_alunos.append(media_alunos)

maior_med = media_alunos[0]
menor_med = media_alunos[0]

for media in media_alunos:
    if media > maior_med:
        maior_med = media
    if media < menor_med:
        menor_med = media

qtd_aprovados = 0
for i in range(5):
    media = media_alunos(i)

    if media_alunos >= 70:
        qtd_aprovados += 1
        classificacao = 'Aprovado'
    elif media_alunos >= 40 and media_alunos < 70:
        classificacao = 'Recuperado'
    else:
        classificacao = 'Reprovado'

print(f"Aluno {i} - Media: {media:.2f} - {classificacao}")

print(f"Maior media: {maior_med:.2f}")
print(f"Menor media: {menor_med:.2f}")
print(f"Quantidade de aprovados: {qtd_aprovados}")