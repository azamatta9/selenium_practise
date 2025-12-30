from final_practise.pages.base_page import BasePage
from final_practise.config import MY_EMAIL
from final_practise.config import MY_PASSWORD


class LoginPage(BasePage):
    URL = 'https://automationexercise.com/login'
    EMAIL = ('xpath', '//input[@data-qa="login-email"]')
    PASSWORD = ('xpath', '//input[@data-qa="login-password"]')
    LOGIN_BUTTON = ('xpath', '//button[@data-qa="login-button"]')

    def open_page(self):
        self.open(self.URL)

    def login(self):
        self.type(self.EMAIL, MY_EMAIL)
        self.type(self.PASSWORD, MY_PASSWORD)
        self.click(self.LOGIN_BUTTON)
