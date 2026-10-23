matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        valor = int(input('N:'))
        linha.append(valor)
    matriz.append(linha)

quantidade_picos = 0

for i in range(5):
    for j in range(5):
        atual = matriz[i][j]

        acima = matriz[i - 1][j]
        baixo = [i+ 1][j]
        esquerda = [i][j - 1]
        direita = [i][j + 1]

if atual > acima and atual > baixo and atual > esquerda and atual > direita:
    print(f"Pico encontrado em [{i}][{j}] com valor {atual}")
    quantidade_picos += 1


print(f"Quantidade de picos: {quantidade_picos}")