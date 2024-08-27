import pyautogui
import time

# Configurações
mensagem_commit = "First commit"

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

# Feche o terminal
pyautogui.typewrite('exit')
pyautogui.press('enter')

print("Programa enviado para o repositório remoto com sucesso!")
