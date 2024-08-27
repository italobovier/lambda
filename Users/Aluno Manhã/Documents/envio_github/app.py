import pyautogui
import time

def open_terminal():
    # Abrir o terminal usando o atalho (ajuste conforme seu sistema operacional)
    pyautogui.hotkey('ctrl', 'alt', 't')
    time.sleep(2)  # Aguarda o terminal abrir
def run_command(command):
    # Digitar o comando no terminal e pressionar Enter
    pyautogui.typewrite(command, interval=0.05)
    pyautogui.press('enter')
    time.sleep(2)  # Aguarda o comando ser executado

def navigate_and_commit():
    # Navegar até o diretório do projeto (ajuste o caminho conforme necessário)
    run_command('cd C:\\Users\\Aluno Manhã\\Documents\\crud_de_cadastro')

    # Adicionar todos os arquivos ao repositório
    run_command('git add .')

    # Fazer commit das mudanças
    run_command('git commit -m "Add source code and executable"')

    # Enviar as mudanças para o repositório remoto
    run_command('git push origin main')

def main():
    open_terminal()
    navigate_and_commit()

if __name__ == '__main__':
    main()
