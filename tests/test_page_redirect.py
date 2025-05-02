import pytest
import allure
from data import YA_SCOOTER_MAIN_PAGE


class TestPageRedirect:
    @allure.title("Переход на главную при клике на логотип 'Самокат'")
    def test_scooter_logo_redirects_to_main_page(self, main_page):
        main_page.click_scooter_logo()

        assert YA_SCOOTER_MAIN_PAGE in main_page.get_current_url()

    @allure.title("Переход на Яндекс.Дзен при клике на логотип Яндекса")
    def test_yandex_logo_redirects_to_dzen(self, main_page):
        main_page.click_yandex_logo()

        assert "dzen.ru" in main_page.get_current_url()