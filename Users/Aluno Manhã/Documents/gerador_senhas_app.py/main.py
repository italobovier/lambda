import secrets

while True:
    confirma = input('Gerar Senha (s/n)?').lower()

    if confirma == 's':
        print(secrets.token_urlsafe(16))
        continue
    else:
        print('Programa encerrado!')
        break