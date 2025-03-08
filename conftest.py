import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach

@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }


    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)


    browser.quit()
'''
    options = Options()
    selenoid_capabilities = {
        "browserName": "opera",
        #"browserVersion": "100.0",
        "browserVersion": "106.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser = Browser(Config(driver))
    yield browser

    browser.quit()
'''