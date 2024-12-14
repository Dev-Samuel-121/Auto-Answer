import FileJson as Json
from playwright.sync_api import sync_playwright
"""
from playwright.sync_api import sync_playwright
program = sync_playwright().start()
browser = program.chromium.launch(headless=False, slow_mo=1000)
page = browser.new_page()
page.goto('https://saladofuturo.educacao.sp.gov.br/')
page.locator('button[data-testid="botao-login-sed"]').click()
page.locator(':nth-match(.css-1frrzr1, 1)').fill("110065923")
page.locator(':nth-match(.css-1frrzr1, 2)').fill("7")
page.locator('.css-r1nef8').click()
page.locator(f'li.css-1ep6xdl[data-value="SP"]').click()
page.locator('.css-scvshb').fill("Bp110065#")
page.locator('.css-56yhrg').click()

"""

class Sala_Futuro():
    def __init__(self, user):
        self.page = 'https://saladofuturo.educacao.sp.gov.br/'
        self.user = dict(user)
        self.engine(self.user, self.page)

    def engine(self, user, page):
        try:
            with sync_playwright() as program:
                browser = program.chromium.launch(headless=False)
                page = browser.new_page()
                page.goto(self.page)
                self.entrada(user, page)
                page.locator("fsdaf").count()
                page.wait_for_timeout(5000)
                # page.locator(":nth-match(.css-15j76c0, 1)").text_content()
                # page.locator(".css-5vgve0")
        except Exception as e:
            print(f'ERRO NO ENGINE: {e}')
    
    def entrada(self, user, page):
        try:
            self.login(user, page)
            # self.acessar_sala(page)
            # self.acessar_atividades(page)
        except Exception as e:
            print(f'ERRO NA ENTRADA: {e}')

    def login(self, user, page):
        page.locator('button[data-testid="botao-login-sed"]').click()
        page.locator(':nth-match(.css-1frrzr1, 1)').fill(user['ra'])
        page.locator(':nth-match(.css-1frrzr1, 2)').fill(user['dg'])
        page.locator('.css-r1nef8').click()
        page.locator(f'li.css-1ep6xdl[data-value="{str(user['uf']).upper()}"]').click()
        page.locator('.css-scvshb').fill(user['password'])
        page.locator('.css-56yhrg').click()

    def verificacao_inicial(self, page):
        self.atividades_pendentes(page)
        # VERIFICAR O NÚMERO DE FALTAS;
        pass
    
    def atividades_pendentes(self, page):
        try:
            geral = page.text_content(":nth-match(.css-15j76c0, 1)")
            tarefas = page.text_content(":nth-match(.css-1qedkgf, 1)")
            redacao = page.text_content(":nth-match(.css-1qedkgf, 2)")
            prova = page.text_content(":nth-match(.css-1qedkgf, 3)")
            resultado = {
                "tarefas":str(tarefas),
                "redacao":str(redacao),
                "prova":str(prova),
                "geral":str(geral)
            }
            page.locator(".css-jzfio7").highlight()
            return resultado
        except Exception as e:
            print(f'ERRO AO PEGAR O NÚMERO DE ATIVIDADES PENDENTES: {e}')

    def tarefa_sp(self, page):
        """
        !!! VOLTAR AQUI !!!
        """
        page.locator(":nth-match(.css-w2vw1p, 3)").click()
        page.locator(".css-5vgve0").highlight() # SE EXISTIR ISSO, NÃO TEM ATIVIDADES PARA FAZER.
        page.locator(":nth-match(.css-39ukww, 1)").highlight() # DRAGDOW DE TURMAS.
        page.locator(":nth-match(.css-39ukww, 2)").highlight() # DRAGDOW DE ATIVIDADES.
        # page.locator(":nth-match(.css-1ep6xdl, 1)").highlight() # TODAS AS ATIVIDADES.
        # page.locator(":nth-match(.css-1ep6xdl, 2)").highlight() # AFAZER.
        # page.locator(":nth-match(.css-1ep6xdl, 3)").highlight() # RASCUNHOS.
        # page.locator(":nth-match(.css-1ep6xdl, 4)").highlight() # EM CORREÇÃO.
        # page.locator(":nth-match(.css-1ep6xdl, 5)").highlight() # REVISAR.
        # page.locator(":nth-match(.css-1ep6xdl, 6)").highlight() # CONCLUIDAS.
        page.locator(":nth-match(.css-1ep6xdl, 7)").highlight() # EXPIRADAS.
        page.locator(".css-wiwm8n") # CARD DAS ATIVIDADES.
        page.locator(".css-15734jk") # MATERIA DA ATIVIDADE.
        page.locator('p[data-testid="status-cartao-tarefa"]') # STATUS DA ATIVIDADE.
        page.locator('p[data-testid="cartao-tarefa-titulo"]') # TITULO DA ATIVIDADE.
        #* CONTINUAR A PROSEGUIR NO CÓDIGO, PEGAR CADA ATIVIDADE E VERIFICAR SE PODE FAZER OU NÃO.
        # page.locator(":nth-match(.css-1ep6xdl, 8)").highlight() # PENDENTES.
    
    def speak(self, page):
        page.locator(":nth-match(.css-w2vw1p, 5)").highlight()

    def leia_sp(self, page):
        page.locator(":nth-match(.css-w2vw1p, 8)").highlight() # ACESSAR O LEIA SP.
        page.locator(":nth-match(.css-w2vw1p, 8)").highlight() # ACESSAR O LEIA SP.

    def khan_academy(self, page):
        page.locator(":nth-match(.css-w2vw1p, 9)").highlight()

    def me_salva(self, page):
        page.locator(":nth-match(.css-w2vw1p, 11)").highlight()

if __name__ == '__main__':
    json = Json.FileJson()

    def program():
        try:
            path = 'S:\PYTHON\AutoAnswer\Auto D\B'
            users = json.read("users", path)
            for user in dict(users).keys():
                Sala_Futuro(dict(users[user]))
        except Exception as e:
            print(f'ERRO NO PROGRAMA: {e}')

    program()
