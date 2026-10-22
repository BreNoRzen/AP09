matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input('digite o valor:'))
        linha.append(valor)
    matriz.append(linha)

pares_linhas = []
for i in range(4):
    pares = 0
    for j in range (4):
        if matriz [i][j] % 2 == 0:
            pares =+ 1
    pares_linhas.append(pares)

impares_colunas = []
for j in range(4):
    for i in range(4):
        if matriz [i][j] % 2 == 0:
            impares =+ 1
    impares_colunas.append(impares)

print(f"Pares: {pares_linhas}")
print(f"Impares: {impares_colunas}")