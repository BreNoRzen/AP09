matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input('digite o valor:'))
        linha.append(valor)
    matriz.append(linha)

soma_coluna = 0

for j in range(3):
    for i in range(3):
        soma_coluna += matriz[i][j]
    print(f"Soma da coluna {j}: {soma_coluna}")