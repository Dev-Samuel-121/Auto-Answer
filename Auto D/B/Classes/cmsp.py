from playwright.sync_api import sync_playwright
import Classes.FileJson as Json
import Classes.khan_academy as KhanAcademy
import Classes.leia_sp as LeiaSP
import Classes.me_salva as MeSalva
import Classes.provas_atividades as ProvasAtividades
import Classes.speak as Speak

"""
OBJETIVOS:
    CRIAR OS MÉTODOS DE ACESSO AS OUTRAS PLATAFORMAS(HJ/AM);
    CRIR OS PRIMEIOS PROTOTIPOS DE INTERFACE DE USUÁRIO(MAIS PARA FRENTE);
"""

class CMSP():
    def __init__(self, user, plataformas):
        self.page = "https://cmspweb.ip.tv/"
        self.user = user
        self.plataformas = plataformas
        self.engine(self.user, self.page, self.plataformas)

    def engine(self, user, page, plataformas):
        try:
            with sync_playwright() as program:
                browser = program.chromium.launch(headless=False, slow_mo=500)
                page = browser.new_page()
                page.goto(self.page)
                self.entrada(user, page)
                # self.verificar_plataformas(plataformas, user)
        except Exception as e:
            print(f'ERRO NO ENGINE: {e}')
    
    def khan_academy(self):
        try:
            button = 'img[src="https://s3.sa-east-1.amazonaws.com/edusp-static.ip.tv/room/cards/edusp/elianemararod3272389-sp/LgpmslZ5LlI3soKX2lulNpjhYXhx7C.png"]'
            button.highlight()
            button.click()
        except Exception as e:
            print(f'ERRO AO ACESSAR O COM O CMSP: {e}')
    
    def leia_sp(self):
        try:
            button = 'img[src="https://s3.sa-east-1.amazonaws.com/edusp-static.ip.tv/room/cards/edusp/elianemararod3272389-sp/ZLEPCTfa0Iz4Bzbrv7Lkl2cz2JFluu.png"]'
            button.highlight()
            button.click()
        except Exception as e:
            print(f'ERRO AO ACESSAR O COM O CMSP: {e}')

    def me_salva(self):
        try:
            button = 'img[src="https://s3.sa-east-1.amazonaws.com/edusp-static.ip.tv/room/cards/edusp/elianemararod3272389-sp/e6TVO7cyptJu5lb6wSUTwyYUtlgVd5.png"]'
            button.highlight()
            button.click()
        except Exception as e:
            print(f'ERRO AO ACESSAR O COM O CMSP: {e}')
    
    def provas_atividades(self):
        try:
            button = ''
            button.highlight()
            button.click()
        except Exception as e:
            print(f'ERRO AO ACESSAR O COM O CMSP: {e}')
    
    def speak(self):
        try:
            button = 'img[src="https://s3.sa-east-1.amazonaws.com/edusp-static.ip.tv/room/cards/edusp/julianasanche3225895-sp/OssSPvVLLQCMBVxQ2ERP3Q36wgHq8W.png"]'
            button.highlight()
            button.click()
        except Exception as e:
            print(f'ERRO AO ACESSAR O COM O CMSP: {e}')
    
    # def verificar_plataformas(self, plataformas, user):
    #     list(plataformas)
    #     for plataforma in plataformas:
    #         if plataforma == "KhanAcademy":
    #             KhanAcademy.Khan_Academy(user).acessar_cmsp()
    #         elif plataforma == "LeiaSP":
    #             LeiaSP.Leia_Sp(user).acessar_cmsp()
    #         elif plataforma == "MeSalva":
    #             MeSalva.Me_Salva(user).acessar_cmsp()
    #         elif plataforma == "ProvasAtividades":
    #             ProvasAtividades.Provas_Atividades(user).acessar_cmsp()
    #         elif plataforma == "Speak":
    #             Speak.Speak(user).acessar_cmsp()
    #         else:
    #             print(f'PLATAFORMA INCORRETA: {plataforma}')

    def entrada(self, user, page):
        try:
            self.login(user, page)
            self.acessar_sala(page)
            # self.acessar_atividades(page)
        except Exception as e:
            print(f'ERRO NA ENTRADA: {e}')

    def login(self, user, page):
        try:
            dict(user)
            page.locator('div#access-student').click()
            page.locator('input#ra-student').fill(user['ra'])
            page.locator('input#digit-student').fill(user['dg'])
            page.locator('select#uf-student').select_option(value=user['uf'])
            page.locator('input#password-student').fill(user['password'])
            page.locator('input#btn-login-student').click()
        except Exception as e:
            print(f'ERRO NO LOGIN: {e}')
    
    def acessar_sala(self, page):
        try:
            sala = page.locator(':nth-match(div#lproom_r783fda450260e0cbe-l.lproom_r783fda450260e0cbe-l.frm.w100.p10.pt, 4)')
            sala.click()
        except Exception as e:
            print(f'ERRO AO ACESSAR A SALA: {e}')

    def acessar_atividades(self, page):
        try:
            url_atividades = "https://cmsp.ip.tv/mobile/tms?auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJza2V5IjoiYXV0aF90b2tlbjplZHVzcDpkYW5pZWxvbGl2ZTEwMDY1OTE4My1zcCIsIm5pY2siOiJkYW5pZWxvbGl2ZTEwMDY1OTE4My1zcCIsInJvbGUiOiIwMDA2IiwicmVhbG0iOiJlZHVzcCIsImlhdCI6MTczMzUxOTYwOSwiYXVkIjoid2ViY2xpZW50In0.oqO-eR0IwyvdISxDKoKaGCsQI4dXw-3S9tUblegiV4g&room=r783fda450260e0cbe-l"
            page.goto(url_atividades)
            page.locator(':nth-match(div.MuiBox-root.css-p0pzb2, 2)').click()
        except Exception as e:
            print(f'ERRO AO ACESSAR AS ATIVIDADES: {e}')
    
    def verificar_elemento_existe(self, page, seletor):
        """Verifica a existência de um elemento na página."""
        elemento = page.locator(seletor)
        if elemento.count() > 0:
            print("Elemento encontrado.")
            return True
        else:
            print("Elemento não encontrado.")
            return False

    def rolar_ate_ultimo_item(self, page, seletor_atividades):
        """Rola até o último item da página de atividades."""
        atividades = page.locator(seletor_atividades)
        total_atividades = atividades.count()

        if total_atividades > 0:
            print(f"Total de atividades encontradas: {total_atividades}")
            ultimo_item = page.locator(f'{seletor_atividades}:nth-match({seletor_atividades}, {total_atividades})')
            ultimo_item.scroll_into_view_if_needed()
            print(f"Rolando até o último item (atividade {total_atividades}).")
        else:
            print("Não há atividades para rolar.")

    def contar_atividades_pendentes(self, page, seletor_atividades):
        """Conta as atividades pendentes na página e retorna o total de atividades."""
        atividades = page.locator(seletor_atividades)
        atividades_iniciais = atividades.count()
        print(f"Atividades iniciais encontradas: {atividades_iniciais}")

        rolagem = 1
        while rolagem > 0:
            self.rolar_ate_ultimo_item(page, seletor_atividades)
            page.wait_for_timeout(500)

            atividades_atualizadas = atividades.count()
            if atividades_atualizadas > atividades_iniciais:
                print(f"Número de atividades aumentou: {atividades_atualizadas}")
                atividades_iniciais = atividades_atualizadas
                rolagem += 1
            else:
                print("Número de atividades não aumentou, presumindo que não há mais lições.")
                rolagem = 0

        print(f"Total de atividades encontradas: {atividades_iniciais}")
        return atividades_iniciais

    def ir_para_aba_expiradas(self, page):
        """Vai para a aba 'Expiradas'."""
        page.locator('div#language').click()
        page.locator(':nth-match(li.css-p0z5r, 2)').click()
        print("Navegando para a aba 'Expiradas'.")

    def validar_atividade_realizavel(self, page, seletor_botao_realizar):
        """Validar atividade"""
        botao_realizar = page.locator(seletor_botao_realizar)
        
        if botao_realizar.locator('span.css-1l6c7y9').count() > 0:
            print("A atividade NÃO pode ser realizada (Botão com span).")
            return False
        
        elif botao_realizar.inner_text() != "Realizar":
            print("A atividade NÃO pode ser realizada (Texto diferente de 'Realizar').")
            return False
        
        print("A atividade PODE ser realizada.")
        return True

    def fazer_atividade(self, page, seletor_botao_realizar):
        """Fazer Atividade"""
        page.locator(seletor_botao_realizar).click()
        print("Atividade realizada!")

    def clicar_atividade(self, page, seletor_atividade):
        """Clica na atividade"""
        
        atividade_btn = page.locator(seletor_atividade)
        
        atividade_btn.scroll_into_view_if_needed()
        
        atividade_btn.wait_for(state="visible")
        
        atividade_btn.click()
        print("Atividade clicada.")

    """ RUN """

    # def run(ra, dg, uf, ps):
    #     """Função principal para executar o fluxo do bot."""
    #     with sync_playwright() as p:
    #         browser = p.chromium.launch(headless=False)
    #         page = browser.new_page()
    #         page.goto("https://cmspweb.ip.tv/login")
            
    #         login_estudante(page, ra, dg, uf, ps)
    #         acessar_sala(page)
    #         acessar_atividades(page)
            
    #         seletor_tabela = 'table.MuiTable-root.css-1rb4ifj'
    #         seletor_atividades = 'button.css-k9aczr'
    #         seletor_botao_realizar = 'button.css-1hmr1hq'
            
    #         if verificar_elemento_existe(page, seletor_tabela):
    #             print("Existem lições para realizar.")
    #             atividades_pendentes = contar_atividades_pendentes(page, seletor_atividades)
    #             print(f"Há {atividades_pendentes} atividades pendentes para realizar na aba 'A fazer'.")
                
    #             for i in range(1, atividades_pendentes + 1):
    #                 seletor_atividade = f":nth-match({seletor_atividades}, {i})"
                    
    #                 clicar_atividade(page, seletor_atividade)
                    
    #                 page.wait_for_selector(seletor_botao_realizar)
                    
    #                 if validar_atividade_realizavel(page, seletor_botao_realizar):
    #                     fazer_atividade(page, seletor_botao_realizar)
    #                 else:
    #                     print("Atividade não pode ser realizada. Fechando o modal...")
    #                     page.locator(seletor_atividade).click()
    #                     page.wait_for_timeout(500)
    #         else:
    #             print("Não há lições na aba 'A fazer'. Navegando para a aba 'Expiradas'.")
    #             ir_para_aba_expiradas(page)
    #             print("Verificando novamente na aba 'Expiradas'...")
    #             page.wait_for_selector(seletor_tabela)
                
    #             if verificar_elemento_existe(page, seletor_tabela):
    #                 print("Existem lições na aba 'Expiradas'.")
    #                 atividades_pendentes = contar_atividades_pendentes(page, seletor_atividades)
    #                 print(f"Há {atividades_pendentes} atividades pendentes para realizar na aba 'Expiradas'.")
                    
    #                 for i in range(1, atividades_pendentes + 1):
    #                     seletor_atividade = f":nth-match({seletor_atividades}, {i})"
                        
    #                     clicar_atividade(page, seletor_atividade)
                        
    #                     page.wait_for_selector(seletor_botao_realizar)
                        
    #                     if validar_atividade_realizavel(page, seletor_botao_realizar):
    #                         fazer_atividade(page, seletor_botao_realizar)
    #                     else:
    #                         print("Atividade não pode ser realizada. Fechando o modal...")
    #                         page.locator(seletor_atividade).click()
    #                         page.wait_for_timeout(500)
    #             else:
    #                 print("Não há lições na aba 'Expiradas'.")
            
    #         page.wait_for_timeout(5000)
    #         browser.close()
        

json = Json.FileJson()

def create_users():
    try:
        users = {
            "U1": {
                "ra": "110065918",
                "dg": "3",
                "uf": "sp",
                "email":"00001100659183sp@al.educacao.sp.gov.br",
                "password": "Bp110065#"
            },
            "U2": {
                "ra": "110065923",
                "dg": "7",
                "uf": "sp",
                "email":"00001100659237sp@al.educacao.sp.gov.br",
                "password": "Bp110065#"
            }
        }
    
        json.create("users", users)
    except Exception as e:
        print(f'ERRO NA CRIAÇÃO DO(S) USUARIO(S): {e}')

def program():
    try:
        users = json.read("users")
        plataformas = ["KhanAcademy", "LeiaSP", "MeSalva", "ProvasAtividades", "Speak"]
        for user in dict(users).keys():
            CMSP(dict(users[user]), plataformas)
    except Exception as e:
        print(f'ERRO NO PROGRAMA: {e}')

create_users()
program()
