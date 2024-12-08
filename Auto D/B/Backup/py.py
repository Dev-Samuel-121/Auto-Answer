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

                !# num_de_verificações = 0 # Aqui vamos contar o número de verificações para cada card 
                questao_atual = 0 # Identificar a questão atual e facilitar a especificação dos elementos dentro dela
                text_atual = 0 # Identificar o texto atual e facilitar a especificação dos elementos dentro dela
                numero_de_card_verificado = 0 # Será para ajudar 
                numero_questao_respondido = 0
                
                ## DESCOBRIR QUANTAS VERIFICAÇÕES TEM QUE FAZER
                numero_de_card = número de div.css-xz389d # A div.css-xz389d são cada card

                FACA { # Vamos fazer tudo isso enquanto o número de numero_de_card for menor que o numero_de_card_verificado
                    SE (dentro da :nth-match('div.css-xz389d, numero_de_card_verificado') EXISTI a div.css-1mi3tt8 OU EXISTI a div.ytp-cued-thumbnail-overlay OU EXISTI a div.MuiBox-root.css-1ierx79 { # Esse numero_de_card_verificado ajuda a saber qual é o card atual
                        # Se existir então temos aqui tem um PDF ou VÍDEO ou GIF
                        SE (dentro da :nth-match('div.css-xz389d, numero_de_card_verificado') EXISTI div.MuiTypography-root.MuiTypography-subtitle2.css-qpwa0j) {
                            # Se tiver um deles vamos verificar se EXISTI div.MuiTypography-root.MuiTypography-subtitle2.css-qpwa0j o que significa que temos um breve texto sobre o assunto
                            text_atual += 1 # Para saber em qual texto estamos
                            numero_de_card_verificado += 1 # Para saber em qual card estamos e se já foi verificado
                            Pega todo o texto das tags P que estão dentro do :nth-match('div.MuiTypography-root.MuiTypography-subtitle2.css-qpwa0j, text_atual')
                            Passa para a próxima div.css-xz389d # Em outras palavras passar para o próximo card
                        } SENÃO {
                            # Se não EXISTI div.MuiTypography-root.MuiTypography-subtitle2.css-qpwa0j então provavelmente aqui tem só um PDF ou VÍDEO ou GIF
                            Passa para a próxima div.css-xz389d
                            numero_de_card_verificado += 1 # Para saber em qual card estamos e se já foi verificado
                        }
                    } SENÃO {
                        SE (dentro da :nth-match('div.css-xz389d, numero_de_card_verificado') EXISTI div.MuiTypography-root.MuiTypography-subtitle2.css-qpwa0j) {
                            # Se não tiver nenhum PDF, VÍDEO ou GIF vamos verificar se é um card só de texto
                            text_atual += 1 # Para saber em qual texto estamos
                            Pegue todo texto das tags P que estão contidas na :ntch-match('div.MuiTypography-root.MuiTypography-subtitle2.css-qpwa0j, text_atual')
                            Armazene todo esse conteúdo no JSON # Já, já vamos criar uma função JSON para armazenar as questões que estamos fazendo
                            numero_de_card_verificado += 1
                        } SENÃO {
                            # Se não é um card que contem TEXTO, PDF, VÍDEO ou GIF então só pode ser uma questão
                            SE (dentro da :nth:match('div.css-xz389d, numero_de_card_verificado') EXISTI div.css-nlzma4) {
                                # Se tiver essa div então sabemos que é uma questão então agora verificamos o tipo de questão (Radios, Checkbox, etc)
                                questao_atual += 1 # Adicionamos 1 a questao_atual para identificarmos em qual questão estamos
                                SE (dentro da :nth:match('div.MuiCard-root.css-1aksd3q, questao_atual') EXISTI span.MuiRadio-root.css-1sgsc5r) {
                                    # Se existir enão é uma questão de tipo Radios
                                    numero_de_card_verificado += 1
                                    Pega o conteúdo de todos os P dentro de todas as div.MuiBox-root.css-kmkory que estão dentro do pai que é :nth-match('div.MuiCard-root.css-1aksd3q, $') # Esse $ é a questao_atual
                                    Armazene todo esse conteúdo no JSON
                                    Vá para a página do ChatGPT (Abra uma nova guia, Entre em https://chatgpt.com/)
                                    Pega todo o conteúdo do JSON e coloca no ChatGPT
                                    Pega a resposta do ChatGPT que vai vim em formato JSON
                                    TODO Responder # Lógica para Responder
                                    numero_questao_respondido += 1
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
                                numero_de_card_verificado += 1
                            }
                        }
                        VERIFICAR LIÇÃO SE AS ALTERNATIVAS FOR APENAS IMAGENS
                            PEDIR AO USUÁRIO PARA QUERESOLVA ESSA QUESTÃO
                        PEGA O TÍTULO DA QUESTÃO E AS ALTERNATIVAS DEPOIS ARMARZENA-LÁS NO JSON
                        PEGA O JSON COM A PERGUNTA E AS ALTERNATIVAS DA $ E PASSE PARA ChatGPT PARA QUE RESOLVA E RETORNE A RESPOSTA(s)
                        PEGA AS RESPOSTAS DESSE JSON E COLOUQE NA ALTERNATIVA CORRETA
                    }
                } ENQUANTO (numero_de_card < numero_de_card_verificado)
                
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
