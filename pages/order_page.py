import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators



class OrderPage(BasePage):

    @allure.step("Ожидание загрузки формы заказа")
    def wait_for_order_form(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.NAME_INPUT)
        )

    @allure.step('Ввод имени')
    def set_name (self, name):
        self.add_text_to_element(OrderPageLocators.NAME_INPUT, name)

    @allure.step('Ввод фамилии')
    def set_surname(self, surname):
        self.add_text_to_element(OrderPageLocators.SURNAME_INPUT, surname)

    @allure.step('Ввод адреса')
    def set_address(self, address):
        self.add_text_to_element(OrderPageLocators.ADDRESS_INPUT, address)

    @allure.step('Выбор станции метро')
    def select_metro(self, metro_name):

        # Находим инпут и вводим название станции
        input_field = self.find_element_with_wait(OrderPageLocators.METRO_INPUT)
        input_field.send_keys(metro_name)

        input_field.send_keys(Keys.ARROW_DOWN)
        input_field.send_keys(Keys.ENTER)

    @allure.step('Ввод номера')
    def set_phone(self, phone):
        self.add_text_to_element(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step('Клик по кнопке Далее')
    def click_next(self):
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Выбор даты аренды')
    def select_date(self, days_from_today=1):
        from datetime import datetime, timedelta
        target_date = datetime.today() + timedelta(days=days_from_today)
        formatted_date = target_date.strftime("%d.%m.%Y")

        date_input = self.find_element_with_wait(OrderPageLocators.DATE_INPUT)
        date_input.send_keys(formatted_date)
        date_input.send_keys(Keys.ENTER)

    @allure.step('Выбор срока аренды')
    def select_duration(self, duration_text):
        self.click_to_element(OrderPageLocators.DURATION_DROPDOWN)
        option = OrderPageLocators.get_duration_option(duration_text)
        element = self.find_element_with_wait(option)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    @allure.step('Выбор цвета самоката')
    def select_color(self, color_text):
        checkbox = OrderPageLocators.get_color_checkbox(color_text)
        self.click_to_element(checkbox)

    @allure.step('Ввод комментария')
    def set_comment(self, comment):
        self.add_text_to_element(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step('Нажать кнопку "Заказать"')
    def submit_order(self):
        element = self.find_element_with_wait(OrderPageLocators.ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON))
        element.click()

    @allure.step('Подтверждение заказа')
    def confirm_order(self):
        self.click_to_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Проверка успешного оформления заказа')
    def check_order_success(self):
        return self.get_text_from_element(OrderPageLocators.MODAL_HEADER)