from pages.base_page import BasePage
from locators import home_page_locators as home_page
from selenium.webdriver.common.keys import Keys
import logging


class HomePage(BasePage):
    def click_on_search_and_input(self, text):
        """
        Perform a search action by clicking the search button and entering the provided text.
        This method scrolls to the search button, clicks it, scrolls to the search input field,
        and inputs the text followed by pressing the ENTER key to submit the search.

        :param text: Text to be entered into the search input field.
        :return: None
        """
        logging.debug(f"Click on the search button and input text {text}")
        self.scroll_to_element(home_page.browse_btn)
        self.click(home_page.browse_btn)
        self.scroll_to_element(home_page.search_input_field)
        self.input(text, home_page.search_input_field)
        self.input(Keys.ENTER, home_page.search_input_field)
