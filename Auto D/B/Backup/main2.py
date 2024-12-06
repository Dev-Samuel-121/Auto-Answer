import time
from playwright.sync_api import sync_playwright

# Credenciais
us1 = 'daniel_oliveira_matias'
ps1 = 'SlS34914909SlS'
us2 = 'samuel_oliveira_matias'
ps2 = 'SlS34914909SlS'

def run():
    with sync_playwright() as p:
        # Montando Browser
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("https://eadtec.cps.sp.gov.br/")
        
        # Acesso Estudante
        usuario = page.locator('input#usuario')
        usuario.fill(us1)
        senha = page.locator('input#senha')
        senha.fill(ps1)
        entrar = page.locator('input#bt_entrar')
        entrar.click()
        page.wait_for_timeout(15000)

run()

