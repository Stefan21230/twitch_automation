import logging
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def action_click(self, locator):
        element = self.wait_for_element_to_be_presence(locator)
        ActionChains(self.driver).move_to_element(element).click(element).perform()

    def click(self, locator, timeout=10):
        self.wait_for_element_to_be_clickable(locator, timeout).click()

    def click_javascript(self, locator):
        self.driver.execute_script("arguments[0].click", locator)

    def close_pop_up_window(self, locator, timeout=10):
        self.wait_for_element_to_be_presence(locator, timeout).send_keys(Keys.ESCAPE)

    def input(self, text: str, locator, timeout=10):
        self.wait_for_element_to_be_presence(locator, timeout).send_keys(text)

    def input_in_iframe_element(self, iframe_locator, locator, text):
        iframe = self.driver.find_element(By.XPATH, iframe_locator)
        self.driver.switch_to.frame(iframe)
        self.input(text, locator)
        self.driver.switch_to.default_content()

    @staticmethod
    def get_child_element(parent, search_child_element):
        """
        Go through the tree and searching for the first child in the DOM that matching search requirements.
        pass additonal value if you search for something specific, e.g. [@id='specific-id']
        if you search for e.g. span[@id='specific-id'], span[@class='some-class']
        :param parent: parent WebElement that we already found
        :param search_child_element: tag or tag with specific criteria that we are searching for.
        :return: child WebElement
        """
        try:
            search_element = parent.find_element(By.XPATH, f".//{search_child_element}")
            return search_element
        except Exception as e:
            logging.error(f"Exception {e} during get_child_element from {parent}")
            return None

    def get_visible_element_text(self, locator, timeout=10):
        """
        Method get WebElement text.
        """
        return self.wait_for_element_to_be_visible(locator, timeout).text

    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element_to_be_visible(locator, timeout)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def scroll_to_center_of_element(self, locator, timeout=10):
        element = self.wait_for_element_to_be_visible(locator, timeout)
        desired_y = (element.size['height'] / 2) + element.location['y']
        window_h = self.driver.execute_script('return window.innerHeight')
        window_y = self.driver.execute_script('return window.pageYOffset')
        current_y = (window_h / 2) + window_y
        scroll_y_by = desired_y - current_y

        self.driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)

    def wait_for_element_to_be_visible(self, locator, timeout=10):
        """
        Method check is WebElement visible.
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            logging.error(f"Exception during wait_for_element_to_be_visible {e}")
            raise Exception(f"Couldn't find element that has locator: {locator[1]},"
                            f" for time period of: {timeout} seconds.")

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        """
        Method check is WebElement clickable.
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except Exception as e:
            logging.error(f"Exception during wait_for_element_to_be_clickable {e}")
            raise Exception(f"Couldn't find element that has locator: {locator[1]},"
                            f" for time period of: {timeout} seconds.")

    def wait_for_elements_to_be_visible(self, locator, timeout=10):
        """
        Method check is WebElement visible.
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
        except Exception as e:
            logging.error(f"Exception during wait_for_elements_to_be_visible {e}")
            raise Exception(f"Couldn't find element that has locator: {locator[1]},"
                            f" for time period of: {timeout} seconds.")

    def wait_for_element_to_be_presence(self, locator, timeout=10):
        """
        Method check if WebElement  is present on the DOM
        of a page. This does not necessarily mean that the element is visible.
        locator - used to find the element returns the WebElement once it is located
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except Exception as e:
            logging.error(f"Exception during wait_for_element_to_be_presence {e}")
            raise Exception(f"Couldn't find element that has locator: {locator[1]},"
                            f" for time period of: {timeout} seconds.")