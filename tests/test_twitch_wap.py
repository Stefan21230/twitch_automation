import pytest
from pages.home_page import HomePage
from pages.search_page import SearchPage
from selenium.webdriver.chrome.webdriver import WebDriver
from typing import Optional


@pytest.mark.usefixtures("setup")
class TestTwitchWap:
    driver: WebDriver
    screenshots: Optional[str]

    def test_twitch_wap(self):
        self.home_page = HomePage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.home_page.click_on_search_and_input(text="StarCraft II")
        self.search_page.choose_streamer_and_take_screenshot(self.screenshots)