from playwright.sync_api import sync_playwright


def login_estudante(page, ra, dg, uf, ps):
    """Realiza o login com as credenciais fornecidas."""
    page.locator('div#access-student').click()
    page.locator('input#ra-student').fill(ra)
    page.locator('input#digit-student').fill(dg)
    page.locator('select#uf-student').select_option(value=uf)
    page.locator('input#password-student').fill(ps)
    page.locator('input#btn-login-student').click()


def acessar_sala(page):
    """Acessa a sala de aula após o login."""
    sala = page.locator(':nth-match(div#lproom_r783fda450260e0cbe-l.lproom_r783fda450260e0cbe-l.frm.w100.p10.pt, 4)')
    sala.click()


def acessar_atividades(page):
    """Acessa a página de atividades."""
    url_atividades = "https://cmsp.ip.tv/mobile/tms?auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJza2V5IjoiYXV0aF90b2tlbjplZHVzcDpkYW5pZWxvbGl2ZTEwMDY1OTE4My1zcCIsIm5pY2siOiJkYW5pZWxvbGl2ZTEwMDY1OTE4My1zcCIsInJvbGUiOiIwMDA2IiwicmVhbG0iOiJlZHVzcCIsImlhdCI6MTczMzUxOTYwOSwiYXVkIjoid2ViY2xpZW50In0.oqO-eR0IwyvdISxDKoKaGCsQI4dXw-3S9tUblegiV4g&room=r783fda450260e0cbe-l"
    page.goto(url_atividades)
    page.locator(':nth-match(div.MuiBox-root.css-p0pzb2, 2)').click()


def verificar_elemento_existe(page, seletor):
    """Verifica a existência de um elemento na página."""
    elemento = page.locator(seletor)
    if elemento.count() > 0:
        print("Elemento encontrado.")
        return True
    else:
        print("Elemento não encontrado.")
        return False


def rolar_ate_ultimo_item(page, seletor_atividades):
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


def contar_atividades_pendentes(page, seletor_atividades):
    """Conta as atividades pendentes na página."""
    atividades = page.locator(seletor_atividades)
    atividades_iniciais = atividades.count()
    print(f"Atividades iniciais encontradas: {atividades_iniciais}")

    rolagem = 1
    while rolagem > 0:
        rolar_ate_ultimo_item(page, seletor_atividades)
        page.wait_for_timeout(5000)

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


def ir_para_aba_expiradas(page):
    """Vai para a aba 'Expiradas'."""
    page.locator('div#language').click()
    page.locator(':nth-match(li.css-p0z5r, 2)').click()
    print("Navegando para a aba 'Expiradas'.")


def run(ra, dg, uf, ps):
    """Função principal para executar o fluxo do bot."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://cmspweb.ip.tv/login")
        
        login_estudante(page, ra, dg, uf, ps)
        acessar_sala(page)
        acessar_atividades(page)
        
        seletor_tabela = 'table.MuiTable-root.css-1rb4ifj'
        seletor_atividades = 'button.css-k9aczr'
        
        if verificar_elemento_existe(page, seletor_tabela):
            print("Existem lições para realizar.")
            atividades_pendentes = contar_atividades_pendentes(page, seletor_atividades)
            print(f"Há {atividades_pendentes} atividades pendentes para realizar na aba 'A fazer'.")
        else:
            print("Não há lições na aba 'A fazer'. Navegando para a aba 'Expiradas'.")
            ir_para_aba_expiradas(page)
            print("Verificando novamente na aba 'Expiradas'...")
            page.wait_for_selector(seletor_tabela)
            if verificar_elemento_existe(page, seletor_tabela):
                print("Existem lições na aba 'Expiradas'.")
                atividades_pendentes = contar_atividades_pendentes(page, seletor_atividades)
                print(f"Há {atividades_pendentes} atividades pendentes para realizar na aba 'Expiradas'.")
            else:
                print("Não há lições na aba 'Expiradas'.")
        
        page.wait_for_timeout(5000)
        browser.close()

# Dados para o login
if __name__ == '__main__':
    ra = "110065918"
    dg = "3"
    uf = "SP"
    ps = "Bp110065#"
    run(ra, dg, uf, ps)


"""

FUNÇÕES A SEREM ADICIONADAS

def verificar_licoes_na_aba():
    # Verificar se existe a div que indica que não há lições para fazer
    if existe_elemento("div.css-1iovhr3"):  # Você pode usar uma função que verifica a existência do elemento
        return False  # Não há lições para fazer
    return True  # Há lições para fazer

def contar_atividades():
    # Contar quantos botões de atividade existem
    return contar_elementos("button.css-k9aczr")  # Esta função deve contar os elementos com essa classe

def pode_realizar_atividade(botao_atividade):
    # Verificar se a lição pode ser realizada
    if existe_elemento_dentro(botao_atividade, "span.css-1l6c7y9"):
        return False  # Não pode realizar, tem o span indicando que está bloqueada
    if obter_texto(botao_atividade) != "Realizar":
        return False  # Se o texto do botão não for "Realizar", não pode realizar
    return True  # Pode realizar

def realizar_atividade(botao_atividade):
    # Subtrair 1 das atividades restantes
    atividades_restantes = atividades_restantes - 1
    # Clicar no botão para realizar a atividade
    clicar_elemento(botao_atividade)

"""
    