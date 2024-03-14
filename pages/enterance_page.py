import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.auth_page_locators import AuthPageLocators


class EnterancePage(BasePage):

    @allure.step('Ждем загрузки заголовка страницы входа')
    def wait_for_entrance_page_header_loaded(self):
        return self.wait_for_element_loaded(AuthPageLocators.ENTRANCE_HEADER)

    @allure.step('Нажимаем ссылку восстановления пароля')
    def click_restore_password(self):
        return self.click_element_located(AuthPageLocators.BUTTON_RESTORE_PASSWORD)

    @allure.step('Вводим email')
    def enter_email(self, email):
        self.send_keys_to_element_located(locator=AuthPageLocators.EMAIL_INPUT_FIELD, keys=email)

    @allure.step('Вводим пароль')
    def enter_password(self, password):
        self.send_keys_to_element_located(locator=AuthPageLocators.PASSWORD_INPUT_FIELD, keys=password)

    @allure.step('Нажимаем кнопку Войти')
    def click_enter_button(self):
        return self.click_element_located(AuthPageLocators.BUTTON_ENTER)

    @allure.step('Нажимаем Конструктор')
    def click_constructor(self):
        return self.click_element_located(MainPageLocators.MENU_CONSTRUCTOR)

    @allure.step('Заполняем поля email и пароль, нажимаем на вход')
    def fill_email_and_password_and_enter(self, email='', password=''):
        self.wait_for_entrance_page_header_loaded()
        self.enter_email(email)
        self.enter_password(password)
        self.click_enter_button()
        self.check_page()


