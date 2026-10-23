matriz_A = []
matriz_B = []

for i in range(2):
    linha_A = []
    for j in range(3):
        valor_A = int(input('N:'))
        linha_A.append(valor_A)
    matriz_A.append(linha_A)

for i in range(3):
    linha_B = []
    for j in range(2):
        valor_B = int(input('N:'))
        linha_B.append(linha_B)
    matriz_B.append(linha_B)

matriz_C = []

for i in range(2):
    linha_C = []
    for j in range(2):
        soma = 0
        for k in range(3):
            soma += matriz_A[i][k] * matriz_B[k][j]
        linha_C.append(soma)
    matriz_C.append(linha_C)

print("Matriz resultante:")
for linha in matriz_C:
    print(linha)