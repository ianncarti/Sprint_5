from selenium.webdriver.common.by import By


# Страница регистрации
class RegistrationPageLocators:
    user_name = (By.XPATH, ".//label[text()='Имя']/following-sibling::input") # инпут для поля "Имя"
    reg_login = (By.XPATH, ".//label[text()='Email']/following-sibling::input") # инпут для поля "Email"
    reg_password = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input") # инпут для поля "Пароль"
    button_registration = (By.XPATH, ".//button[text()='Зарегистрироваться']") # кнопка регистрации
    button_login_from_reg_page = (By.CLASS_NAME, 'Auth_link__1fOlj') # кнопка "Войти" на странице регистрации
    error_text = (By.XPATH, ".//p[text()='Некорректный пароль']") # текст ошибки при пароле <6 символов

# Страница логина
class LoginPageLocators:
    email_field = (By.XPATH, ".//label[text()='Email']/following-sibling::input") # поле ввода email
    password_field = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input") # поле ввода пароля
    button_auth = (By.XPATH, ".//button[text()='Войти']") # кнопка входа в аккаунт

# Страница конструктора
class ConstructorPageLocators:
    button_login_into_account = (By.XPATH, ".//button[text()='Войти в аккаунт']") # кнопка "Войти в аккаунт"
    button_order = (By.XPATH, ".//button[text()='Оформить заказ']") # кнопка "Оформить заказ"
    button_personal_account = (By.XPATH, ".//p[text()='Личный Кабинет']/ancestor::a") # кнопка "Личный Кабинет"
    tab_buns = (By.XPATH, ".//section/div/div/span[text()='Булки']/..") # таб в конструкторе скроллящий на булки
    tab_sauce = (By.XPATH, ".//section/div/div/span[text()='Соусы']/..") # таб в конструкторе скроллящий на соусы
    tab_toppings = (By.XPATH, ".//section/div/div/span[text()='Начинки']/..") # таб в конструкторе скроллящий на начинки
    tab_active = (By.CLASS_NAME, "tab_tab_type_current__2BEPc") # находит активный таб

# Ссылки в хэдере сайта
class HeaderLinks:
    personal_account_link = (By.XPATH, ".//p[text()='Личный Кабинет']/ancestor::a")  # ссылка на "Личный Кабинет"
    constructor_link = (By.XPATH, ".//p[text()='Конструктор']/ancestor::a") # сслыка на "Конструктор" в хэдере
    logo_link = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']/a") # Кликабельное лого в хэдере, ведёт на главную страницу


# Страница профиля
class ProfilePageLocators:
    button_profile = (By.XPATH, './/a[text()="Профиль"]') # Кнопка "Профиль" в боковом меню в личном кабинете
    button_logout = (By.XPATH, ".//button[text()='Выход']") # Кнопка "Выход" из профиля

# Страница восстановления пароля
class PasswordRecoveryPageLocators:
    button_login_from_pass_recovery = (By.CLASS_NAME, "Auth_link__1fOlj") # кнопка входа в аккаунт на странице восстановления пароля
