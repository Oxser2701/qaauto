import logging
from time import sleep

from selenium.webdriver.common.by import By

from constant.base import BaseConstant
from constant.login_page import LoginPageConstant
from helpers.base import BaseHelpers


class LoginHelpers(BaseHelpers):
    """Login page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.log = logging.getLogger(__name__)

    def login(self, username, password):
        self.fill_input_field(by=By.XPATH, locator=LoginPageConstant.SIGN_IN_USERNAME_XPATH, value=username)
        self.fill_input_field(by=By.XPATH, locator=LoginPageConstant.SIGN_IN_PASSWORD_XPATH, value=password)
        self.log.debug("Enter correct values")

        # Click the button
        self.wait_and_click(By.XPATH, LoginPageConstant.SIGN_IN_BUTTON_XPATH)
        self.log.info("Click on the button")

    def register_user(self, username, email, password):
        """Fill required fields"""

        # Open start page
        self.driver.get(BaseConstant.START_PAGE_URL)

        # Enter values
        self.fill_input_field(by=By.XPATH, locator=LoginPageConstant.SIGN_UP_USERNAME_XPATH, value=username)
        self.fill_input_field(by=By.XPATH, locator=LoginPageConstant.SIGN_UP_PASSWORD_XPATH, value=password)
        self.fill_input_field(by=By.XPATH, locator=LoginPageConstant.SIGN_UP_EMAIL_XPATH, value=email)
        self.log.debug("All fields were filled")
        sleep(1)
        # Click the button
        self.wait_and_click(By.XPATH, LoginPageConstant.SIGN_UP_BUTTON_XPATH)

        return username, email, password

    def verify_message(self, text):
        error_message = self.find_by_text(text)
        assert error_message.text == text
        self.log.debug("Error message")
