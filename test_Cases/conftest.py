from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# conftest.py
import os
import pytest
from datetime import datetime
from selenium import webdriver


@pytest.fixture(scope="function")
def setup(browser):
    options = Options()
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--remote-debugging-port=9222")
    service = Service(r'C:\Users\Karthik.Raj\Downloads\webdrivers\chromedriver.exe')
    driver = webdriver.Edge()
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    if  browser == "edge":
        driver = webdriver.Edge()
        print("Launching Edge Browser")

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def save_screenshots(driver,file_name):
    screenshot_folder = "screenshots"
    if not os.path.exists(screenshot_folder):
        os.makedirs(screenshot_folder)  # Create folder if it doesn't exist

    # Screenshot file path
    screenshot_file = os.path.join(screenshot_folder, file_name)

    # Take and save the screenshot
    driver.save_screenshot(screenshot_file)

    print(f"Screenshot saved at: {screenshot_file}")

    # Quit WebDriver
    #driver.quit()

