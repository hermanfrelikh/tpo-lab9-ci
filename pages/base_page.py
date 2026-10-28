from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Общие действия для всех страниц: открыть, найти, ввести, кликнуть"""

    BASE_URL = "http://127.0.0.1:8000"

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, path):
        self.driver.get(self.BASE_URL + path)

    def find(self, locator):
        # ждём, пока элемент станет видимым
        return self.wait.until(EC.visibility_of_element_located(locator))

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_text(self, locator):
        return self.find(locator).text

    def is_present(self, locator):
        return len(self.driver.find_elements(*locator)) > 0
