teatro = []

for i in range(6):
    fileiras = []
    for j in range(8):
        fileiras.append(0)
    teatro.append(fileiras)

while True:
    print("\n--- SISTEMA DE TEATRO ---")
    print("1 - Reservar assento")
    print("2 - Cancelar reserva")
    print("3 - Mostrar mapa de assentos")
    print("4 - Mostrar relatorio")
    print("5 - Mostrar fileira mais ocupada")
    print("0 - Encerrar")
    
    opcao = int(input("Escolha uma opcao: "))

    if opcao == 0:
        print("Encerrando o sistema...")
        break

    elif opcao == 1 or opcao == 2:
        f = int(input('digite a fileira ( 0 - 5):'))
        a = int(input('digite o assento (0 - 7):'))

        if f < 0 or f > 5 or a < 0 or a > 7:
            print('possicao invalida')
        
        else:
            if opcao == 1:
                if teatro[f][a] == 1:
                    print('assento ocupado')
                
                else:
                    teatro[f][a] = 1
                    print('reserva feita com sucesso')

            else:
                if teatro[f][a] == 0:
                    print('assento ja estav livre')

                else:
                    teatro[f][a] = 0
                    print('assento cancelado')

    elif opcao == 3:
        print("\nMapa de Assentos (0 = Livre, 1 = Ocupado):")
        for fileiras in teatro:
            print(fileiras)

    elif opcao == 4:
        assentos_livres = 0
        assentos_ocupados = 0
        ocupado_fileira = [0] * 6

        for i in range(6):
            for j in range(8):
                if teatro[i][j] == 0:
                    assentos_livres += 1

                else:
                    assentos_ocupados += 1
                    ocupado_fileira[i] += 1

        total_assentos = 6 * 8
        percentual = (assentos_ocupados / total_assentos) * 100

        print("\n--- RELATÓRIO DA SALA ---")
        print(f"Quantidade total de assentos livres: {assentos_livres}")
        print(f"Quantidade total de assentos ocupados: {assentos_ocupados}")
        print(f"Percentual de ocupacao da sala: {percentual:.2f}%")

        print("Assentos ocupados por fileira:")
        for i in range(6):
            print(f"  Fileira {i}: {ocupado_fileira[i]} ocupado(s)")

    elif opcao == 5:
        ocupados_por_fileira = [0] * 6
        for i in range(6):
            for j in range(8):
                if teatro[i][j] == 1:
                    ocupados_por_fileira[i] += 1
                    
        maior_valor = -1
        fileira_vencedora = 0

        for i in range(6):
            if ocupados_por_fileira[i] > maior_valor:
                maior_valor = ocupados_por_fileira[i]
                fileira_vencedora = i  # <-- INDENTAÇÃO CORRIGIDA (dentro do if)
        
        # <-- CORRIGIDO de {maior} para {maior_valor}
        print(f"\nA fileira mais ocupada e a fileira {fileira_vencedora} com {maior_valor} assento(s) ocupado(s).")
