import logging

from selenium.webdriver.common.by import By

from constant.profile_page import ProfilePage
from helpers.base import BaseHelpers


class ProfileHelpers(BaseHelpers):
    """Profile page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.log = logging.getLogger(__name__)

    def verify_success_login(self, username):
        hello_message = self.wait_until_element_found(locator_type=By.XPATH, locator=ProfilePage.HELLO_MESSAGE_XPATH)
        assert username.lower() in hello_message.text
        assert hello_message.text == ProfilePage.HELLO_MESSAGE_TEXT.format(lower_username=username.lower())
        assert self.wait_until_element_found(locator_type=By.XPATH, locator=ProfilePage.HELLO_MESSAGE_USERNAME_XPATH).text == username.lower()
