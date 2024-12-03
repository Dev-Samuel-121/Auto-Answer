"""
RESPONDER AUTOMATICAMENTE OS FORMULÁRIOS ONLINE

PASSOS QUE O PROGRAMA VAI FAZER:

- LER A TELA (printar)
- COPIAR TEXTO
- ENVIAR PARA O CHATGPT
- PEGAR RESPOSTA CORRETA
- SELECIONAR RESPOSTA CORRETA
- VERIFICAR SE DEU CERTO
"""

from Assets.sons import sucess, error, reset
from Assets.screenshot import screenshot
from Assets.tratador_imagem import digitalizador
import os

try:
    reset(3)
    screenshot(os.path.join(str(os.getcwd()),str("Screenshot")))
    sucess()
    digitalizador(os.path.join(str(os.getcwd()),str("Screenshot")))
except Exception as e:
    error()
    print(e)
