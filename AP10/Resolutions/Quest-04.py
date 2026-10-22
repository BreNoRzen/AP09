matriz = []

for i in range (3):
    linha = []
    for j in range(3):
        valor = int(input('digite o num: '))
        linha.append(valor)
    matriz.append(linha)

maior = matriz[0][0]

for i in range(3):
    for i in range(3):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
    print(f'o maior valor: {maior}')