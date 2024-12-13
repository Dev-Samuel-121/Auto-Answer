from playwright.sync_api import sync_playwright

class Speak():
    def __init__(self, user):
        self.page = ''
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
            button = 'img[src="https://s3.sa-east-1.amazonaws.com/edusp-static.ip.tv/room/cards/edusp/julianasanche3225895-sp/OssSPvVLLQCMBVxQ2ERP3Q36wgHq8W.png"]'
            button.highlight()
            button.click()
        except Exception as e:
            print(f'ERRO AO ACESSAR O COM O CMSP: {e}')

if __name__ == '__main__':
    Speak("teste")