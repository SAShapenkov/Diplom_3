from pages.main_page import MainPage
from pages.enterance_page import EnterancePage
from pages.profile_page import ProfilePage
import allure
from constants import Constants


class TestUserCabinet:
    @allure.title('По клику на личный кабинет переходим на Личный Кабинет')
    def test_main_page_to_user_cabinet(self, driver, make_user, create_user_payload):
        entrance_page = EnterancePage(driver)
        entrance_page.open_page(Constants.ENTRANCE_PAGE_SUBDIRECTORY)
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        entrance_page.wait_for_entrance_page_header_loaded()
        entrance_page.enter_email(payload["email"])
        entrance_page.enter_password(payload["password"])
        entrance_page.click_enter_button()
        entrance_page.check_page()
        main_page = MainPage(driver)
        main_page.wait_for_main_page_header_loaded()
        main_page.click_private_area_button()
        profile_page = ProfilePage(driver)
        profile_page.wait_for_profile_header_loaded()
        assert profile_page.check_page(Constants.PROFILE_PAGE_SUBDIRECTORY)

    @allure.title('Из личного кабинета можно перейти в Историю Заказов')
    def test_user_cabinet_to_order_list(self, driver, make_user, create_user_payload):
        entrance_page = EnterancePage(driver)
        entrance_page.open_page(Constants.ENTRANCE_PAGE_SUBDIRECTORY)
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        entrance_page.fill_email_and_password_and_enter(email=payload["email"], password=payload["password"])
        main_page = MainPage(driver)
        main_page.wait_for_main_page_header_loaded()
        main_page.click_private_area_button()
        main_page.check_page(Constants.PROFILE_PAGE_SUBDIRECTORY)
        profile_page = ProfilePage(driver)
        profile_page.wait_for_profile_header_loaded()
        profile_page.check_page(Constants.PROFILE_PAGE_SUBDIRECTORY)
        profile_page.click_orders_history_section_name()
        assert entrance_page.check_page(Constants.ORDER_HISTORY_SUBDIRECTORY)

    @allure.title('Из личного кабинета можно Выйти из аккаунта')
    def test_account_logout(self, driver, make_user, create_user_payload):
        entrance_page = EnterancePage(driver)
        entrance_page.open_page(Constants.ENTRANCE_PAGE_SUBDIRECTORY)
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        entrance_page.fill_email_and_password_and_enter(email=payload["email"], password=payload["password"])
        main_page = MainPage(driver)
        main_page.wait_for_main_page_header_loaded()
        main_page.click_private_area_button()
        main_page.check_page(Constants.PROFILE_PAGE_SUBDIRECTORY)
        profile_page = ProfilePage(driver)
        profile_page.wait_for_profile_header_loaded()
        profile_page.check_page(Constants.PROFILE_PAGE_SUBDIRECTORY)
        profile_page.click_exit()
        entrance_page.check_page(Constants.ENTRANCE_PAGE_SUBDIRECTORY)
        entrance_page.wait_for_entrance_page_header_loaded()
        entrance_page.click_constructor()
        entrance_page.check_page()
        main_page.wait_for_main_page_header_loaded()
        assert main_page.check_enter_account_button()