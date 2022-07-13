from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


from page_objects.base_page import BasePage


class SearchPage(BasePage):
    def get_base_url(self) -> str:
        """Переменная базовый url"""
        return self.driver.current_url

    def click_expected_video(self, expected_text) -> bool:
        """Кликаем видео"""
        counter: int = 0
        found: bool = False
        while not found and counter < 10:
            counter += 1
            search_results = self.driver.find_elements(By.XPATH,
                                                       '//a[@id="video-title"][@class="yt-simple-endpoint style-scope ytd-video-renderer"]')
            for search_result in search_results:
                found = search_result.text == expected_text
                if found:
                    action = ActionChains(self.driver)
                    action.scroll_to_element(search_result).perform()
                    search_result.click()
                    return True
                else:
                    action = ActionChains(self.driver)
                    action.scroll_to_element(search_results[-1]).perform()

        raise RuntimeError("Видео не найдено")




