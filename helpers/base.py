class BaseHelpers:
    """Helpers for web testing"""

    def __init__(self, driver):
        self.driver = driver

    def fill_input_field(self, by, locator, value):
        """Finding required elements using by.X model, clear fields, enter values"""
        username = self.driver.find_element(by=by, value=locator)
        username.clear()
        username.send_keys(value)

    def find_by_text(self, text, element_tag="*"):
        """Finding the elements using XPATH"""
        return self.driver.find_element_by_xpath(f".//{element_tag}[contains(text(), '{text}')]")
