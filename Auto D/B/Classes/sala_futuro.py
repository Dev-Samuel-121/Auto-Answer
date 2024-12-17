import os
import FileJson as Json
from playwright.sync_api import sync_playwright
"""
from playwright.sync_api import sync_playwright
program = sync_playwright().start()
browser = program.chromium.launch(headless=False)
page = browser.new_page()
page.goto('https://saladofuturo.educacao.sp.gov.br/')
page.locator('button[data-testid="botao-login-sed"]').click()
page.locator(':nth-match(.css-1frrzr1, 1)').fill("110065923")
page.locator(':nth-match(.css-1frrzr1, 2)').fill("7")
page.locator('.css-r1nef8').click()
page.locator(f'li.css-4dqmvd[data-value="SP"]').click()
page.locator('.css-scvshb').fill("Bp110065#")
page.locator('button#botao-login-sed').click()

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
                page.wait_for_timeout(5000)
        except Exception as e:
            print(f'ERRO NO ENGINE: {e}')
    
    def entrada(self, user, page):
        try:
            self.login(user, page)
            self.atividades_pendentes(page)
            self.tarefa_sp(page)
        except Exception as e:
            print(f'ERRO NA ENTRADA: {e}')

    def login(self, user, page):
        page.locator('button[data-testid="botao-login-sed"]').click()
        page.locator(':nth-match(.css-1frrzr1, 1)').fill(user['ra'])
        page.locator(':nth-match(.css-1frrzr1, 2)').fill(user['dg'])
        page.locator('.css-r1nef8').click()
        page.locator(f'li.css-4dqmvd[data-value="{str(user['uf']).upper()}"]').click()
        page.locator('.css-scvshb').fill(user['password'])
        page.locator('.css-56yhrg').click()

    def verificacao_inicial(self, page):
        tarefas = self.atividades_pendentes(page)
        # VERIFICAR O NÚMERO DE FALTAS;
        pass
    
    def atividades_pendentes(self, page):
        try:
            geral = page.text_content(":nth-match(.css-15j76c0, 1)")
            page.locator(".css-1odjefb").click()
            tarefas = page.text_content(":nth-match(.css-1qedkgf, 1)")
            redacao = page.text_content(":nth-match(.css-1qedkgf, 2)")
            prova = page.text_content(":nth-match(.css-1qedkgf, 3)")
            resultado = {
                "tarefas":str(tarefas),
                "redacao":str(redacao),
                "prova":str(prova),
                "geral":str(geral)
            }
            page.locator(".css-jzfio7").click()
            return resultado
        except Exception as e:
            print(f'ERRO AO PEGAR O NÚMERO DE ATIVIDADES PENDENTES: {e}')

    def tarefa_sp(self, page):
        try: 
            """
            * 'TODO': VERIFICAR SE TEM ATIVIDADES NA PAGINA INICIAL PARA FAZER; ✔
            * 'TODO': MUDAR PARA 'TODAS AS ATIVIDADES'; ✔
            * 'TODO': EM CADA CARD VERIFICAR (TITULO, MATERIA, STATUS); ✔
            * 'TODO': PARA CADA CARD PEGAR AS INFORMAÇÕES; ✔
            """
            """
            # page.locator(".css-5vgve0").highlight() # SE EXISTIR ISSO, NÃO TEM ATIVIDADES PARA FAZER.
            # page.locator(":nth-match(.css-39ukww, 1)").highlight() # DRAGDOW DE TURMAS.
            # page.locator(".css-wiwm8n") # CARD DAS ATIVIDADES.
            # page.locator(".css-15734jk") # MATERIA DA ATIVIDADE.
            # page.locator('p[data-testid="status-cartao-tarefa"]') # STATUS DA ATIVIDADE.
            # page.locator('p[data-testid="cartao-tarefa-titulo"]') # TITULO DA ATIVIDADE.
            # page.locator('div.css-j7qwjs') # CONTEUDO GERAL DA ATIVIDADE.
            # page.locator('p.css-p4uj5v') # TEXTO DO BOTÃO DA ATIVIDADE.
            # page.locator(':nth-match(p.css-1yy41dc, 1)') # NOTA.
            # page.locator(':nth-match(p.css-1yy41dc, 2)') # DURAÇÃO.
            # page.locator(':nth-match(p.css-1yy41dc, 3)') # ULTIMA ATUALIZAÇÃO.
            # page.locator('p.css-197c44q') # DATA DA ENTREGA.
            # page.locator('button.css-j0wy23') # BOTÃO DA ATIVIDADE.
            #* 'TODO': CONTINUAR A PROSEGUIR NO CÓDIGO, PEGAR CADA ATIVIDADE E VERIFICAR SE PODE FAZER OU NÃO.
            """
            """
            * MUDAR PARA AS OUTROS TIPOS DE ATIVIDADES;
            # page.locator(":nth-match(.css-1ep6xdl, 2)").highlight() # AFAZER.
            # page.locator(":nth-match(.css-1ep6xdl, 3)").highlight() # RASCUNHOS.
            # page.locator(":nth-match(.css-1ep6xdl, 4)").highlight() # EM CORREÇÃO.
            # page.locator(":nth-match(.css-1ep6xdl, 5)").highlight() # REVISAR.
            # page.locator(":nth-match(.css-1ep6xdl, 6)").highlight() # CONCLUIDAS.
            # page.locator(":nth-match(.css-1ep6xdl, 7)").highlight() # EXPIRADAS.
            # page.locator(":nth-match(.css-1ep6xdl, 8)").highlight() # PENDENTES.
            """
            page.locator(":nth-match(.css-w2vw1p, 3)").click()
            page.locator(":nth-match(.css-39ukww, 2)").click() # DRAGDOW DE ATIVIDADES.
            page.locator(":nth-match(.css-1ep6xdl, 1)").click() # TODAS AS ATIVIDADES.
            numero_cards = self.verificar_novos_card(page)
            self.info_card(page, numero_cards)
        except Exception as e:
            print(f'ERRO NA PLATAFORMA "TAREFA SP": {e}')

    #* DEPOIS COLOCAR O IDENTIFICADOR, PARA NÃO FICAR APENAS PARA OS CARDS.
    # def verificar_novos_card(self, page, identificador):
    def verificar_novos_card(self, page):
        try:
            # CÓDIGO ORIGINAL
            page.wait_for_timeout(1500)
            total_cards_encontrados = page.locator(".css-wiwm8n").count()
            cards_encontrados = 0

            while total_cards_encontrados > 0:
                page.locator(f':nth-match(.css-wiwm8n, {total_cards_encontrados})').scroll_into_view_if_needed()
                page.wait_for_timeout(2000)
                cards_encontrados = int(page.locator(".css-wiwm8n").count())

                if cards_encontrados > total_cards_encontrados:
                    total_cards_encontrados = cards_encontrados
                    print(f'CARDS ENCONTRADOS = {total_cards_encontrados}')
                    print('-'*50)
                else:
                    print(f'TOTAL CARDS ENCONTRADOS = {total_cards_encontrados}')
                    print('-'*50)
                    return total_cards_encontrados
        except Exception as e:
            print(f'ERRO NA VERIFICAÇÃO DE NOVOS CARDS: {e}')

    def fazer(self):
        pass

    def rascunho(self):
        text = "Rascunho"
        pass

    def correcao(self):
        pass

    def revisar(self):
        pass

    def concluido(self):
        text = "Concluída"
        pass

    def expirado(self):
        text = "Expirada"
        pass

    def pendente(self):
        pass

    def info_card(self, page, numero_card):
        try: 
            materia = page.text_content(f':nth-match(.css-15734jk, {numero_card})') # MATERIA DA ATIVIDADE.
            status = page.text_content(f':nth-match(p[data-testid="status-cartao-tarefa"], {numero_card})') # STATUS DA ATIVIDADE.
            titulo = page.text_content(f':nth-match(p[data-testid="cartao-tarefa-titulo"], {numero_card})') # TITULO DA ATIVIDADE.
            path = os.path.join(str(os.getcwd()), str("ATIVIDADES"), str(materia).upper(), str(f'{materia} - {titulo}').upper())
            if not os.path.exists(path):
                os.makedirs(path)
            print(path)
            
            # AS INFORMAÇÕES SOBRE CADA CARD SÓ APARECEM QUANDO O CARD É CLICADO OU O MOUSE ESTÁ SOBRE
            page.locator(f':nth-match(.css-wiwm8n, {numero_card})').click()
            nota = page.text_content(':nth-match(p.css-1yy41dc, 1)') # NOTA.
            duracao = page.text_content(':nth-match(p.css-1yy41dc, 2)') # DURAÇÃO.
            ultima_atualizacao = page.text_content(':nth-match(p.css-1yy41dc, 3)') # ULTIMA ATUALIZAÇÃO.
            data_entrega = page.text_content('p.css-197c44q') # DATA DA ENTREGA.
            
            info_atividade = {
                "titulo":str(titulo),
                "materia":str(materia),
                "status":str(status),
                "nota":str(nota),
                "duracao":str(duracao),
                "ultima_atualizacao":str(ultima_atualizacao),
                "data_entrega":str(data_entrega)
            }
            print(info_atividade)
            print('-'*50)
            # json.create(path, info_atividade)
            return info_atividade
        except Exception as e:
            print(f'ERRO NA COLETA DE INFORMAÇÕES DO CARD: {e}')

    def realizando_atividade(self, page):
        """
        * QUESTÃO
        div.css-b200pa - CARD/CONTAINER DA QUESTÃO
        div.css-1a4wlpz - TEXTO DA QUESTÃO
        div.css-1p78i1z - TEXTO DA ALTERNATIVA
        input.css-1m9pwf3 - BOTÃO DA ALTERNATIVA (RADIO, CHECKBOX)
        textarea.css-qgefwl - CAMPO DE RESPOSTA DA ALTERNATIVA (TEXTAREA)

        * BOTÕES DA PAGINA
        button.css-fm81so - BOTÃO VOLTAR
        button.css-1wjnhbh - BOTÃO SALVAR RASCUNHO
        button[data-testid="botao-finalizar"] - BOTÃO FINALIZAR
        """

    def realizando_prova(self, page):
        """
        * MAPA/MENU SUSPENSO
        div[data-testid="container-mapa-botoes"] - MAPA DAS QUESTÕES
        button[data-testid="single"] - CAMINHO DAS QUESTÕES[1, 2, 3, 4, 5, ...]
        :nth-match(div.css-8atqhb, 4) - TITULO DA MATERIA
        :nth-match(div.css-8atqhb, 5) - TITULO DA PERGUNTA E TITULO
        div.css-1x4ovfg - CONTEINER DA ALTERNATIVA
        div.css-1p78i1z - TEXTO DA ALTERNATIVA
        input[name="question-choice"] - BOTÃO DA ALTERNATIVA
        
        * BOTÕES DA PAGINA
        button.css-11iafso - BOTÃO PARA IR PARA A PERGUNTA ANTERIOR
        button.css-1y5nd6d - BOTÃO PARA IR PARA A PROXIMA PERGUNTA
        button.css-fm81so - BOTÃO PARA VOLTAR/SAIR
        """

    def speak(self, page):
        page.locator(":nth-match(.css-w2vw1p, 5)").highlight()

    def leia_sp(self, page):
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
