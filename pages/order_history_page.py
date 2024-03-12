from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators


class OrdersHistoryPage(BasePage):
    @allure.step('Ждем загрузки первого заказа из Ленты Заказов')
    def wait_for_orders_loaded(self):
        self.wait_for_element_loaded(OrderPageLocators.FIRST_ORDER)

    @allure.step('Проверяем наличие ID заказа в Истории заказов')
    def check_order_id_in_orders_history(self, order_id):
        locator = f"//p[contains(text(), '{order_id}')]"
        self.check_pop_opened(locator)

    @allure.step('Кликаем Лента Заказов')
    def click_orders_list(self):
        self.click_element_located(MainPageLocators.ORDER_LINE)