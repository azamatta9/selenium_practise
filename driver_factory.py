from selenium import webdriver
from final_practise.config import BROWSER

def create_driver():
    if BROWSER == 'chrome':
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
        return driver
    raise ValueError(f'Браузер {BROWSER} не настроен')
