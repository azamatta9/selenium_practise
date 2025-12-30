from final_practise.pages.base_page import BasePage
from final_practise.config import (MY_NAME, MY_LAST_NAME, CARD_NUMBER, CVC_NUMBER,
                                   EXPIRATION_MONTH, EXPIRATION_YEAR, CONFIRMATION_TEXT)


class CheckoutPage(BasePage):

    CHECKOUT = ('xpath', '//a[text()="Proceed To Checkout"]')
    COMMENT = ('xpath', '//textarea[@name="message"]')
    ORDER = ('xpath', '//a[text()="Place Order"]')
    NAME_ON_CARD = ('xpath', '//input[@name="name_on_card"]')
    CARD_NUMBER_LOC = ('xpath', '//input[@name="card_number"]')
    CVC = ('xpath', '//input[@name="cvc"]')
    EXPIRY_MONTH = ('xpath', '//input[@name="expiry_month"]')
    EXPIRY_YEAR = ('xpath', '//input[@name="expiry_year"]')
    CONFIRM_ORDER = ('id', 'submit')
    ORDER_PLACED = ('xpath', '//h2[@data-qa="order-placed"]')



    def open_checkout(self):
        self.click(self.CHECKOUT)

    def write_comment(self, text):
        self.type(self.COMMENT, text)

    def place_order(self):
        self.click(self.ORDER)

    def make_payment(self):
        self.type(self.NAME_ON_CARD, f"{MY_NAME}{MY_LAST_NAME}")
        self.type(self.CARD_NUMBER_LOC, CARD_NUMBER)
        self.type(self.CVC, CVC_NUMBER)
        self.type(self.EXPIRY_MONTH, EXPIRATION_MONTH)
        self.type(self.EXPIRY_YEAR, EXPIRATION_YEAR)
        self.click(self.CONFIRM_ORDER)
        assert CONFIRMATION_TEXT == self.get_text(self.ORDER_PLACED)
