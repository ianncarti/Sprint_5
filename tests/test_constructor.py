from locators import ConstructorPageLocators
from urls import AppUrls


class TestConstructorTabs:
    def test_constructor_tabs_buns_selected_by_default(self, browser, login):
        # открываем страницу конструктора
        browser.get(AppUrls.main_page)

        # получаем классы таба булок и активного таба
        buns_class = browser.find_element(*ConstructorPageLocators.tab_buns).get_attribute("class")
        tab_active_class = browser.find_element(*ConstructorPageLocators.tab_active).get_attribute("class")

        # проверяем, что булки являются активным табом
        assert tab_active_class in buns_class

    def test_constructor_tabs_switch_to_buns_after_sauce(self, browser, login):
        # открываем страницу конструктора
        browser.get(AppUrls.main_page)

        # жмём таб "Соусы"
        browser.find_element(*ConstructorPageLocators.tab_sauce).click()

        # жмём таб "Булки"
        browser.find_element(*ConstructorPageLocators.tab_buns).click()

        # получаем классы таба булок и активного таба
        buns_class = browser.find_element(*ConstructorPageLocators.tab_buns).get_attribute("class")
        tab_active_class = browser.find_element(*ConstructorPageLocators.tab_active).get_attribute("class")

        # проверяем, что булки являются активным табом
        assert tab_active_class in buns_class

    def test_constructor_tabs_switch_tab_to_sauce(self, browser, login):
        # открываем страницу конструктора
        browser.get(AppUrls.main_page)

        # жмём таб "Соусы"
        browser.find_element(*ConstructorPageLocators.tab_sauce).click()

        # получаем классы таба соусов и активного таба
        sauce_class = browser.find_element(*ConstructorPageLocators.tab_sauce).get_attribute("class")
        tab_active_class = browser.find_element(*ConstructorPageLocators.tab_active).get_attribute("class")

        # проверяем, что соусы являются активным табом
        assert tab_active_class in sauce_class

    def test_constructor_tabs_switch_tab_to_toppings(self, browser, login):
        # открываем страницу конструктора
        browser.get(AppUrls.main_page)

        # жмём таб "Начинки"
        browser.find_element(*ConstructorPageLocators.tab_toppings).click()

        # получаем классы таба начинки и активного таба
        toppings_class = browser.find_element(*ConstructorPageLocators.tab_toppings).get_attribute("class")
        tab_active_class = browser.find_element(*ConstructorPageLocators.tab_active).get_attribute("class")

        # проверяем, что начинки являются активным табом
        assert tab_active_class in toppings_class
