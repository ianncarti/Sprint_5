from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LoginPageLocators, ConstructorPageLocators, RegistrationPageLocators, HeaderLinks, \
    PasswordRecoveryPageLocators
from urls import AppUrls


class TestLoginPage:

    email_valid = "yan_prytkov_17123@gmail.com"
    password_valid = "123456"

    def test_login_from_button_on_main_page(self, browser):
        # открываем главную страницу
        browser.get(AppUrls.main_page)

        # жмём кнопку "Войти в аккаунт"
        browser.find_element(*ConstructorPageLocators.button_login_into_account).click()

        # вводим валидные креды
        browser.find_element(*LoginPageLocators.email_field).send_keys(self.email_valid)
        browser.find_element(*LoginPageLocators.password_field).send_keys(self.password_valid)

        # жмём кнопку "Войти"
        browser.find_element(*LoginPageLocators.button_auth).click()

        # ждём появления кнопки "Оформить заказ"
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(ConstructorPageLocators.button_order))

        # проверяем, что после авторизации перекинуло на страницу конструктора
        assert browser.current_url == AppUrls.main_page

    def test_login_from_personal_account_button(self, browser):
        # открываем главную страницу
        browser.get(AppUrls.main_page)

        # жмём кнопку "Личный кабинет"
        browser.find_element(*HeaderLinks.personal_account_link).click()

        # вводим валидные креды
        browser.find_element(*LoginPageLocators.email_field).send_keys(self.email_valid)
        browser.find_element(*LoginPageLocators.password_field).send_keys(self.password_valid)

        # жмём кнопку "Войти"
        browser.find_element(*LoginPageLocators.button_auth).click()

        # ждём появления кнопки "Оформить заказ"
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(ConstructorPageLocators.button_order))

        # проверяем, что после авторизации перекинуло на страницу конструктора
        assert browser.current_url == AppUrls.main_page

    def test_login_from_registration_form(self, browser):
        # открываем страницу регистрации
        browser.get(AppUrls.register_page)

        # жмём кнопку "Войти"
        browser.find_element(*RegistrationPageLocators.button_login_from_reg_page).click()

        # вводим валидные креды
        browser.find_element(*LoginPageLocators.email_field).send_keys(self.email_valid)
        browser.find_element(*LoginPageLocators.password_field).send_keys(self.password_valid)

        # жмём кнопку "Войти"
        browser.find_element(*LoginPageLocators.button_auth).click()

        # ждём появления кнопки "Оформить заказ"
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(ConstructorPageLocators.button_order))

        # проверяем, что после авторизации перекинуло на страницу конструктора
        assert browser.current_url == AppUrls.main_page

    def test_login_from_password_recovery_form(self, browser):
        # открываем страницу восстановления пароля
        browser.get(AppUrls.password_recovery_page)

        # жмём кнопку "Войти"
        browser.find_element(*PasswordRecoveryPageLocators.button_login_from_pass_recovery).click()

        # вводим валидные креды
        browser.find_element(*LoginPageLocators.email_field).send_keys(self.email_valid)
        browser.find_element(*LoginPageLocators.password_field).send_keys(self.password_valid)

        # жмём кнопку "Войти"
        browser.find_element(*LoginPageLocators.button_auth).click()

        # ждём появления кнопки "Оформить заказ"
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(ConstructorPageLocators.button_order))

        # проверяем, что после авторизации перекинуло на страницу конструктора
        assert browser.current_url == AppUrls.main_page
