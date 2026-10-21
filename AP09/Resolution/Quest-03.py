def calcular_comissao(valor_venda):
    comissao = valor_venda * 0.05
    return comissao

venda = int(input('venda: '))
resultado = calcular_comissao(venda)

print(f"O valor guardado é: {resultado}")