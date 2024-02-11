from selenium.webdriver.common.by import By


class TestLocators:
    REGISTRATION_NAME = By.XPATH, './/*[@id="root"]//fieldset[1]//input[@type="text"]' # Поле Имя на странице регистрации
    REGISTRATION_EMAIL = By.XPATH, './/*[@id="root"]//fieldset[2]//input[@type="text"]' # Поле Email на странице регистрации
    REGISTRATION_PASSWORD = By.XPATH, './/*[@id="root"]//fieldset[3]//input[@type="password"]' # Поле Пароль на странице регистрации
    REGISTRATION_BUTTON = By.XPATH, './/*[@id="root"]//form/button' # Кнопка Зарегистрироваться на странице регистрации
    ENTER_EMAIL = By.XPATH, '//*[@id="root"]//fieldset[1]//input[@type="text"]' # Поля Email на странице входа
    ENTER_PASSWORD = By.XPATH, '//*[@id="root"]//fieldset[2]//input[@type="password"]' # Поля Пароль на странице входа
    ENTER_BUTTON = By.XPATH, '//*[@id="root"]//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]' #Кнопка Войти на странице входа
    ENTER_LINK = By.XPATH, '//*[@id="root"]//a[@href="/login"]'
    ENTER_HEADER = By.XPATH, './/*[@id="root"]//h2[text()="Вход"]' #Заголовок Вход на странице входа
    INCORRECT_PASSWORD_MESSAGE = By.XPATH, './/*[@id="root"]//fieldset[3]//p[@class="input__error text_type_main-default"]' #Сообщение Некорректный пароль при вводе невалидного пароля
    LOGIN_TO_ACCOUNT_LINK = By.XPATH, './/div[@id="root"]//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]' #Кнопка "Войти в аккаунт"
    LOGO_LINK = By.XPATH, '//*[@id="root"]//div[@class="AppHeader_header__logo__2D0X2"]/a[@href="/"]' #Ссылка логотипа Stellar Burgers
    LK_BUTTON = By.LINK_TEXT, "Личный Кабинет" # Кнопка "Личный Кабинет"
    REGISTRATION_LINK = By.LINK_TEXT, "Зарегистрироваться" # Ссылка Зарегистрироваться
    FORGOT_PASSWORD_LINK = By.LINK_TEXT, "Восстановить пароль" # Ссылка Восстановить пароль
    CONSTRUCTOR_BUTTON = By.LINK_TEXT, "Конструктор" # Кнопка Коструктор
    EXIT_BUTTON = By.CLASS_NAME, "Account_button__14Yp3" # Кнопка Выход
    SAUCES_TAB = By.XPATH, '//*[@id="root"]//span[text()="Соусы"]' # Вкладка Соусы
    BUNS_TAB = By.XPATH, '//*[@id="root"]//span[text()="Булки"]' # Вкладка Булки
    FILLINGS_TAB = By.XPATH, '//*[@id="root"]//span[text()="Начинки"]' # Вкладка Начинки
    BUNS_CLASS = By.XPATH, './/*[@id="root"]//span[text()="Булки"]/parent::div' # Класс Булки
    SAUCES_CLASS = By.XPATH, './/*[@id="root"]//span[text()="Соусы"]/parent::div' # Класс Соусы
    FILLINGS_CLASS = By.XPATH, './/*[@id="root"]//span[text()="Начинки"]/parent::div' # Класс Начинки

