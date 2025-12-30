from final_practise.pages.base_page import BasePage


class ProductsPage(BasePage):

    URL = 'https://automationexercise.com/products'
    SEARCH_PRODUCT = ('id', 'search_product')
    SUBMIT_SEARCH_BUTTON = ('id', 'submit_search')
    PRODUCTS_LOC = ('xpath', '//div[@class="features_items"]')
    VIEW_PRODUCT = ('xpath', '//a[text()="View Product"]')
    QUANTITY = ('id', 'quantity')
    ADD_TO_CART = ('xpath', '//button[contains(., "Add to cart")]')
    CONTINUE_SHOPPING = ('xpath', '//button[text()="Continue Shopping"]' )
    CART = ('xpath', '//a[text()=" Cart"]')
    DELETE_PRODUCT = ('xpath', '//a[@class="cart_quantity_delete"]')

    def open_page(self):
        self.open(self.URL)
        if "products" not in self.driver.current_url:
            self.driver.execute_script(f"window.location.href='{self.URL}';")

    def search_by_name(self, name):
        self.type(self.SEARCH_PRODUCT, name)
        self.click(self.SUBMIT_SEARCH_BUTTON)

    def view_product(self):
        els = self.find_all(self.VIEW_PRODUCT)
        self.click(els[1])

    def add_to_cart(self, quantity):
        self.type(self.QUANTITY, quantity)
        self.click(self.ADD_TO_CART)
        self.click(self.CONTINUE_SHOPPING)

    def delete_from_cart(self):
        self.click(self.CART)
        self.click(self.DELETE_PRODUCT)
