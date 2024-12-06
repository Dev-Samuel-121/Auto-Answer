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

        sala = page.locator(
            ':nth-match(div#lproom_r783fda450260e0cbe-l.lproom_r783fda450260e0cbe-l.frm.w100.p10.pt, 4)'
        )
        sala.click()

        # Acesso Todas as atividades
        page.goto("https://cmsp.ip.tv/mobile/tms?auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJza2V5IjoiYXV0aF90b2tlbjplZHVzcDpkYW5pZWxvbGl2ZTEwMDY1OTE4My1zcCIsIm5pY2siOiJkYW5pZWxvbGl2ZTEwMDY1OTE4My1zcCIsInJvbGUiOiIwMDA2IiwicmVhbG0iOiJlZHVzcCIsImlhdCI6MTczMzQ5MjQzNywiYXVkIjoid2ViY2xpZW50In0.Cb9gBJa-zktTjbfZRt3DiXq6l0u089-4Y_Bnq5JNMJg&room=r783fda450260e0cbe-l")
        todasAsAtividades = page.locator(
            ':nth-match(div.MuiBox-root.css-p0pzb2, 2)'
        )
        todasAsAtividades.click()

        """
        https://chatgpt.com/c/675351ca-e478-800a-9871-8b626af06d54
        * Objetivo dessa função:
            TODO Verificar se há lição na aba "A fazer"                     ✔
            TODO Verificar se há lição na aba "Expiradas"                   ✔ ✖
            TODO Verificar quantas lições tem para fazer na Aba atual       ✔ ✖
            TODO Validar se dá para fazer a lição ou não                    ✔ ✖
            TODO Fazer atividade                                            ✔ ✖

        * ASDFASDFASDÇLK

        FACA {
            SE (EXISTI a div.css-1iovhr3) { ## OU SEJA, significa que não há nada apenas um SVG para mostrar que não há nada
                Vá para expiradas (CLICK na div#language SELECIONE a li cujo data-value="expired:all") ## VÁ para próxima seção
            } senão {
                SABER quantos button.css-k9aczr TEM e coloque na variavel Atividades ## SABER quantos button.css-k9aczr tem, ajuda nós a identificar quantas ATIVIDADES tem para fazer
                CLICK no PRIMEIRO button.css-k9aczr e BUSQUE por btn.css-1hmr1hq ## CLICAMOS para abrir a div e validar se dá ou não para realizar a atividade
                SE (
                    dentro da div.css-nzomx6 no btn.css-1hmr1hq tiver span.css-1l6c7y9 ## Se há esse span NÃO DÁ PARA REALIZAR A ATIVIDADE
                    OU
                    O conteúdo do btn.css-1hmr1hq for ! de "Realizar") { # SE o TEXTO do botão for diferente então não dá para REALIZAR
                ) {
                    CLICK no PRÓXIMO button.css-k9aczr e BUSQUE por btn.css-1hmr1hq  # Se tudo acima for verdade, vamos passar para o proximo botão e refazer os mesmos passos
                } SE NÃO { # Se as afirmações acima forem falso, então significa que é uma ATIVIDADE e dá para REALIZAR
                    Subtraia -1 nas ativadades # Subtrair 1 das atividades para o programa saber quantas atividades ainda faltam
                    Click no btn.css-1hmr1hq # Clicar no botão para realizar
                }
            }
        } ENQUANTO(Atividades > 0) # Faça tudo isso enquanto ainda tiver atividades
        """

        page.wait_for_timeout(5000)
        page.wait_for_timeout(5000)

run()
