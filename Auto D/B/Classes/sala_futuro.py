from playwright.sync_api import sync_playwright

class Speak():
    def __init__(self, user):
        self.page = 'https://saladofuturo.educacao.sp.gov.br/'
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

if __name__ == '__main__':
    Speak("teste")
