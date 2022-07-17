import time
import unittest

from page_objects.home_page import HomePage
from page_objects.search_page import SearchPage
from page_objects.video_page import VideoPage
from webdriver_factory import WebDriverFactory


class SearchTest(unittest.TestCase):

    def setUp(self) -> None:
        """Действия до теста"""
        self.driver = WebDriverFactory.get_driver()
        self.home_page = HomePage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.video_page = VideoPage(self.driver)
        self.search_query = "selenium python"
        self.expected_title = "Selenium + Python = автоматизация тестирования веб-сайтов | Селениум + Питон"

    def tearDown(self) -> None:
        """Действия после теста"""
        # Выполняется после каждого теста!
        # Сохраняем скриншот с именем каждого теста
        self.driver.save_screenshot('test-reports/' + self.id() + '.png')
        self.driver.close()

    def test_1(self):
        """test"""
        self.home_page.open()
        self.home_page.send_text_in_the_search_field(self.search_query)
        self.home_page.click_search_button()
        self.assertTrue(self.search_page.click_expected_video(self.expected_title))
        self.assertEqual('Пауза (k)', self.video_page.get_condition_vidio())
        self.video_page.move_in_progress_bar(1/3)
        self.assertEqual('Пауза (k)', self.video_page.get_condition_vidio())
        self.video_page.move_in_progress_bar(4/5)
        self.assertEqual('Пауза (k)', self.video_page.get_condition_vidio())












        pass