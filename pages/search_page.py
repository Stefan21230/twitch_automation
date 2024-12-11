import os
import logging
from pages.base_page import BasePage
from locators import search_page_locators as search_page
from locators import streamer_page_locators as streamer_page


class SearchPage(BasePage):
    def choose_streamer_and_take_screenshot(self, screenshots_dir):
        logging.debug(f"Choose streamer and take a screenshot what will be saved in {screenshots_dir}")
        menu_list = self.wait_for_element_to_be_visible(search_page.menu_list)
        channels = self.get_child_element(menu_list, search_page.channels_btn)
        channels.click()
        self.wait_for_element_to_be_visible(search_page.list_of_channels)
        self.scroll_to_center_of_element(search_page.streamer_btn)
        streamer_btn = self.wait_for_element_to_be_visible(search_page.streamer_btn)
        streamer_btn.click()
        current_url = self.driver.current_url.split("https://m.twitch.tv/")
        screenshot_name = "".join(current_url)
        screenshots_path = os.path.join(screenshots_dir, f"{screenshot_name}.png")
        self.wait_for_elements_to_be_visible(streamer_page.a_videos)
        self.driver.save_screenshot(screenshots_path)
