# Sprint_5
### Предварительные требования
* Python 3.11
* pytest
* Selenium
* ChromeDriver для Chrome

### Запуск тестов
* pytest -v
* pytest -v tests/test_registration.py
* pytest -v tests/test_login.py
* pytest -v tests/test_personal_account.py
* pytest -v tests/test_constructor.py

Тесты запускаются для сайта https://stellarburgers.nomoreparties.site/

### Описания тестов
#### test_registration (Проверка регистрации)
* test_correct_registration - Успешная регистрация
* test_incorrect_registration_password_less_6_characters - Неуспешная регистрация - пароль меньше 6 символов

#### test_login (Проверка входа) 
* test_enter_login_to_account - вход по кнопке «Войти в аккаунт» на главной
* test_enter_lk - вход по кнопке «Личный кабинет» на главной
* test_enter_form_registration - вход через кнопку в форме регистрации
* test_enter_password_recovery - вход через кнопку в форме восстановления пароля

#### test_personal_account (Проверка личного кабинета)
* test_click_lk_button - Переход в личный кабинет
* test_following_button_contructor - Переход из личного кабинета в конструктор по кнопке конструктор
* test_following_logo - Переход из личного кабинета в конструктор по логотипу Stellar Burgers
* test_following_exit_button - Переход из личного кабинета в конструктор по логотипу Stellar Burgers

#### test_constructor (Проверка раздела 'Конструктор')
* test_select_buns_from_sauces - Переход к разделу Булки из раздела Соусы
* est_select_buns_from_filling - Переход к разделу Булки из раздела Начинки
* test_select_sauces_from_buns - Переход к разделу Соусы из раздела Булки
* test_select_sauces_from_filling - Переход к разделу Соусы из раздела Начинки
* test_select_filling_from_buns - Переход к разделу Начинки из раздела Булки
* test_select_filling_from_sauces - Переход к разделу Начинки из раздела Соусы
