import pyautogui
import time

# Configurações
mensagem_commit = "First commit"
github_usuario = "italobovier"  # Substitua pelo seu usuário do GitHub
github_senha = "!July1997!"  # Substitua pela sua senha do GitHub ou tokenitalobovier

link_repositorio_remoto = "https://github.com/italobovier/teste_do.git"  # Substitua pelo link do repositório remoto

# Abra o terminal
pyautogui.hotkey('win', 'r')

pyautogui.write('cmd')
pyautogui.press('enter')
time.sleep(2)

pyautogui.typewrite('cd')
print("Cole o link do diretório e pressione Enter manualmente.")
time.sleep(4)  # Dá tempo para você colar o link manualmente e pressionar Enter
pyautogui.press('enter')
time.sleep(1)



# Adicione todos os arquivos ao commit
pyautogui.typewrite('git add .')
pyautogui.press('enter')
time.sleep(1)

# Crie o commit
pyautogui.typewrite(f'git commit -m "{mensagem_commit}"')
pyautogui.press('enter')
time.sleep(2)

# Mude o nome da branch para 'main'
pyautogui.typewrite('git branch -M main')
pyautogui.press('enter')
time.sleep(1)

# Adicione o repositório remoto
pyautogui.typewrite(f'git remote add origin {link_repositorio_remoto}')
pyautogui.press('enter')
time.sleep(1)

# Empurre para o repositório remoto
pyautogui.typewrite('git push -u origin main')
pyautogui.press('enter')
time.sleep(5)

# Insira o nome de usuário do GitHub
pyautogui.typewrite(github_usuario)
pyautogui.press('enter')
time.sleep(2)

# Insira a senha do GitHub
pyautogui.typewrite(github_senha)
pyautogui.press('enter')
time.sleep(5)

# Feche o terminal
pyautogui.typewrite('exit')
pyautogui.press('enter')

print("Programa enviado para o repositório remoto com sucesso!")
