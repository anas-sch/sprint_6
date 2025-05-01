from selenium.webdriver.common.by import By


class OrderPageLocators:

    COOKIE_CLOSE_BUTTON = (By.ID, "rcc-confirm-button")

    # Первая страница заказа
    NAME_INPUT = (By.CSS_SELECTOR, "input.Input_Input__1iN_Z[placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_INPUT = (By.CLASS_NAME, "select-search__input")
    PHONE_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')

    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')

    # Вторая страница заказа
    DATE_INPUT = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    DURATION_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    COLOR_BLACK_PEARL = (By.XPATH,"//label[text()='чёрный жемчуг']/input[@type='checkbox']")
    COLOR_GREY_HOPELESSNESS = (By.XPATH, "//label[text()='серая безысходность']/input[@type='checkbox']")
    COMMENT_INPUT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')

    ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[2]')
    CONFIRM_BUTTON = (By.XPATH, '//button[contains(text(), "Да")]')
    MODAL_HEADER = (By.XPATH, '//div[contains(@class, "Order_ModalHeader")]')

    @staticmethod
    def get_metro_button(metro_name):
        return By.XPATH, f"//button[contains(@class, 'select-search__option') and text()='{metro_name}']"

    @staticmethod
    def get_date_element(day: str):
        return (By.XPATH, f"//div[contains(@class,'react-datepicker__day') and text()='{day}']")

    @staticmethod
    def get_duration_option(duration_text: str):
        return (By.XPATH, f"//div[contains(@class,'Dropdown-option') and text()='{duration_text}']")

    @staticmethod
    def get_color_checkbox(color_text: str):
        return (By.XPATH, f"//label[text()='{color_text}']/input[@type='checkbox']")

