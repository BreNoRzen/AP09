matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        valor = int(input('n:'))
        linha.append(valor)
    matriz.append(linha)


diagonal_principal_soma = 0

for i in range(5):
    for j in range(5):
        if i == j:
            diagonal_principal_soma += matriz[i][j]

print(f"Soma da diagonal principal: {diagonal_principal_soma}")

diagonal_secundaria_soma = 0

for j in range(5):
    for i in range(5):
        if i + j == 4:
            diagonal_secundaria_soma += matriz[i][j]
print(f"Soma da diagonal secundária: {diagonal_secundaria_soma}")

soma_acima = 0

for i in range(5):
    for j in range(5):
        if j > i:
            soma_acima += matriz[i][j]

soma_abaixo = 0

for i in range(5):
    for j in range(5):
        if i > j:
            soma_abaixo += matriz[i][j]

maior_soma = 0

if soma_acima > soma_abaixo:
    maior_regiao = "acima da diagonal principal"
else:
    maior_regiao = "abaixo da diagonal principal"

print(f"Soma acima da diagonal principal: {soma_acima}")
print(f"Soma abaixo da diagonal principal: {soma_abaixo}")
print(f"Maior regiao: {maior_regiao}")
        