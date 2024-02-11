from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:
    """Проверка входа"""

    def test_enter_login_to_account(self, browser, registration):
        """вход по кнопке «Войти в аккаунт» на главной"""
        email, password = registration
        browser.find_element(*TestLocators.LOGO_LINK).click()
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/', f'{browser.current_url}'
        browser.find_element(*TestLocators.LOGIN_TO_ACCOUNT_LINK).click()
        WebDriverWait(browser, 3).until(expected_conditions.url_changes('https://stellarburgers.nomoreparties.site/'))
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/login', f'{browser.current_url}'
        browser.find_element(*TestLocators.ENTER_EMAIL).send_keys(email)
        browser.find_element(*TestLocators.ENTER_PASSWORD).send_keys(password)
        browser.find_element(*TestLocators.ENTER_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.url_changes('https://stellarburgers.nomoreparties.site/login'))
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/', f'{browser.current_url}'


    def test_enter_lk(self, browser, registration):
        """вход по кнопке «Личный кабинет» на главной"""
        email, password = registration
        browser.find_element(*TestLocators.LK_BUTTON).click()
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/login', f'{browser.current_url}'
        browser.find_element(*TestLocators.ENTER_EMAIL).send_keys(email)
        browser.find_element(*TestLocators.ENTER_PASSWORD).send_keys(password)
        browser.find_element(*TestLocators.ENTER_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.url_changes('https://stellarburgers.nomoreparties.site/login'))
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/', f'{browser.current_url}'


    def test_enter_form_registration(self, browser, registration):
        """вход через кнопку в форме регистрации"""
        email, password = registration
        browser.find_element(*TestLocators.REGISTRATION_LINK).click()
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/register', f'{browser.current_url}'
        browser.find_element(*TestLocators.ENTER_LINK).click()
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/login', f'{browser.current_url}'
        browser.find_element(*TestLocators.ENTER_EMAIL).send_keys(email)
        browser.find_element(*TestLocators.ENTER_PASSWORD).send_keys(password)
        browser.find_element(*TestLocators.ENTER_BUTTON).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.url_changes('https://stellarburgers.nomoreparties.site/login'))
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/', f'{browser.current_url}'


    def test_enter_password_recovery(self, browser, registration):
        """вход через кнопку в форме восстановления пароля"""
        email, password = registration
        browser.find_element(*TestLocators.FORGOT_PASSWORD_LINK).click()
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/forgot-password', f'{browser.current_url}'
        browser.find_element(*TestLocators.ENTER_LINK).click()
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/login', f'{browser.current_url}'
        browser.find_element(*TestLocators.ENTER_EMAIL).send_keys(email)
        browser.find_element(*TestLocators.ENTER_PASSWORD).send_keys(password)
        browser.find_element(*TestLocators.ENTER_BUTTON).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.url_changes('https://stellarburgers.nomoreparties.site/login'))
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/', f'{browser.current_url}'



