from pages.base_page import BasePage
from locators import home_page_locators as home_page
from selenium.webdriver.common.keys import Keys
import logging


class HomePage(BasePage):
    def click_on_search_and_input(self, text):
        logging.debug(f"Click on the search button and input text {text}")
        self.scroll_to_element(home_page.browse_btn)
        self.click(home_page.browse_btn)
        self.scroll_to_element(home_page.search_input_field)
        self.input(text, home_page.search_input_field)
        self.input(Keys.ENTER, home_page.search_input_field)
