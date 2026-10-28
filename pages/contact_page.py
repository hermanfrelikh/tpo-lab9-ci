from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class ContactPage(BasePage):
    """Страница с формой обратной связи"""

    PATH = "/contact"

    # локаторы
    NAME = (By.ID, "name")
    EMAIL = (By.ID, "email")
    PHONE = (By.ID, "phone")
    TOPIC = (By.ID, "topic")
    MESSAGE = (By.ID, "message")
    SUBMIT = (By.ID, "submit-button")
    SUCCESS = (By.ID, "success")

    def open_page(self):
        self.open(self.PATH)
        return self

    def fill_form(self, name="", email="", phone="", topic="Вопрос", message=""):
        self.type(self.NAME, name)
        self.type(self.EMAIL, email)
        self.type(self.PHONE, phone)
        Select(self.find(self.TOPIC)).select_by_visible_text(topic)
        self.type(self.MESSAGE, message)

    def submit(self):
        self.click(self.SUBMIT)

    def get_success_message(self):
        return self.get_text(self.SUCCESS)

    def get_error(self, field):
        # у каждого поля своя ошибка: name-error, email-error и т.д.
        return self.get_text((By.ID, f"{field}-error"))

    def has_error(self, field):
        return self.is_present((By.ID, f"{field}-error"))
