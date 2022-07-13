import os

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.base_page import BasePage


class HomePage(BasePage):
    def get_base_url(self) -> str:
        """Переменная базовый url"""
        return os.environ['BASE_URL']

    def open(self):
        """Открыть страницу"""
        self.driver.get(self.get_base_url())

    def get_search_field(self) -> WebElement:
        """Получаем элемент поля поиска"""
        search_field = self.driver.find_element(By.NAME, "search_query")
        return search_field

    def send_text_in_the_search_field(self, text) -> None:
        """Вводим символы в поле поиска"""
        self.get_search_field().send_keys(text)

    def get_search_button(self) -> WebElement:
        """Получаем элемент кнопки поиска"""
        search_button = WebDriverWait(self.driver, 5).until(ES.element_to_be_clickable((By.ID, "search-icon-legacy")))
        return search_button

    def click_search_button(self) -> None:
        self.get_search_button().click()
        WebDriverWait(self.driver, 5).until_not(ES.visibility_of_element_located((By.ID, "chips")))
