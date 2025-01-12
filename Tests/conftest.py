import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
from locators import LoginPageLocators, ConstructorPageLocators


@pytest.fixture
def browser():
    # Настройка драйвера браузера
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login(browser):
    # открываем страницу входа в аккаунт
    url_login_page = "https://stellarburgers.nomoreparties.site/login"
    browser.get(url_login_page)

    # валидные креды для входа
    email_valid = "yan_prytkov_17123@gmail.com"
    password_valid = "123456"

    # ввод кредов в поля
    browser.find_element(*LoginPageLocators.email_field).send_keys(email_valid)
    browser.find_element(*LoginPageLocators.password_field).send_keys(password_valid)

    # нажатие кнопки "Войти"
    browser.find_element(*LoginPageLocators.button_auth).click()

    # ждём появления кнопки оформления заказа
    WebDriverWait(browser, 3).until(
        expected_conditions.visibility_of_element_located(ConstructorPageLocators.button_order))

@pytest.fixture
def random_user_generator():
    random_name = "Amogus" + str(random.randint(100, 999)) # рандомный юзернейм из слова "Amogus" и 3-х рандомных цифр
    random_login = random_name + "@yandex.ru" # на основе сгенерированного юзернейма делаем почту
    random_password = str(random.randint(100000, 999999)) # генерируем пароль из 6 цифр
    return random_name, random_login, random_password
