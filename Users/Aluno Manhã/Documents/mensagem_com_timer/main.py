#importando biblioca
import time

msgs = ("Abrindo programa...", 'Executando programa...', 'Ainda executndo o programa...', 'Programa demorando mais que os esperado', 'Finalizando, aguarde...')

for msg in msgs:
    print(msg)
    time.sleep(3)