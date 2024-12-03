"""
    STEPS
    | STEPS                                                                                        | Biblioteca              | Por que                                                                                               |
    | -------------------------------------------------------------------------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------- |
    | 1. Ver código HTML (F12)                                                                     | Selenium                | Permite inspecionar o HTML diretamente no navegador, identificando elementos e atributos específicos. |
    | 2. Identificar o que é e o que não é questão                                                 | Selenium                | Usando `find_elements`, é possível localizar elementos pelo tipo (ex.: `input`, `textarea`, etc.).    |
    | 3. Categorizar as questões (CHECKBOX, RADIOS, DRAG-DROP...)                                  | Selenium                | Identifica o tipo de elemento pelos atributos, como `type="radio"` ou `type="checkbox"`.              |
    | 4. Extrair texto                                                                             | Selenium, BeautifulSoup | Selenium captura o texto diretamente do DOM; BeautifulSoup pode ajudar em análises mais detalhadas.   |
    | 5. Procurar resposta (Chatgpt - Copiar as perguntas e passar para a Janela onde está o chat) | OpenAI API              | A API permite enviar perguntas ao modelo GPT-3.5-Turbo para obter respostas automatizadas.            |
    | 6. Responder (Simular click do mouse na alternativa)                                         | Selenium                | Simula cliques humanos nos elementos de resposta, como botões ou checkboxes.                          |
    
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
