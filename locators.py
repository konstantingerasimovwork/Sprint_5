from selenium.webdriver.common.by import By


class TestLocators:
    REGISTRATION_NAME = By.XPATH, './/label[text()="Имя"]/following-sibling::input' # Поле Имя на странице регистрации
    REGISTRATION_EMAIL = By.XPATH, './/label[text()="Email"]/following-sibling::input' # Поле Email на странице регистрации
    REGISTRATION_PASSWORD = By.XPATH, './/input[@name="Пароль"]' # Поле Пароль на странице регистрации
    REGISTRATION_BUTTON = By.CLASS_NAME, 'button_button__33qZ0' # Кнопка Зарегистрироваться на странице регистрации
    ENTER_EMAIL = By.XPATH, './/label[text()="Email"]/following-sibling::input' # Поля Email на странице входа
    ENTER_PASSWORD = By.XPATH, './/input[@name="Пароль"]' # Поля Пароль на странице входа
    ENTER_BUTTON = By.CLASS_NAME, 'button_button__33qZ0' #Кнопка Войти на странице входа
    ENTER_LINK = By.XPATH, '//a[@href="/login"]' # Кнопка Войти на странице регистрации
    ENTER_HEADER = By.XPATH, './/h2[text()="Вход"]' #Заголовок Вход на странице входа
    INCORRECT_PASSWORD_MESSAGE = By.CLASS_NAME, 'input__error' #Сообщение Некорректный пароль при вводе невалидного пароля
    LOGIN_TO_ACCOUNT_LINK = By.CLASS_NAME, 'button_button__33qZ0' #Кнопка "Войти в аккаунт"
    LOGO_LINK = By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]/a[@href="/"]' #Ссылка логотипа Stellar Burgers
    LK_BUTTON = By.LINK_TEXT, "Личный Кабинет" # Кнопка "Личный Кабинет"
    REGISTRATION_LINK = By.LINK_TEXT, "Зарегистрироваться" # Ссылка Зарегистрироваться
    FORGOT_PASSWORD_LINK = By.LINK_TEXT, "Восстановить пароль" # Ссылка Восстановить пароль
    CONSTRUCTOR_BUTTON = By.LINK_TEXT, "Конструктор" # Кнопка Коструктор
    EXIT_BUTTON = By.CLASS_NAME, "Account_button__14Yp3" # Кнопка Выход
    SAUCES_TAB = By.XPATH, '//span[text()="Соусы"]' # Вкладка Соусы
    BUNS_TAB = By.XPATH, '//span[text()="Булки"]' # Вкладка Булки
    FILLINGS_TAB = By.XPATH, '//span[text()="Начинки"]' # Вкладка Начинки
    BUNS_CLASS = By.XPATH, './/span[text()="Булки"]/parent::div' # Класс Булки
    SAUCES_CLASS = By.XPATH, './/span[text()="Соусы"]/parent::div' # Класс Соусы
    FILLINGS_CLASS = By.XPATH, './/span[text()="Начинки"]/parent::div' # Класс Начинки

