from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import generate_user_login_data


class TestRegistration:
    """Проверка регистрации"""
    
    def test_correct_registration(self, browser):
        """Успешная регистрация"""
        browser.get('https://stellarburgers.nomoreparties.site/register')
        user_data = generate_user_login_data()
        browser.find_element(*TestLocators.REGISTRATION_NAME).send_keys(user_data['name'])
        browser.find_element(*TestLocators.REGISTRATION_EMAIL).send_keys(user_data['email'])
        browser.find_element(*TestLocators.REGISTRATION_PASSWORD).send_keys(user_data['pass'])
        browser.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(browser, 9).until(expected_conditions.visibility_of_element_located((TestLocators.ENTER_HEADER)))
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/login', f'{browser.current_url}'


    def test_incorrect_registration_password_less_6_characters(self, browser):
        """Неуспешная регистрация - пароль меньше 6 символов"""
        browser.get('https://stellarburgers.nomoreparties.site/register')
        user_data = generate_user_login_data()
        browser.find_element(*TestLocators.REGISTRATION_NAME).send_keys(user_data['name'])
        browser.find_element(*TestLocators.REGISTRATION_EMAIL).send_keys(user_data['email'])
        browser.find_element(*TestLocators.REGISTRATION_PASSWORD).send_keys('12345')
        browser.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        incorrect_password = WebDriverWait(browser, 9).until(expected_conditions.visibility_of_element_located((TestLocators.INCORRECT_PASSWORD_MESSAGE))).text
        assert incorrect_password == 'Некорректный пароль', f'{incorrect_password}'

