from selenium.webdriver.common.by import By
class ProfilePageLocators:
    BUTTON_EXIT_ACCOUNT = (By.XPATH, "//button[text()='Выход']")  # Кнопка выхода из аккаунта
    ORDERS_HISTORY_AREA = (By.XPATH, "//a[text()='История заказов']")  # Кнопка секции истории заказов
    PROFILE_AREA = (By.XPATH, "//a[text()='Профиль']")  # Кнопка секции истории заказов