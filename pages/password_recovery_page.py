from pages.base_page import BasePage
import allure
from locators.password_page_locators import PasswordPageLocators


class PasswordRecoveryPage(BasePage):

    @allure.step('Ждем загрузки заголовка страницы Восстановления пароля')
    def wait_for_recovery_page_header_loaded(self):
        self.wait_for_element_loaded(PasswordPageLocators.HEADER_RESTORE_PASSWORD)

    @allure.step('Вводим имейл')
    def enter_email(self, email):
        self.send_keys_to_element_located(locator=PasswordPageLocators.EMAIL_INPUT_FIELD, keys=email)

    @allure.step('Нажимаем кнопку восстановления пароля')
    def recover_button_click(self):
        self.click_element_located(PasswordPageLocators.BUTTON_RESTORE_PASSWORD)