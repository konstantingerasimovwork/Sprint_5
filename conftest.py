import pytest
from locators import TestLocators
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from data import user_test_data

@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def login_account(browser):
    user_data = user_test_data()
    browser.get('https://stellarburgers.nomoreparties.site/')
    browser.find_element(*TestLocators.LK_BUTTON).click()
    browser.find_element(*TestLocators.ENTER_EMAIL).send_keys(user_data['email'])
    browser.find_element(*TestLocators.ENTER_PASSWORD).send_keys(user_data['pass'])
    browser.find_element(*TestLocators.ENTER_BUTTON).click()
    WebDriverWait(browser, 3).until(expected_conditions.url_changes('https://stellarburgers.nomoreparties.site/login'))
