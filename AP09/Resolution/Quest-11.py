def calcular_inscricao(valor_base, taxa=10):
    valor_total = valor_base + (valor_base * taxa / 100)
    return valor_total

valor_inicial = float(input('Digite o valor base da inscrição: '))
resultado_padrao = calcular_inscricao(valor_inicial)

resultado_personalizado = calcular_inscricao(valor_inicial, 15)

print("\n--- RESULTADOS DA INSCRIÇÃO ---")
print(f'Valor com a taxa padrão (10%): {resultado_padrao:.2f}')
print(f'Valor com a taxa personalizada (15%): {resultado_personalizado:.2f}')
print("--------------------------------")