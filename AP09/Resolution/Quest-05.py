# 1. Funções reutilizadas dos exercícios anteriores
def exibir_cabecalho():
    print("====================================")
    print("           LOJA EXEMPLO             ")
    print("      Sistema de Atendimento        ")
    print("====================================")

def exibir_cliente(nome):
    print(f'Cliente: {nome}')

def calcular_valor_final(valor_produto, desconto):
    valor_do_desconto = valor_produto * (desconto / 100)
    valor_final = valor_produto - valor_do_desconto
    return valor_final

def calcular_comissao(valor_venda):
    # Calcula 5% de comissão com base no valor final da venda
    comissao_vendedor = valor_venda * 0.05
    return comissao_vendedor


exibir_cabecalho()

nome_cliente = input('Digite o nome do cliente: ')
exibir_cliente(nome_cliente)

valor_orig = float(input('Valor original do produto: R$ '))
percentual_desc = float(input('Percentual de desconto (%): '))

# Processamento utilizando as funções criadas
preco_final = calcular_valor_final(valor_orig, percentual_desc)
comissao_calculada = calcular_comissao(preco_final)

# Exibição do resumo final estruturado
print("\n--- RESUMO DO ATENDIMENTO ---")
print(f'Valor original: R$ {valor_orig:.2f}')
print(f'Desconto aplicado: {percentual_desc}%')
print(f'Valor final da compra: R$ {preco_final:.2f}')
print(f'Comissão gerada: R$ {comissao_calculada:.2f}')
print("-----------------------------")