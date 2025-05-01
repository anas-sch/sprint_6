import pytest
import allure

from data import ORDER_DATA_1, ORDER_DATA_2
from locators.main_page_locators import MainPageLocators
from pages.order_page import OrderPage

@allure.title("Позитивный сценарий оформления заказа с параметризацией")
@pytest.mark.parametrize("order_data", [ORDER_DATA_1, ORDER_DATA_2])
def test_create_order(driver, main_page, order_data):
    main_page.click_to_element(MainPageLocators.COOKIE_CLOSE_BUTTON)
    # Клик по кнопке в зависимости от данных
    main_page.click_order_button(order_data["button"])

    order_page = OrderPage(driver)
    order_page.wait_for_order_form()

    # Первая страница
    order_page.set_name(order_data["name"])
    order_page.set_surname(order_data["surname"])
    order_page.set_address(order_data["address"])
    order_page.select_metro(order_data["metro"])
    order_page.set_phone(order_data["phone"])
    order_page.click_next()

    # Вторая страница
    order_page.select_date(order_data["days_from_today"])
    order_page.select_duration(order_data["duration"])
    order_page.select_color(order_data["color"])
    order_page.set_comment(order_data["comment"])
    order_page.submit_order()
    order_page.confirm_order()

    # Проверка успешного оформления
    assert "Заказ оформлен" in order_page.check_order_success()
