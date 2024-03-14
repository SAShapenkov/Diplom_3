import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators

class OrdersListPage(BasePage):

    @allure.step('Ждем загрузки заголовка страницы Ленты Заказов')
    def wait_for_orders_list_header_loaded(self):
        self.wait_for_element_loaded(OrderPageLocators.ORDER_LIST_HEADER)

    @allure.step('Получаем ID первого заказа')
    def get_first_order_id(self):
        return self.get_text_by_locator(OrderPageLocators.FIRST_ORDER[1])

    @allure.step('Кликаем заказ Ленты Заказов по номеру {order_id}')
    def click_order_by_id(self, order_id):
        or_a = OrderPageLocators.ORDER_LOCATOR_A
        or_b = OrderPageLocators.ORDER_LOCATOR_B
        locator = f"{or_a}+{order_id}+{or_b}"
        selector = (By.XPATH, locator)
        self.click_element_located(selector)

    @allure.step('Проверяем видимость модального окна')
    def check_order_details_modal_opened(self):
        self.check_pop_opened(OrderPageLocators.ORDER_DETAILS_POPUP)

    @allure.step('Получаем ID заказа из заголовка модального окна')
    def get_order_id_from_modal(self):
        return self.get_text_by_locator(OrderPageLocators.ORDER_DETAILS_POPUP_ORDER_ID_XPATH)

    @allure.step('Проверяем наличие ID {order_id} заказа в Ленте заказов')
    def check_order_id_in_orders_list(self, order_id):
        or_a = OrderPageLocators.ORDER_LOCATOR_A
        or_b = OrderPageLocators.ORDER_LOCATOR_B
        locator = f"{or_a}+{order_id}+{or_b}"
        self.check_pop_opened(locator)

    @allure.step('Нажимаем Конструктор')
    def click_constructor(self):
        return self.click_element_located(MainPageLocators.MENU_CONSTRUCTOR)

    @allure.step('Получаем значение счетчика Выполнено за все время')
    def get_total_count(self):
        return self.get_text_by_locator(OrderPageLocators.TOTAL_COUNT_XPATH)

    @allure.step('Получаем значение счетчика Выполнено за сегодня')
    def get_today_count(self):
        return self.get_text_by_locator(OrderPageLocators.TODAY_COUNT_XPATH)

    @allure.step('Проверяем наличие ID {order_id} заказа среди заказов в работе')
    def check_order_id_in_processing_orders(self, order_id):
        or_c = OrderPageLocators.ORDER_LOCATOR_C
        or_d = OrderPageLocators.ORDER_LOCATOR_D
        locator = f"{or_c}+{order_id}+{or_d}"
        self.check_pop_opened(locator)