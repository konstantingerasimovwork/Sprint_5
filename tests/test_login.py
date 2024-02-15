from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import user_test_data


class TestLogin:
    """Проверка входа"""

    def test_enter_login_to_account(self, browser):
        """вход по кнопке «Войти в аккаунт» на главной"""
        user_data = user_test_data()
        browser.get('https://stellarburgers.nomoreparties.site/')
        browser.find_element(*TestLocators.LOGIN_TO_ACCOUNT_LINK).click()
        WebDriverWait(browser, 3).until(expected_conditions.url_changes('https://stellarburgers.nomoreparties.site/'))
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/login', f'{browser.current_url}'
        browser.find_element(*TestLocators.ENTER_EMAIL).send_keys(user_data['email'])
        browser.find_element(*TestLocators.ENTER_PASSWORD).send_keys(user_data['pass'])
        browser.find_element(*TestLocators.ENTER_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.url_changes('https://stellarburgers.nomoreparties.site/login'))
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/', f'{browser.current_url}'


    def test_enter_lk(self, browser):
        """вход по кнопке «Личный кабинет» на главной"""
        user_data = user_test_data()
        browser.get('https://stellarburgers.nomoreparties.site/')
        browser.find_element(*TestLocators.LK_BUTTON).click()
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/login', f'{browser.current_url}'
        browser.find_element(*TestLocators.ENTER_EMAIL).send_keys(user_data['email'])
        browser.find_element(*TestLocators.ENTER_PASSWORD).send_keys(user_data['pass'])
        browser.find_element(*TestLocators.ENTER_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.url_changes('https://stellarburgers.nomoreparties.site/login'))
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/', f'{browser.current_url}'


    def test_enter_form_registration(self, browser):
        """вход через кнопку в форме регистрации"""
        user_data = user_test_data()
        browser.get('https://stellarburgers.nomoreparties.site/register')
        browser.find_element(*TestLocators.ENTER_LINK).click()
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/login', f'{browser.current_url}'
        browser.find_element(*TestLocators.ENTER_EMAIL).send_keys(user_data['email'])
        browser.find_element(*TestLocators.ENTER_PASSWORD).send_keys(user_data['pass'])
        browser.find_element(*TestLocators.ENTER_BUTTON).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.url_changes('https://stellarburgers.nomoreparties.site/login'))
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/', f'{browser.current_url}'


    def test_enter_password_recovery(self, browser):
        """вход через кнопку в форме восстановления пароля"""
        user_data = user_test_data()
        browser.get('https://stellarburgers.nomoreparties.site/forgot-password')
        browser.find_element(*TestLocators.ENTER_LINK).click()
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/login', f'{browser.current_url}'
        browser.find_element(*TestLocators.ENTER_EMAIL).send_keys(user_data['email'])
        browser.find_element(*TestLocators.ENTER_PASSWORD).send_keys(user_data['pass'])
        browser.find_element(*TestLocators.ENTER_BUTTON).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.url_changes('https://stellarburgers.nomoreparties.site/login'))
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/', f'{browser.current_url}'



