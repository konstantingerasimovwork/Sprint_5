from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestPersonalAccount:
    """Проверка личного кабинета """

    def test_click_lk_button(self, browser, login_account):
        """Переход в личный кабинет """
        browser.find_element(*TestLocators.LK_BUTTON).click()
        WebDriverWait(browser, 15).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/account/profile', f'{browser.current_url}'


    def test_following_button_contructor(self, browser, login_account):
        """Переход из личного кабинета в конструктор по кнопке конструктор"""
        browser.find_element(*TestLocators.LK_BUTTON).click()
        WebDriverWait(browser, 15).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/account/profile', f'{browser.current_url}'
        browser.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.url_changes('https://stellarburgers.nomoreparties.site/account/profile'))
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/', f'{browser.current_url}'


    def test_following_logo(self, browser, login_account):
        """Переход из личного кабинета в конструктор по логотипу Stellar Burgers"""
        browser.find_element(*TestLocators.LK_BUTTON).click()
        WebDriverWait(browser, 15).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/account/profile', f'{browser.current_url}'
        browser.find_element(*TestLocators.LOGO_LINK).click()
        WebDriverWait(browser, 3).until(expected_conditions.url_changes('https://stellarburgers.nomoreparties.site/account/profile'))
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/', f'{browser.current_url}'


    def test_following_exit_button(self, browser, login_account):
        """Переход из личного кабинета в конструктор по логотипу Stellar Burgers"""
        browser.find_element(*TestLocators.LK_BUTTON).click()
        WebDriverWait(browser, 15).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/account/profile', f'{browser.current_url}'
        browser.find_element(*TestLocators.EXIT_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.url_changes('https://stellarburgers.nomoreparties.site/account/profile'))
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/login', f'{browser.current_url}'







