import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

from page_objects.base_page import BasePage


class VideoPage(BasePage):
    def get_button_run_video(self) -> WebElement:
        button_run = WebDriverWait(self.driver, 5).until(
            ES.visibility_of_element_located((By.CLASS_NAME, 'ytp-play-button')))
        return button_run

    def get_condition_vidio(self) -> str:
        return self.get_button_run_video().get_attribute('title')

    def get_progress_container(self) -> WebElement:
        return self.driver.find_elements(By.CLASS_NAME, "ytp-chrome-bottom")[0]

    def get_progress_bar(self):
        progress_bar = self.get_progress_container().find_elements(By.CLASS_NAME, 'ytp-progress-bar')[0]
        return progress_bar

    def get_attribute_video_size(self) -> int:
        self.get_progress_bar().get_attribute('aria-valuemax')
        return int(self.get_progress_bar().get_attribute('aria-valuemax'))

    def get_aria_valuenow(self):
        return int(self.get_progress_bar().get_attribute('aria-valuenow'))


    def get_width_container(self):
        return int(self.get_progress_container().value_of_css_property('width')[:-2])

    def get_pointer(self):
        return self.driver.find_elements(By.CLASS_NAME, 'ytp-swatch-background-color')

    def move_to_progress_bar(self) -> None:
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(self.get_progress_bar(), 0, 0)
        time.sleep(3)
        action.move_by_offset(255, 0)
        action.click()
        action.perform()
