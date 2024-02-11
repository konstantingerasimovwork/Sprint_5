from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructor:
    """Проверка раздела 'Конструктор'"""

    def test_select_buns_from_sauces(self, browser):
        """Переход к разделу Булки из раздела Соусы"""
        browser.get('https://stellarburgers.nomoreparties.site')
        browser.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/', f'{browser.current_url}'
        browser.find_element(*TestLocators.SAUCES_TAB).click()
        WebDriverWait(browser, 9)
        attribute = browser.find_element(*TestLocators.SAUCES_CLASS).get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in attribute
        browser.find_element(*TestLocators.BUNS_TAB).click()
        WebDriverWait(browser, 9)
        attribute = browser.find_element(*TestLocators.BUNS_CLASS).get_attribute(
            'class')
        assert 'tab_tab_type_current__2BEPc' in attribute


    def test_select_buns_from_filling(self, browser):
        """Переход к разделу Булки из раздела Начинки"""
        browser.get('https://stellarburgers.nomoreparties.site')
        browser.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/', f'{browser.current_url}'
        browser.find_element(*TestLocators.FILLINGS_TAB).click()
        WebDriverWait(browser, 9)
        attribute = browser.find_element(*TestLocators.FILLINGS_CLASS).get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in attribute
        browser.find_element(*TestLocators.BUNS_TAB).click()
        WebDriverWait(browser, 9)
        attribute = browser.find_element(*TestLocators.BUNS_CLASS).get_attribute(
            'class')
        assert 'tab_tab_type_current__2BEPc' in attribute


    def test_select_sauces_from_buns(self, browser):
        """Переход к разделу Соусы из раздела Булки"""
        browser.get('https://stellarburgers.nomoreparties.site')
        browser.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/', f'{browser.current_url}'
        attribute = browser.find_element(*TestLocators.BUNS_CLASS).get_attribute(
            'class')
        assert 'tab_tab_type_current__2BEPc' in attribute
        browser.find_element(*TestLocators.SAUCES_TAB).click()
        WebDriverWait(browser, 9)
        attribute = browser.find_element(*TestLocators.SAUCES_CLASS).get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in attribute


    def test_select_sauces_from_filling(self, browser):
        """Переход к разделу Соусы из раздела Начинки"""
        browser.get('https://stellarburgers.nomoreparties.site')
        browser.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/', f'{browser.current_url}'
        browser.find_element(*TestLocators.FILLINGS_TAB).click()
        WebDriverWait(browser, 9)
        attribute = browser.find_element(*TestLocators.FILLINGS_CLASS).get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in attribute
        browser.find_element(*TestLocators.SAUCES_TAB).click()
        WebDriverWait(browser, 9)
        attribute = browser.find_element(*TestLocators.SAUCES_CLASS).get_attribute(
            'class')
        assert 'tab_tab_type_current__2BEPc' in attribute


    def test_select_filling_from_buns(self, browser):
        """Переход к разделу Начинки из раздела Булки"""
        browser.get('https://stellarburgers.nomoreparties.site')
        browser.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/', f'{browser.current_url}'
        attribute = browser.find_element(*TestLocators.BUNS_CLASS).get_attribute(
            'class')
        assert 'tab_tab_type_current__2BEPc' in attribute
        browser.find_element(*TestLocators.FILLINGS_TAB).click()
        WebDriverWait(browser, 9)
        attribute = browser.find_element(*TestLocators.FILLINGS_CLASS).get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in attribute


    def test_select_filling_from_sauces(self, browser):
        """Переход к разделу Начинки из раздела Соусы"""
        browser.get('https://stellarburgers.nomoreparties.site')
        browser.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/', f'{browser.current_url}'
        browser.find_element(*TestLocators.SAUCES_TAB).click()
        WebDriverWait(browser, 9)
        attribute = browser.find_element(*TestLocators.SAUCES_CLASS).get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in attribute
        browser.find_element(*TestLocators.FILLINGS_TAB).click()
        WebDriverWait(browser, 9)
        attribute = browser.find_element(*TestLocators.FILLINGS_CLASS).get_attribute(
            'class')
        assert 'tab_tab_type_current__2BEPc' in attribute
