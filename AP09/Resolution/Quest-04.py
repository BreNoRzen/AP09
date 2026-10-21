def calcular_valor_final(valor_produto, desconto):
    valor_do_desconto = valor_orig * ( valor_desconto / 100 )
    valor_final = valor_orig - valor_desconto
    return valor_final

valor_orig = int(input('valor original:'))
valor_desconto = int(input('valor desconto: '))

resultado = calcular_valor_final(valor_orig, valor_desconto)
print(f'Valor final com desconto: R$ {resultado}')