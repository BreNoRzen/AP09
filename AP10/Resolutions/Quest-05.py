matriz = []

for i in range(3):
    linha = []
    for j in range(4):
        value = int(input('numero:'))
        linha.append(value)
    matriz.append(linha)

soma = 0

for i in range(3):
    for j in range(4):
        soma += matriz[i][j]
    print(f"Soma da linha {i}: {soma}")
