from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import ProfilePageLocators, HeaderLinks, ConstructorPageLocators
from urls import AppUrls


class TestRedirectsToProfile:
    def test_redirect_to_profile(self, browser, login):
        # открываем страницу конструктора
        browser.get(AppUrls.main_page)

        # жмём кнопку "Личный кабинет"
        browser.find_element(*HeaderLinks.personal_account_link).click()

        # ждём появления кнопки "Профиль"
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(ProfilePageLocators.button_profile))

        # проверяем, что находимся на странице профиля
        assert browser.current_url == AppUrls.profile_page

class TestRedirectsToConstructor:
    def test_redirect_from_profile_to_constructor(self, browser, login):
        # открываем страницу конструктора
        browser.get(AppUrls.main_page)

        # жмём кнопку "Личный кабинет"
        browser.find_element(*HeaderLinks.personal_account_link).click()

        # ждём появления кнопки "Профиль"
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(ProfilePageLocators.button_profile))

        # жмём ссылку "Конструктор" в хэдере
        browser.find_element(*HeaderLinks.constructor_link).click()

        # ждём появления кнопки "Оформление заказа"
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(ConstructorPageLocators.button_order))

        # проверяем, что произошёл переход на страницу конструктора
        assert browser.current_url == AppUrls.main_page

    def test_redirect_to_constructor_by_clicking_on_logo(self, browser, login):
        # открываем страницу конструктора
        browser.get(AppUrls.main_page)

        # жмём кнопку "Личный кабинет"
        browser.find_element(*HeaderLinks.personal_account_link).click()

        # ждём появления кнопки "Профиль"
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(ProfilePageLocators.button_profile))

        # жмём на лого в хэдере
        browser.find_element(*HeaderLinks.logo_link).click()

        # ждём появления кнопки "Оформление заказа"
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(ConstructorPageLocators.button_order))

        # проверяем, что произошёл переход на страницу конструктора
        assert browser.current_url == AppUrls.main_page
