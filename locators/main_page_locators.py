from selenium.webdriver.common.by import By

class MainPageLocators:
    QUESTION_LOCATOR = (By.XPATH, '//*[@id="accordion__heading-{}"]')
    ANSWER_LOCATOR = (By.XPATH, '//*[@id="accordion__panel-{}"]')
    QUESTION_LOCATOR_TO_SCROLL = (By.XPATH, '//*[@id="accordion__heading-7"]')

    #закрытие куки
    COOKIE_CLOSE_BUTTON = (By.ID, "rcc-confirm-button")

    # Кнопки "Заказать"
    ORDER_BUTTON = {
        "top": (By.XPATH, '//div[contains(@class, "Header_Nav__")]/button[text()="Заказать"]'),
        "bottom": (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]')
    }

    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")