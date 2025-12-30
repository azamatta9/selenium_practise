from final_practise.pages.base_page import BasePage
from final_practise.config import (MY_EMAIL, MY_NAME, MY_LAST_NAME, MY_STATE, MY_PASSWORD,
                                   MY_CITY, MY_MOBILE_NUMBER, MY_ZIPCODE, MY_ADDRESS, ACC_CREATED_TEXT)

from selenium.webdriver.support.ui import Select


class SignupPage(BasePage):
    URL = 'https://automationexercise.com/login'
    NAME = ('xpath', '//input[@data-qa="signup-name"]')
    EMAIL = ('xpath', '//input[@data-qa="signup-email"]')
    SIGNUP_BUTTON = ('xpath', '//button[@data-qa="signup-button"]')
    CREATE_ACC_BUTTON = ('xpath', '//button[@data-qa="create-account"]')
    ACC_CREATED_LOC = ('xpath', '//h2[@data-qa="account-created"]')
    CONTINUE_BUTTON = ('xpath', '//a[text()="Continue"]')
    LOGOUT_BUTTON = ('xpath', '//a[text()=" Logout"]')

    TITLE = 'Automation Exercise - Signup'
    MR = ('xpath', '//label[@for="id_gender1"]')
    PASSWORD = ('id', 'password')
    DAY = ('id', 'days')
    MONTH = ('id', 'months')
    YEAR = ('id', 'years')
    FIRST_NAME = ('id', 'first_name')
    LAST_NAME = ('id', 'last_name')
    COUNTRY = ('id', 'country')
    STATE = ('id', 'state')
    CITY = ('id', 'city')
    ZIPCODE = ('id', 'zipcode')
    MOBILE_NUMBER = ('id', 'mobile_number')
    ADDRESS = ('id', 'address1')


    def open_page(self):
        self.open(self.URL)

    def sign_up(self):
        self.type(self.NAME, MY_NAME)
        self.type(self.EMAIL, MY_EMAIL)
        self.click(self.SIGNUP_BUTTON)
        self.wait_title(self.TITLE)

    def type_info(self):
        self.click(self.MR)
        self.type(self.PASSWORD, MY_PASSWORD)
        Select(self.find(self.DAY)).select_by_value('1')
        Select(self.find(self.MONTH)).select_by_value('1')
        Select(self.find(self.YEAR)).select_by_value('2000')
        self.type(self.FIRST_NAME, MY_NAME)
        self.type(self.LAST_NAME, MY_LAST_NAME)
        self.type(self.ADDRESS, MY_ADDRESS)
        Select(self.find(self.COUNTRY)).select_by_value('United States')
        self.type(self.STATE, MY_STATE)
        self.type(self.CITY, MY_CITY)
        self.type(self.ZIPCODE, MY_ZIPCODE)
        self.type(self.MOBILE_NUMBER, MY_MOBILE_NUMBER)
        self.click(self.CREATE_ACC_BUTTON)
        assert ACC_CREATED_TEXT in self.get_text(self.ACC_CREATED_LOC)

    def logout(self):
        self.click(self.CONTINUE_BUTTON)
        self.click(self.LOGOUT_BUTTON)

