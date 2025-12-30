from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, 1)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", el)
        try:
            el.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", el)

    def type(self, locator, text):
        el = self.find(locator)
        el.clear()
        el.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def wait_title(self, title):
        return self.wait.until(EC.title_contains(title))


