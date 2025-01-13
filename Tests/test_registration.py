from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import random_user_generator
from locators import RegistrationPageLocators, LoginPageLocators
from urls import AppUrls


class TestRegistration:

    def test_registration_with_valid_creds_success(self, browser):
        # генерируем рандомные креды
        username, email, password = random_user_generator()

        # открываем страницу регистрации
        browser.get(AppUrls.register_page)

        # находим инпуты и вводим сгенерированные данные
        browser.find_element(*RegistrationPageLocators.user_name).send_keys(username)
        browser.find_element(*RegistrationPageLocators.reg_login).send_keys(email)
        browser.find_element(*RegistrationPageLocators.reg_password).send_keys(password)

        # жмём кнопку регистрации
        browser.find_element(*RegistrationPageLocators.button_registration).click()

        # ждём появления кнопки "Войти"
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.button_auth))

        # проверяем, что после регистрации перекинуло на страницу логина
        assert browser.current_url == AppUrls.login_page


    def test_registration_with_invalid_pass_shows_error(self, browser):
        # генерируем рандомные креды
        username, email, password = random_user_generator()

        # открываем страницу регистрации
        browser.get(AppUrls.register_page)

        # находим инпуты и вводим сгенерированные данные, кроме пароля - пароль вводим невалидный
        browser.find_element(*RegistrationPageLocators.user_name).send_keys(username)
        browser.find_element(*RegistrationPageLocators.reg_login).send_keys(email)
        browser.find_element(*RegistrationPageLocators.reg_password).send_keys("123")

        # жмём кнопку регистрации
        browser.find_element(*RegistrationPageLocators.button_registration).click()

        # ждём появления текста "Некорректный пароль"
        WebDriverWait(browser, 3).until(
            expected_conditions.text_to_be_present_in_element((RegistrationPageLocators.error_text), "Некорректный пароль"))

        # Сохраняем текст ошибки в переменную
        error_text = browser.find_element(*RegistrationPageLocators.error_text).text

        # Проверяем, что текст ошибки присутствует на странице
        assert error_text in browser.page_source
