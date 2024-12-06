from playwright.sync_api import sync_playwright

def login_estudante(page, ra, dg, uf, ps):
    """Realiza o login com as credenciais fornecidas."""
    acessoEstudante = page.locator('div#access-student')
    acessoEstudante.click()

    raa = page.locator('input#ra-student')
    raa.fill(ra)
    
    dgg = page.locator('input#digit-student')
    dgg.fill(dg)
    
    uff = page.locator('select#uf-student')
    uff.select_option(value=uf)
    
    pss = page.locator('input#password-student')
    pss.fill(ps)

    entrar = page.locator('input#btn-login-student')
    entrar.click()

def acessar_sala(page):
    """Acessa a sala de aula após o login."""
    sala = page.locator(
        ':nth-match(div#lproom_r783fda450260e0cbe-l.lproom_r783fda450260e0cbe-l.frm.w100.p10.pt, 4)'
    )
    sala.click()

def acessar_atividades(page):
    """Acessa a página de atividades."""
    page.goto("https://cmsp.ip.tv/mobile/tms?auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJza2V5IjoiYXV0aF90b2tlbjplZHVzcDpkYW5pZWxvbGl2ZTEwMDY1OTE4My1zcCIsIm5pY2siOiJkYW5pZWxvbGl2ZTEwMDY1OTE4My1zcCIsInJvbGUiOiIwMDA2IiwicmVhbG0iOiJlZHVzcCIsImlhdCI6MTczMzQ5MjQzNywiYXVkIjoid2ViY2xpZW50In0.Cb9gBJa-zktTjbfZRt3DiXq6l0u089-4Y_Bnq5JNMJg&room=r783fda450260e0cbe-l")
    todasAsAtividades = page.locator(':nth-match(div.MuiBox-root.css-p0pzb2, 2)')
    todasAsAtividades.click()

def verificar_elemento_existe(page, seletor):
    """Verifica a existencia de um elemento"""
    elemento = page.locator(seletor)
    
    # Verificar se o elemento existe
    if elemento.count() > 0:
        print("Tem lição.")
        return True
    else:
        print("Não tem lição.")
        return False

def ir_para_aba_expiradas(page):
    """Vai para a próxima seção"""
    trocarSecao = page.locator('div#language')
    trocarSecao.click()
    
    expiradas = page.locator(':nth-match(li.css-p0z5r, 2)')
    expiradas.click()
    
    print("Navegando para a aba 'Expiradas'.")

"""RUN"""

def run(ra, dg, uf, ps):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://cmspweb.ip.tv/login")
        
        login_estudante(page, ra, dg, uf, ps)
        acessar_sala(page)
        acessar_atividades(page)

        seletor_tabela = 'table.MuiTable-root.css-1rb4ifj'
        
        if verificar_elemento_existe(page, seletor_tabela):
            print("Existem lições para realizar.")
        else:
            print("Não há lições na aba 'A fazer'. Navegando para a aba 'Expiradas'.")
            ir_para_aba_expiradas(page)
            
            print("Verificando novamente na aba 'Expiradas'...")
            page.wait_for_selector(seletor_tabela)

            if verificar_elemento_existe(page, seletor_tabela):
                print("Existem lições na aba 'Expiradas'.")
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
    