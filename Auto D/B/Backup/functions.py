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