from playwright.sync_api import sync_playwright

class Me_Salva():
    def __init__(self, user):
        self.page = 'https://www.mesalva.com/app/entrar'
        self.user = user
        self.engine(self.user, self.page)

    def engine(self, user, page):
        try:
            with sync_playwright() as program:
                browser = program.chromium.launch(headless=False, slow_mo=500)
                page = browser.new_page()
                page.goto(self.page)
        except Exception as e:
            print(f'ERRO NO ENGINE: {e}')

    def acessar_cmsp(self):
        try:
            button = 'img[src="https://s3.sa-east-1.amazonaws.com/edusp-static.ip.tv/room/cards/edusp/elianemararod3272389-sp/e6TVO7cyptJu5lb6wSUTwyYUtlgVd5.png"]'
            button.highlight()
            button.click()
        except Exception as e:
            print(f'ERRO AO ACESSAR O COM O CMSP: {e}')

if __name__ == '__main__':
    Me_Salva("teste")