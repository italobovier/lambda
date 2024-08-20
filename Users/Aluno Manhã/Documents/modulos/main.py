import cinematica as cn


while True:
    # Mostrar menu na tela
    cn.mostrar_menu()

    opcao = input('Opção do usuário: ')

    match opcao:
        case '1':
            massa = float(input('Digite a massa (kg): ').replace(',', '.'))
            altura = float(input('Digite a altura (m): ').replace(',', '.'))
            print(f'A energia potencial é: {cn.calcular_energia_potencial:,.2f} Joules.')
            continue
        case '2':
            massa = float(input('Digite a massa (kg): ').replace(',', '.'))
            velocidade = float(input('Digite a velocidade (m/s): ').replace(',', '.'))
            print(f'A energia cinética é: {cn.calcular_energia_cinetica:,.2f} Joules.')
        case '0':
            print('Saindo do programa.')
            break
        case _:
            print('Opção inválida, por favor tente novamente.')
            continue