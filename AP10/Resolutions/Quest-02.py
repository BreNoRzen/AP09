matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

for i in range(3):
    for j in range(3):
        print(f"matriz[{i}][{j}] = {matriz[i][j]}")