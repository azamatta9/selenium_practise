import pytest
from final_practise.pages.login_page import LoginPage
from final_practise.pages.signup_page import SignupPage
from final_practise.pages.products_page import ProductsPage
from final_practise.pages.checkout_page import CheckoutPage

@pytest.mark.parametrize('cloth_name, quantity, text', [
    ('jeans', '2', 'Some text')
])

def test_e2e(driver, cloth_name, quantity, text):

    page = SignupPage(driver)
    page.open_page()
    page.sign_up()
    page.type_info()
    page.logout()

    login = LoginPage(driver)
    login.open_page()
    login.login()

    products = ProductsPage(driver)
    products.open_page()
    products.search_by_name(cloth_name)
    products.view_product()
    products.add_to_cart(quantity)
    products.delete_from_cart()

    checkout = CheckoutPage(driver)
    checkout.open_checkout()
    checkout.write_comment(text)
    checkout.place_order()
    checkout.make_payment()
