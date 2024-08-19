# #Função de boas-vindas
# def saudar(nome, idade):
#     if idade >= 18:
#         print(f'{nome}, Seja bem-vindo ao curso de Python!')
#     else:
#         print(f'{nome} teve a inscrição bloqueada.')
# #Programa principal
# nome = input('Informe seu nome: ')
# idade = int(input('Informe sua idade: '))

# #Executando a função
# saudar(nome, idade)

# Função de boas-vindas com ternário
def saudar(nome, idade):
    # Usando f-string com ternário
    print(f'{nome}, bem-vindo.' if idade >= 18 else f'{nome} foi bloqueado')

# Programa principal
nome = input('Informe seu nome: ')
idade = int(input('Informe sua idade: '))

# Executando a função
saudar(nome, idade)
