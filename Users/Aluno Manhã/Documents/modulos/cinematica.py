def mostrar_menu():
    print('1 - Energia potencial.')
    print('2 - Energia cinética.')
    print('3 - Sair do programa.')

def calcular_energia_potencial(massa, altura):
    g = 9.81  # aceleração devido à gravidade em m/s²
    return massa * g * altura

def calcular_energia_cinetica(massa, velocidade):
    return 0.5 * massa * (velocidade ** 2)