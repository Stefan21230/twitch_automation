import pytest
import logging
import os
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

base_dir = os.path.dirname(__file__)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    logging_path = os.path.join(base_dir, 'twitch_automation.log')
    screenshots_dir = os.path.join(base_dir, "screenshots")     # create path screenshot dir
    remove_and_create_directory([screenshots_dir])              # remove existing and create new screenshot dir
    config.screenshots_dir = screenshots_dir
    logging.basicConfig(filename=logging_path, filemode='w+',
                        format='%(levelname)s %(asctime)s %(message)s (%(filename)s:%(lineno)s)',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.DEBUG)


@pytest.fixture(scope="function")
def setup(request, pytestconfig, open_page="https://m.twitch.tv/"):
    opt_chrome = webdriver.ChromeOptions()
    opt_chrome.add_argument("--start-maximized")
    opt_chrome.add_argument("--no-sandbox")
    opt_chrome.add_argument("--disable-popup-blocking")

    # Mobile emulator
    mobile_emulation = {"deviceName": "Nexus 5"}
    opt_chrome.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=opt_chrome)
    driver.get(open_page)
    screenshots_dir = getattr(pytestconfig, "screenshots_dir", None)

    request.cls.driver = driver  # set driver as class attribute
    request.cls.screenshots = screenshots_dir
    yield
    driver.close()
    driver.quit()


def remove_and_create_directory(dir_paths):
    for dir_path in dir_paths:
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
        os.makedirs(dir_path)