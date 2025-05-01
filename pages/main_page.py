import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class MainPage(BasePage):

    @allure.step('Клик на вопрос')
    def click_to_question(self, num):
        self.click_to_element(MainPageLocators.COOKIE_CLOSE_BUTTON)
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_TO_SCROLL)
        self.scroll_to_element(locator_q_formatted)
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator_q_formatted))
        self.click_to_element(locator_q_formatted)

    @allure.step('Получение ответа на вопрос')
    def get_answer_text(self, num):
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator_a_formatted))
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Проверяем ответ')
    def check_question_and_answer(self, num):
        self.click_to_question(num)
        return self.get_answer_text(num)

    @allure.step('Клик по кнопке "Заказать" — позиция: {position}')
    def click_order_button(self, position: str):
        locator = MainPageLocators.ORDER_BUTTON[position]
        if position == "bottom":
            self.scroll_to_element(locator)
        self.click_to_element(locator)