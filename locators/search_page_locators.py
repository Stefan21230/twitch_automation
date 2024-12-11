from selenium.webdriver.common.by import By

menu_list = (By.CSS_SELECTOR, "ul[role='tablist']")
channels_btn = "a[contains(@href, 'type=channels')]"

list_of_channels = (By.CSS_SELECTOR, "div[role='list']")
streamer_btn = (By.XPATH, "//a[contains(@class, 'ScCoreLink')]")