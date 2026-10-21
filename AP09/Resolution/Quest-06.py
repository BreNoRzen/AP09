def nota_valida(nota):
    if nota >= 0 and nota <= 100:
        return True
    else:
        return False

nota = int(input('digite sua nota: '))

if nota_valida(nota):
    print('Nota válida dentro do padrão.')
else:
    print('Nota fora do padrão.')