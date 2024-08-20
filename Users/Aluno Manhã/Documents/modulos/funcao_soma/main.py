#Função lambda
somar = lambda x,y: x + y

#Programa principal
x = int(input('Informe o valor de X: '))
y = int(input('Informe o valor de Y: '))

#EXIBE O RESULTADO
print(f'A soma de {x} e {y} é {somar(x, y)}.')