import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import ValidUserCreds
from locators import LoginPageLocators, ConstructorPageLocators
from urls import AppUrls


@pytest.fixture
def browser():
    # Настройка драйвера браузера
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login(browser):
    # открываем страницу входа в аккаунт
    browser.get(AppUrls.login_page)

    # ввод кредов в поля
    browser.find_element(*LoginPageLocators.email_field).send_keys(ValidUserCreds.email_valid)
    browser.find_element(*LoginPageLocators.password_field).send_keys(ValidUserCreds.password_valid)

    # нажатие кнопки "Войти"
    browser.find_element(*LoginPageLocators.button_auth).click()

    # ждём появления кнопки оформления заказа
    WebDriverWait(browser, 3).until(
        expected_conditions.visibility_of_element_located(ConstructorPageLocators.button_order))
