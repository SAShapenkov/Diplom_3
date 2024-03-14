from selenium.webdriver.common.by import By

class AuthPageLocators:

  ENTRANCE_HEADER = (By.XPATH, ".//h2[text()='Вход']")  # Заголовок формы логина
  BUTTON_RESTORE_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")  # Гиперссылка для восстановления пароля
  EMAIL_INPUT_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::*")  # Поле ввода e-mail
  PASSWORD_INPUT_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::*")  # Поле ввода пароля
  BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")  # Кнопка входа на форме логина