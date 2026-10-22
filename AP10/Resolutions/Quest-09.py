matriz_cidade = []

for i in range(4):
    cidades = []
    for j in range(7):
        temperatura =int(input('temperatura:'))
        cidades.append(temperatura)
    matriz_cidade.append(cidades)


for i in range(4):
    soma = 0
    for j in range(7):
        soma += matriz_cidade[i][j]
    media = soma / 7
    print(f"Cidade {i} - Média: {media}")


maior_geral = matriz_cidade[0][0]
cidade_maior = 0
dia_maior = 0

for i in range(4):
    for j in range(7):
        if matriz_cidade[i][j] > maior_geral:
            maior_geral = matriz_cidade[i][j]
            cidade_maior = i
            dia_maior = j

    print(f"Maior temperatura geral da semana: {maior_geral}")
    print(f"Posição: cidade {cidade_maior}, dia {dia_maior}")

for i in range(4):
    maior_cidade = matriz_cidade[i][0]
    dia_maior_cidade = 0

    for j in range(7):
        if matriz_cidade[i][j] > maior_cidade:
            maior_cidade = matriz_cidade[i][j]
            dia_maior_cidade = j

        print(f"Maior temperatura da cidade {i}: {maior_cidade} no dia {dia_maior_cidade}")


acima_30 = 0

for i in range(4):
    for j in range(7):
        if matriz_cidade[i][j] > 30:
            acima_30 += 1

print(f"Registos acima de 30 graus: {acima_30}")