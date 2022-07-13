from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    """Базовый (родительский) класс PageObject,
        который содержит общие для всех страниц методы."""

    def __init__(self, driver: WebDriver):
        """Конструктор класса"""
        self.driver = driver


