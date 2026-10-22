matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input('N:'))
        linha.append(valor)
    matriz.append(linha)

matriz_normalizada = []
menor_valor = [0][0]
maior_valor = [0][0]

for i in range(4):
    for j in range(4):
        if menor_valor < matriz[i][j]:
            matriz[i][j] = menor_valor
            menor_valor += matriz[i][j]            

        elif maior_valor > matriz[i][j]:
            matriz[i][j] = maior_valor 
            maior_valor += matriz

for i in range(4):
    linha_norm = []
    for j in range(4):
        if maior_valor == menor_valor:
            valor_normalizado = 0.0
    else:
        matriz_normalizada = (valor - menor_valor) / (maior_valor - menor_valor )
    linha_norm.append(valor_normalizado)
matriz_normalizada.append(linha_norm)

print("Matriz normalizada:")
for i in range(4):
    for j in range(4):
        print(f"{matriz_normalizada[i][j]:.2f}")