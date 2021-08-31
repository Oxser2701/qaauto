import logging
from time import sleep

from selenium.webdriver.common.by import By

from Pages.profile_page import ProfilePage
from constant.base import BaseConstant
from constant.login_page import LoginPageConstant
from helpers.base import BaseHelpers, UserData


class LoginPage(BaseHelpers):
    """Login page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.log = logging.getLogger(__name__)
        self.constants = LoginPageConstant

    def login(self, user: UserData):
        self.fill_input_field(by=By.XPATH, locator=self.constants.SIGN_IN_USERNAME_XPATH, value=user.username)
        self.fill_input_field(by=By.XPATH, locator=self.constants.SIGN_IN_PASSWORD_XPATH, value=user.password)
        self.log.debug("Enter correct values")

        # Click the button
        self.wait_and_click(By.XPATH, self.constants.SIGN_IN_BUTTON_XPATH)
        self.log.info("Click on the button")

        return ProfilePage(self.driver)

    def register_user(self, user: UserData):
        """Fill required fields"""

        # Open start page
        self.driver.get(BaseConstant.START_PAGE_URL)

        # Enter values

        self.fill_input_field(by=By.XPATH, locator=self.constants.SIGN_UP_USERNAME_XPATH, value=user.username)
        self.fill_input_field(by=By.XPATH, locator=self.constants.SIGN_UP_PASSWORD_XPATH, value=user.password)
        self.fill_input_field(by=By.XPATH, locator=self.constants.SIGN_UP_EMAIL_XPATH, value=user.email)
        self.log.debug("All fields were filled")
        sleep(1)
        # Click the button
        self.wait_and_click(By.XPATH, self.constants.SIGN_UP_BUTTON_XPATH)

        # return username, email, password
        return ProfilePage(self.driver)

    def verify_message(self, text):
        error_message = self.find_by_text(text)
        assert error_message.text == text
        self.log.debug("Error message")
