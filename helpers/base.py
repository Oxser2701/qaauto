import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseHelpers:
    """Helpers for web testing"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=5)

    def wait_until_element_found(self, locator_type, locator):
        """Wait till element found"""
        self.wait.until(EC.presence_of_element_located((locator_type, locator)))
        return self.driver.find_element(by=locator_type, value=locator)

    def wait_and_click(self, locator_type, locator):
        """Wait until element clickable and click"""
        self.wait.until(EC.element_to_be_clickable((locator_type, locator)))
        self.driver.find_element(by=locator_type, value=locator).click()

    def fill_input_field(self, by, locator, value):
        """Finding required elements using by.X model, clear fields, enter values"""
        field = self.wait_until_element_found(locator_type=by, locator=locator)
        field.clear()
        field.send_keys(value)

    def find_by_text(self, text, element_tag="*"):
        """Finding the elements using XPATH"""
        return self.wait_until_element_found(By.XPATH, f".//{element_tag}[contains(text(), '{text}')]")
