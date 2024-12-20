import os
import FileJson as Json
from playwright.sync_api import sync_playwright

"""
* ENTRADA EXPRESSA

from playwright.sync_api import sync_playwright
program = sync_playwright().start()
browser = program.chromium.launch(headless=False)
page = browser.new_page()
page.goto('https://pt.khanacademy.org/')
page.locator('button#onetrust-reject-all-handler').click()
page.locator('a#login-or-signup').click()
page.locator('input[name="username"]').fill("00001100659237sp@al.educacao.sp.gov.br")
page.locator('input[name="current-password"]').fill("Bp110065#")
page.locator('button[data-testid="log-in-submit-button"]').click()

"""

class Khan_Academy():
    def __init__(self, user):
        self.page = 'https://pt.khanacademy.org/login'
        self.user = user
        self.engine(self.page, self.user)

    def engine(self, page, user):
        try:
            with sync_playwright() as program:
                browser = program.chromium.launch(headless=False, slow_mo=500)
                page = browser.new_page()
                page.goto(self.page)
                self.entrada(page,user)
                page.wait_for_timeout(5000) # TEMPO DE ESPERA.
        except Exception as e:
            print(f'ERRO NO ENGINE: {e}')

    def entrada(self, page, user):
        try:
            self.login(page, user)
            self.verificar_grupos_atividades(page)

        except Exception as e:
            print(f'ERRO NA ENTRADA: {e}')

    def login(self, page,user):
        try:
            user = dict(user)
            #* ENTRAR
            page.locator('button#onetrust-reject-all-handler').click() # REJEITAR COOKIES
            page.locator('a#login-or-signup').click() # ENTRAR/LOGAR
            
            #* LOGIN
            page.locator('input[name="username"]').fill(user['email']) # COLOCAR EMAIL
            page.locator('input[name="current-password"]').fill(user['password']) # COLOCAR SENHA
            page.locator('button[data-testid="log-in-submit-button"]').click() # ENTRAR
        except Exception as e:
            print(f'ERRO AO EFETUAR O LOGIN: {e}')

    def verificar_grupos_atividades(self, page):
        try:
            #* ATIVO
            page.wait_for_timeout(8000) # TEMPO DE ESPARA PARA CARREGAR OS ITENS
            page.locator('span#goal-filters-NO_KMAP0-label').click() # ABA ATIVO
            ativos = page.locator('div[data-testid="mastery-goal-class"]').count() # QUANTIDADE DE CARDS
            print(f'ATIVOS: {ativos}')
            
            #* ANTERIOR
            page.locator('span#goal-filters-NO_KMAP1-label').click() # ABA ANTERIOR
            page.wait_for_timeout(8000) # TEMPO DE ESPARA PARA CARREGAR OS ITENS
            anteriores = page.locator('div[data-testid="mastery-goal-class"]').count() # QUANTIDADE DE CARDS
            print(f'ANTERIORES: {anteriores}')
        except Exception as e:
            print(f'ERRO AO VERIFICAR OS GRUPOS DE ATIVIDADES: {e}')

    def verificar_atividades(self, page):
        #! TRABALHANDO NISSO...
        with sync_playwright() as program:
            browser = program.chromium.launch(headless=False, slow_mo=500)
            page = browser.new_page()
            page.goto(self.page)

            #* ATIVIDADE
            page.locator('a[data-testid="stp-cta-button"]') # BOTÃO DE COMEÇAR DE NOVO A ATIVIDADE
            page.locator('div[data-testid="lesson-card"]').count() # QUANTIDADE DE CARDS DE ATIVIDADES
            
            #* APRENDER
            page.locator('a._zl1qagl') # VIDEO (APOIO)
            page.locator('a._557wnsf') # ARQUIVO (APOIO)

            #* STARTS
            page.locator('a._1w2ulnnd') # INICIAR ATIVIDADE
            page.locator('a._1jmukqkc') # INICIAR PRATICA

            #* TESTE | QUIZ
            page.locator('div._rflrqt') # ZONA DE TESTES
            page.locator('button[data-testid="quiz-open-modal-button"]') # BOTÃO INICIAR QUIZ
            page.locator('button[data-testid="test-open-modal-button"]') # BOTÃO INICIAR TESTE

    def realizando_atividade(self, page):
        #! TRABALHANDO NISSO...
        with sync_playwright() as program:
            browser = program.chromium.launch(headless=False, slow_mo=500)
            page = browser.new_page()
            page.goto(self.page)

            #* INTRODUÇÃO
            page.locator('button._1piqtblu').click() # BOTÃO 'VAMOS LÁ'

            #* ATIVIDADE
            page.locator('div._12wan2o2') # CARD QUESTÃO

            #* ALTERNATIVA
            page.locator(':nth-match(div[style="display: flex; flex-direction: row; place-content: center; padding-top: 8px; padding-bottom: 8px; padding-left: 8px;"], 1)').text_content()

            #* BOTÃO ALTERNATIVA
            page.locator('span[data-testid="focus-ring"]') # BOTÃO

            #* BOTÃO DA PÁGINA
            page.locator('button[data-testid="exercise-check-answer"]') # BOTÃO VERIFICAR
            page.locator('button[data-testid="exercise-skip-button"]') # BOTÃO PULAR

    def acessar_cmsp(self):
        try:
            button = 'img[src="https://s3.sa-east-1.amazonaws.com/edusp-static.ip.tv/room/cards/edusp/elianemararod3272389-sp/LgpmslZ5LlI3soKX2lulNpjhYXhx7C.png"]'
            button.highlight()
            button.click()
        except Exception as e:
            print(f'ERRO AO ACESSAR O COM O CMSP: {e}')

if __name__ == '__main__':
    json = Json.FileJson()

    def program():
        try:
            path = r'S:\PYTHON\AutoAnswer\Auto D\B'
            users = json.read("users", path)
            for user in dict(users).keys():
                Khan_Academy(dict(users[user]))
        except Exception as e:
            print(f'ERRO NO PROGRAMA: {e}')

    program()
