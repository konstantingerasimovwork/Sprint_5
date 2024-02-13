import pytest
from data import generate_user_login_data
from locators import TestLocators
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def browser():
    options = Options()
    # service =
    # service = Service(executable_path='/chromedriver')
    options.add_argument('--window-size=1920,1080')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def login_account(browser):
    browser.get('https://stellarburgers.nomoreparties.site/')
    browser.find_element(*TestLocators.LK_BUTTON).click()
    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/login', f'{browser.current_url}'
    browser.find_element(*TestLocators.ENTER_EMAIL).send_keys('konstantin_gerasimov_5@yandex.ru')
    browser.find_element(*TestLocators.ENTER_PASSWORD).send_keys('123456')
    browser.find_element(*TestLocators.ENTER_BUTTON).click()
    WebDriverWait(browser, 3).until(expected_conditions.url_changes('https://stellarburgers.nomoreparties.site/login'))
    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/', f'{browser.current_url}'
