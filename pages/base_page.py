from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            locator))
        return  self.driver.find_element(*locator)

    def click_to_element(self, some):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(some))
        self.driver.find_element(*some).click()

    def add_text_to_element(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def format_locators(self, locator_1, num):
        method, locator = locator_1  # '//*[@class="my-question-locator-{}"]'
        locator = locator.format(num)  # '//*[@class="my-question-locator-1"]'

        return (method, locator)

    def scroll_to_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент {locator} не стал видимым на странице"
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def go_to_url(self, url):
        self.driver.get(url)

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

