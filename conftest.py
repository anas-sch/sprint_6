import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import YA_SCOOTER_MAIN_PAGE
from data import  YA_SCOOTER_ORDER_PAGE


@pytest.fixture(scope="function")
def driver():
    options = FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Firefox(options=options)
    try:
        driver.get(YA_SCOOTER_MAIN_PAGE)

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "Home_Header__iJKdX"), "Самокат"
            ),
            message="Текст 'Самокат' не появился на главной"
        )

        yield driver

    except WebDriverException as e:
        pytest.fail(f"Ошибка инициализации браузера {str(e)}")

    finally:
        driver.quit()


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    return page

@pytest.fixture
def order_page(driver):
    return OrderPage(driver)
