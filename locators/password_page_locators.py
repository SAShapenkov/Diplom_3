from selenium.webdriver.common.by import By
class PasswordPageLocators:
    HEADER_RESTORE_PASSWORD = (By.XPATH, ".//h2[text()='Восстановление пароля']")  # Хедер страницы восстан. пароля
    BUTTON_ENTER_ACCOUNT_FROM_RESTORE_FORM = (By.XPATH, "//a[text()='Войти']")  # Кнопка входа в аккаунт на форме
    # восстановления пароля
    EMAIL_INPUT_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::*")  # Поле ввода e-mail
    BUTTON_RESTORE_PASSWORD = (By.XPATH, "//button[text()='Восстановить']")  # Кнопка выхода из аккаунта
    SHOW_PASSWORD_BUTTON = (By.XPATH, ".//div[contains(@class, 'input__icon')]")
    ACTIVE_PASSWORD_INPUT_FIELD = (By.XPATH, ".//div[contains(@class, 'input_status_active')]")