matriz = []

for i in range(3):
    linha = []
    for j in range(4):
        valor = int(input('adinate, diga os numeros: '))
        linha.append(valor)
    matriz.append(linha)

soma = 0

for i in range(3):
    for j in range(4):
        soma += matriz[i][j]

print(f"Soma total: {soma}")