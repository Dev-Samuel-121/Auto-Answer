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
        * Objetivo dessa função:
            TODO Fazer atividade
                TODO Identificar o que é e o que não é questão                      ✔
                TODO Categorizar as qeustões pelo seu TYPE (Radio, Checkbox, Drag-Drop, etc)      ✔

                ### TO MORROW ###

                TODO Extrair conteúdo (Pergnta, Alternativas)                                               ✔ ✖
                TODO Armazenar conteúdo em um arquivo JSON já preparado                                     ✔ ✖
                TODO Procurar resposta (ChatGPT, usar o JSON com o conteúdo e gerar as respostas)           ✔ ✖
                TODO Responder                                                                              ✔ ✖

                ??? ========================================= ***** ========================================= ???

                num_de_verificações = 0
                questao_atual = 0
                num_de_card_verificado = 0
                # num_questao_respondido = 0 -> Uma ideia para facilitar a forma verificar se todas as questões foram selecionadas
                
                ## DESCOBRIR QUANTAS VERIFICAÇÕES TEM QUE FAZER
                Contar quantos div.css-xz389d tem -> A div.css-xz389d são cada card

                FACA {
                    SE (dentro da :nth-match('div.css-xz389d, $') EXISTI a div.css-1mi3tt8 OU EXISTI a div.ytp-cued-thumbnail-overlay OU EXISTI a div.MuiBox-root.css-1ierx79 {
                        # Verificar se é PDF, VÍDEO ou GIF
                        Passa para próxima div.css-xz389d
                        num_de_card_verificado += 1
                    } SENÃO {
                        SE (dentro da :nth-match('div.css-xz389d, $') EXISTI div.MuiTypography-root.MuiTypography-subtitle2.css-qpwa0j) {
                            # Verificar se é Texto
                            Pegue todo texto das tags P dessa div
                            Armazene todo esse conteúdo no JSON
                            num_de_card_verificado += 1
                        } SENÃO {
                            SE (dentro da :nth:match('div.css-xz389d, $') EXISTI div.css-nlzma4) {
                                # Verifica o tipo de questão (Radios, Checkbox, etc)
                                questao_atual += 1
                                SE (dentro da :nth:match('div.MuiCard-root.css-1aksd3q, $') EXISTI span.MuiRadio-root.css-1sgsc5r) {
                                    # Aqui o Type dele é "Radio"
                                    Pega o conteúdo de todos os P dentro de todas as div.MuiBox-root.css-kmkory que estão dentro do pai que é div.MuiCard-root.css-1aksd3q, $ # Esse $ é a questao_atual
                                    Armazene todo esse conteúdo no JSON
                                    Vá para a página do ChatGPT (Abra uma nova guia, Entre em https://chatgpt.com/)
                                    Pega todo o conteúdo do JSON e coloca no ChatGPT
                                    Pega a resposta do ChatGPT que vai vim em formato JSON
                                    TODO Responder # Lógica para Responder
                                    num_de_card_verificado += 1
                                } SENÃO SE (dentro da :nth:match('div.MuiCard-root.css-1aksd3q, $') EXISTI span.MuiCheckbox-root.css-14bgux8) {
                                    # Aqui o Type dele é "Checkbox"
                                    Pega o conteúdo de todos os P dentro de todas as div.MuiBox-root.css-kmkory que estão dentro do pai que é div.MuiCard-root.css-1aksd3q, $ # Esse $ é a questao_atual
                                    Armazene todo esse conteúdo no JSON
                                    Vá para a página do ChatGPT (Abra uma nova guia, Entre em https://chatgpt.com/)
                                    Pega todo o conteúdo do JSON e coloca no ChatGPT
                                    Pega a resposta do ChatGPT que vai vim em formato JSON
                                    TODO Responder # Lógica para Responder
                                TODO } SENÃO SE (dentro da :nth:match('div.MuiCard-root.css-1aksd3q, $') EXISTI span.MuiCheckbox-root.css-14bgux8) {
                                !   # Aqui o Type dele é "Dragable"
                                !   Pega o conteúdo de todos os P dentro de todas as div.MuiBox-root.css-kmkory que estão dentro do pai que é div.MuiCard-root.css-1aksd3q, $ # Esse $ é a questao_atual
                                !   Armazene todo esse conteúdo no JSON
                                !   Vá para a página do ChatGPT (Abra uma nova guia, Entre em https://chatgpt.com/)
                                !   Pega todo o conteúdo do JSON e coloca no ChatGPT
                                !   Pega a resposta do ChatGPT que vai vim em formato JSON
                                TODO Responder # Lógica para Responder
                                TODO }SENÃO SE (dentro da :nth:match('div.MuiCard-root.css-1aksd3q, $') EXISTI span.MuiCheckbox-root.css-14bgux8) {
                                !   # Aqui o Type dele é "Right Wrong"
                                !   Pega o conteúdo de todos os P dentro de todas as div.MuiBox-root.css-kmkory que estão dentro do pai que é div.MuiCard-root.css-1aksd3q, $ # Esse $ é a questao_atual
                                !   Armazene todo esse conteúdo no JSON
                                !   Vá para a página do ChatGPT (Abra uma nova guia, Entre em https://chatgpt.com/)
                                !   Pega todo o conteúdo do JSON e coloca no ChatGPT
                                !   Pega a resposta do ChatGPT que vai vim em formato JSON
                                TODO Responder # Lógica para Responder
                                TODO }SENÃO SE (dentro da :nth:match('div.MuiCard-root.css-1aksd3q, $') EXISTI span.MuiCheckbox-root.css-14bgux8) {
                                !   # Aqui o Type dele é "Select"
                                !   Pega o conteúdo de todos os P dentro de todas as div.MuiBox-root.css-kmkory que estão dentro do pai que é div.MuiCard-root.css-1aksd3q, $ # Esse $ é a questao_atual
                                !   Armazene todo esse conteúdo no JSON
                                !   Vá para a página do ChatGPT (Abra uma nova guia, Entre em https://chatgpt.com/)
                                !   Pega todo o conteúdo do JSON e coloca no ChatGPT
                                !   Pega a resposta do ChatGPT que vai vim em formato JSON
                                TODO Responder # Lógica para Responder
                                TODO }SENÃO SE (dentro da :nth:match('div.MuiCard-root.css-1aksd3q, $') EXISTI span.MuiCheckbox-root.css-14bgux8) {
                                !   # Aqui o Type dele é "Textarea"
                                !   Pega o conteúdo de todos os P dentro de todas as div.MuiBox-root.css-kmkory que estão dentro do pai que é div.MuiCard-root.css-1aksd3q, $ # Esse $ é a questao_atual
                                !   Armazene todo esse conteúdo no JSON
                                !   Vá para a página do ChatGPT (Abra uma nova guia, Entre em https://chatgpt.com/)
                                !   Pega todo o conteúdo do JSON e coloca no ChatGPT
                                !   Pega a resposta do ChatGPT que vai vim em formato JSON
                                TODO Responder # Lógica para Responder
                                TODO } SENÃO SE (dentro da :nth:match('div.MuiCard-root.css-1aksd3q, $') EXISTI span.MuiCheckbox-root.css-14bgux8) {
                                !   # Aqui o Type dele é "Order"
                                !   Pega o conteúdo de todos os P dentro de todas as div.MuiBox-root.css-kmkory que estão dentro do pai que é div.MuiCard-root.css-1aksd3q, $ # Esse $ é a questao_atual
                                !   Armazene todo esse conteúdo no JSON
                                !   Vá para a página do ChatGPT (Abra uma nova guia, Entre em https://chatgpt.com/)
                                !   Pega todo o conteúdo do JSON e coloca no ChatGPT
                                !   Pega a resposta do ChatGPT que vai vim em formato JSON
                                TODO Responder # Lógica para Responder
                                TODO }
                                num_de_card_verificado += 1
                            }
                        }
                        VERIFICAR LIÇÃO SE AS ALTERNATIVAS FOR APENAS IMAGENS
                            PEDIR AO USUÁRIO PARA QUERESOLVA ESSA QUESTÃO
                        PEGA O TÍTULO DA QUESTÃO E AS ALTERNATIVAS DEPOIS ARMARZENA-LÁS NO JSON
                        PEGA O JSON COM A PERGUNTA E AS ALTERNATIVAS DA $ E PASSE PARA ChatGPT PARA QUE RESOLVA E RETORNE A RESPOSTA(s)
                        PEGA AS RESPOSTAS DESSE JSON E COLOUQE NA ALTERNATIVA CORRETA
                    }
                } ENQUANTO (num_de_card_verificado < num_de_verificações)
                
                * Adicionar forma de verificar se todas as questões foram selecionadas
                * Adicionar forma de clicar no botão enviar
                * Adicionar forma de verificar quantas você acertou
                * Adicionar forma de verificar quantas você errou
        '''
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
        '''
        """

        page.wait_for_timeout(5000)
        page.wait_for_timeout(5000)

run()
