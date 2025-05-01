import pytest
import allure

from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage


class TestPageRedirect:
    @allure.title("Переход на главную при клике на логотип 'Самокат'")
    def test_scooter_logo_redirects_to_main_page(self, main_page, driver):
        main_page = MainPage(driver)
        main_page.go_to_url("https://qa-scooter.praktikum-services.ru/")
        main_page.click_to_element(MainPageLocators.COOKIE_CLOSE_BUTTON)
        main_page.click_to_element(MainPageLocators.SCOOTER_LOGO)
        assert ("qa-scooter.praktikum-services.ru" in main_page.driver.current_url)

    @allure.title("Переход на Яндекс.Дзен при клике на логотип Яндекса")
    def test_yandex_logo_redirects_to_dzen(self, main_page, driver):
        main_page = MainPage(driver)

        main_page.go_to_url("https://qa-scooter.praktikum-services.ru/")
        main_page.click_to_element(MainPageLocators.COOKIE_CLOSE_BUTTON)
        main_page.click_to_element(MainPageLocators.YANDEX_LOGO)
        main_page.driver.switch_to.window(main_page.driver.window_handles[-1])
        WebDriverWait(main_page.driver, 10).until(EC.url_contains("dzen"))
        assert "dzen.ru" in main_page.driver.current_url