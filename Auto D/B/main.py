import time
from playwright.sync_api import sync_playwright

# Credenciais
ra = '110065918'
dg = '3'
uf = 'sp'
ps = 'Bp110065#'

def run():
    with sync_playwright() as p:
        # Montando Browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://cmspweb.ip.tv/login")

        # Acesso Estudante
        acessoEstudante = page.locator('div#access-student')
        acessoEstudante.click()

        # Colocando Credenciais do Estudante
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
        
        page.wait_for_event('load', timeout=30000)  # Espera até o carregamento da página ser concluído

        # Espera até que a sala de acesso esteja disponível
        sala = page.locator('div#lproom_r783fda450260e0cbe-l')
        sala.wait_for(state='visible', timeout=30000)  # Espera até o elemento aparecer
        sala.click()

        # Espera até as provas e atividades estarem disponíveis
        provasEAtividades = page.locator('div#roomDetailTms')
        provasEAtividades.wait_for(state='visible', timeout=30000)  # Espera até o elemento aparecer
        provasEAtividades.click()

        # Espera o ícone de todas as atividades ficar visível
        todasAsAtividades = page.locator('div.MuiAvatar-root.MuiAvatar-circular.MuiAvatar-colorDefault.css-1ra3t6t')
        todasAsAtividades.wait_for(state='visible', timeout=30000)  # Espera até o elemento aparecer
        todasAsAtividades.click()

        # Alternativa com espera mais eficiente
        page.wait_for_event('load', timeout=30000)  # Espera até o carregamento da página ser concluído

        # Espera um tempo adequado ou até o carregamento final (alternativa)
        page.wait_for_timeout(120000)  # Espera por 120 segundos (em milissegundos)

run()
