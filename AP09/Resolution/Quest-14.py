def eh_par(numero):
    if numero % 2 == 0:
       return True
    else:
        return False

def contador_pares_faixa(inicio,fim):
    contador = 0
    for num in range(inicio, fim + 1):
        if eh_par(num):
           contador += 1 
    return contador

inicio_faixa = int(input('Digite o início da faixa: '))
fim_faixa = int(input('Digite o fim da faixa: '))

total_pares = contador_pares_faixa(inicio_faixa, fim_faixa)
print(f'A quantidade de números de peito pares é: {total_pares}')