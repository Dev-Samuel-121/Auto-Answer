"""
# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait
def waitID(id, time=30):
    variavel = WebDriverWait(driver, time).until(EC.visibility_of_element_located((By.ID, str(id))))
    return variavel

def waitCLASS(id, time=30):
    variavel = WebDriverWait(driver, time).until(EC.visibility_of_element_located((By.CLASS_NAME, str(id))))
    return variavel

def waitXPATH(id, time=30):
    variavel = WebDriverWait(driver, time).until(EC.visibility_of_element_located((By.XPATH, str(id))))
    return variavel

# Users
def user():
    # Definindo os dados dos usuários de forma mais estruturada
    usuarios = {
        '1': {
            'ra': 110065918,
            'dg': 3,
            'uf': 'sp',
            'pass': 'Bp110065#'
        },
        '2': {
            'ra': 110065923,
            'dg': 9,
            'uf': 'sp',
            'pass': 'Bp110065#'
        }
    }

    try:
        # Exibe as opções de usuários disponíveis
        print("Usuários disponíveis:")
        for chave, valor in usuarios.items():
            print(f"Usuário {chave}: {valor['uf'].upper()}")

        # Solicita o número do usuário
        n = input('Digite o número do usuário (1 ou 2): \n')

        # Verifica se a escolha é válida e retorna os dados do usuário
        if n in usuarios:
            usu = usuarios[n]
            return [usu['ra'], usu['dg'], usu['uf'], usu['pass']]
        else:
            print('Opção inválida. Digite 1 ou 2.')
            return None

    except Exception as e:
        print(f"Erro ao processar os dados: {e}")
        return None
# Drivers
driver = webdriver.Chrome()

accessStudent = waitID('access-student')
accessStudent.click()
"""