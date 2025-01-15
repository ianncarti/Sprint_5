from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import ProfilePageLocators, HeaderLinks, LoginPageLocators
from urls import AppUrls


class TestLogout:
   def test_logout(self, browser, login):
       # открываем страницу конструктора
       browser.get(AppUrls.main_page)

       # жмём кнопку "Личный кабинет"
       browser.find_element(*HeaderLinks.personal_account_link).click()

       # ждём появления кнопки "Профиль"
       WebDriverWait(browser, 3).until(
           expected_conditions.visibility_of_element_located(ProfilePageLocators.button_profile))

       # жмём кнопку "Выход"
       browser.find_element(*ProfilePageLocators.button_logout).click()

       # ждём появления кнопки "Войти"
       WebDriverWait(browser, 3).until(
           expected_conditions.visibility_of_element_located(LoginPageLocators.button_auth))

       # проверяем, что после выхода перекинуло на страницу логина
       assert browser.current_url == AppUrls.login_page
