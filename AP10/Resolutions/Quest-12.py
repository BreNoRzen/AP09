
matriz = []

for i in range(4):
    linha = []
    for j in range (4):
        valor = int(input('N:'))
        linha.append(valor)
    matriz.append(linha)

matriz_rotacionada = []

for i in range(4):
    linha_rot = []
    for j in range(4):
        linha_rot.append(matriz [3 - j][i])
    matriz_rotacionada.append(linha_rot)


print("Matriz original:")
for linha in matriz:
    print(linha)

print("\nMatriz rotacionada:")
for linha in matriz_rotacionada:
    print(linha)