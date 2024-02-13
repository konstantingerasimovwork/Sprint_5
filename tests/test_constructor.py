from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


class TestConstructor:
    """Проверка раздела 'Конструктор'"""

    def test_select_buns_from_sauces(self, browser):
        """Переход к разделу Булки из раздела Соусы"""
        browser.get('https://stellarburgers.nomoreparties.site')
        browser.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        browser.find_element(*TestLocators.SAUCES_TAB).click()
        WebDriverWait(browser, 9).until(expected_conditions.text_to_be_present_in_element_attribute(TestLocators.SAUCES_CLASS,
                                                                                                    'class',
                                                                                                    'tab_tab_type_current__2BEPc'))
        browser.find_element(*TestLocators.BUNS_TAB).click()
        WebDriverWait(browser, 9).until(expected_conditions.text_to_be_present_in_element_attribute(TestLocators.BUNS_CLASS,
                                                                                                    'class',
                                                                                                    'tab_tab_type_current__2BEPc'))

    def test_select_buns_from_filling(self, browser):
        """Переход к разделу Булки из раздела Начинки"""
        browser.get('https://stellarburgers.nomoreparties.site')
        browser.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        browser.find_element(*TestLocators.FILLINGS_TAB).click()
        WebDriverWait(browser, 9).until(expected_conditions.text_to_be_present_in_element_attribute(TestLocators.FILLINGS_CLASS,
                                                                                                    'class',
                                                                                                    'tab_tab_type_current__2BEPc'))
        browser.find_element(*TestLocators.BUNS_TAB).click()
        WebDriverWait(browser, 9).until(expected_conditions.text_to_be_present_in_element_attribute(TestLocators.BUNS_CLASS,
                                                                                                    'class',
                                                                                                    'tab_tab_type_current__2BEPc'))


    def test_select_sauces_from_buns(self, browser):
        """Переход к разделу Соусы из раздела Булки"""
        browser.get('https://stellarburgers.nomoreparties.site')
        browser.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(browser, 9).until(expected_conditions.text_to_be_present_in_element_attribute(TestLocators.BUNS_CLASS,
                                                                        'class',
                                                                        'tab_tab_type_current__2BEPc'))
        browser.find_element(*TestLocators.SAUCES_TAB).click()
        WebDriverWait(browser, 9).until(expected_conditions.text_to_be_present_in_element_attribute(TestLocators.SAUCES_CLASS,
                                                                        'class',
                                                                        'tab_tab_type_current__2BEPc'))


    def test_select_sauces_from_filling(self, browser):
        """Переход к разделу Соусы из раздела Начинки"""
        browser.get('https://stellarburgers.nomoreparties.site')
        browser.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        browser.find_element(*TestLocators.FILLINGS_TAB).click()
        WebDriverWait(browser, 9).until(expected_conditions.text_to_be_present_in_element_attribute(TestLocators.FILLINGS_CLASS,
                                                                        'class',
                                                                        'tab_tab_type_current__2BEPc'))
        browser.find_element(*TestLocators.SAUCES_TAB).click()
        WebDriverWait(browser, 9).until(expected_conditions.text_to_be_present_in_element_attribute(TestLocators.SAUCES_CLASS,
                                                                        'class',
                                                                        'tab_tab_type_current__2BEPc'))


    def test_select_filling_from_buns(self, browser):
        """Переход к разделу Начинки из раздела Булки"""
        browser.get('https://stellarburgers.nomoreparties.site')
        browser.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(browser, 9).until(expected_conditions.text_to_be_present_in_element_attribute(TestLocators.BUNS_CLASS,
                                                                        'class',
                                                                        'tab_tab_type_current__2BEPc'))
        browser.find_element(*TestLocators.FILLINGS_TAB).click()
        WebDriverWait(browser, 9).until(expected_conditions.text_to_be_present_in_element_attribute(TestLocators.FILLINGS_CLASS,
                                                                        'class',
                                                                        'tab_tab_type_current__2BEPc'))


    def test_select_filling_from_sauces(self, browser):
        """Переход к разделу Начинки из раздела Соусы"""
        browser.get('https://stellarburgers.nomoreparties.site')
        browser.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        browser.find_element(*TestLocators.SAUCES_TAB).click()
        WebDriverWait(browser, 9).until(expected_conditions.text_to_be_present_in_element_attribute(TestLocators.SAUCES_CLASS,
                                                                        'class',
                                                                        'tab_tab_type_current__2BEPc'))
        browser.find_element(*TestLocators.FILLINGS_TAB).click()
        WebDriverWait(browser, 9).until(expected_conditions.text_to_be_present_in_element_attribute(TestLocators.FILLINGS_CLASS,
                                                                        'class',
                                                                        'tab_tab_type_current__2BEPc'))

