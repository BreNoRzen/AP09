l = 2
c = 3

matriz_usuario = []

for i in range(2):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz_usuario.append(linha)

print("\nMatriz gerada:")
for linha in matriz_usuario:
    print(linha)