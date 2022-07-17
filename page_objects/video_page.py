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

    def get_bar_in_px(self) -> WebElement:
        bar_with_width_in_px = self.driver.find_element(By.CLASS_NAME, "ytp-chrome-bottom")
        return bar_with_width_in_px

    def get_progress_bar(self) -> WebElement:
        progress_bar = self.driver.find_element(By.CLASS_NAME, "ytp-scrubber-container")
        return progress_bar

    def get_position_now(self) -> float:
        get_attribute = self.get_progress_bar().get_attribute("style")
        get_attribute_width_in_px = get_attribute.split('(')[1]
        position_now = round(float(get_attribute_width_in_px.replace("px);", "")), 2)
        return position_now

    def get_width_video(self) -> float:
        get_attribute = self.get_bar_in_px().get_attribute("style")
        get_attribute_width_in_px = get_attribute.split()[1]
        dx_video = round(float(get_attribute_width_in_px.replace("px;", "")), 2)
        return dx_video

    def move_in_progress_bar(self, value) -> None:
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(self.get_progress_bar(), 0, 0)
        # action.pause(3)
        dx = round(self.get_width_video() * value - self.get_position_now())
        #print(
         #   f'Длительность видео всего {self.get_attribute_video_size_in_sec()} до перемотки {self.get_aria_valuenow_in_sec()}')
        action.move_by_offset(dx, 0)
        action.click()
        action.perform()
        #print(f'После перемотки {self.get_aria_valuenow_in_sec()}')
#Методы для проверки длительности видео в секундах
'''    def get_progress_bar_in_sec(self):
        progress_bar = self.get_bar_in_px().find_elements(By.CLASS_NAME, 'ytp-progress-bar')[0]
        return progress_bar

    def get_attribute_video_size_in_sec(self) -> int:
        max_time_video = int(self.get_progress_bar_in_sec().get_attribute('aria-valuemax'))
        return max_time_video

    def get_aria_valuenow_in_sec(self):
        time_now = int(self.get_progress_bar_in_sec().get_attribute('aria-valuenow'))
        return time_now'''
