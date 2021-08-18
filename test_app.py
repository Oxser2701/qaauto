import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import BaseTest
from constant.base import BaseConstant
from constant.login_page import LoginPageConstant
from constant.profile_page import ProfilePage
from helpers.base import BaseHelpers
from helpers.login_page import LoginHelpers
from helpers.profile_page import ProfileHelpers


class TestLoginPage(BaseTest):

    @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome(executable_path=BaseConstant.DRIVER_PATH)
        yield driver
        # driver.implicitly_wait(5)
        driver.close()

    @pytest.fixture(scope="function")
    def logout(self, driver):
        yield
        base_helper = BaseHelpers(driver)
        base_helper.wait_and_click(locator_type=By.XPATH, locator=ProfilePage.SIGN_OUT_BUTTON_XPATH)
        # sleep(0.5)

    @pytest.fixture(scope="function")
    def registration(self, driver):
        login_helper = LoginHelpers(driver)
        base_helper = BaseHelpers(driver)
        registered_user = login_helper.register_user(username=f"user{self.variety}",
                                                     email=f"user{self.variety}@mail.com",
                                                     password=f"Passw0rd{self.variety}")
        base_helper.wait_and_click(locator_type=By.XPATH, locator=ProfilePage.SIGN_OUT_BUTTON_XPATH)

        return registered_user

    def test_empty_fields_login(self, driver):
        """
        - Open start page
        - Clear pass and login fields
        - Click on Sign In button
        - Verify error message
        """
        login_helper = LoginHelpers(driver)

        # Open start page
        driver.get(BaseConstant.START_PAGE_URL)
        self.log.info("Open Page")

        # Try to login using empty values in the username/password fields
        login_helper.login(username="", password="")

        # Verify error message
        login_helper.verify_message(text=LoginPageConstant.INVALID_LOGIN_MESSAGE_TEXT)
        self.log.info("Error message")

    def test_incorrect_values(self, driver):
        """
        - Open start page
        - Enter incorrect values
        - Click on Sign In button
        - Verify error message
        """
        login_helper = LoginHelpers(driver)

        # Open start page
        driver.get(BaseConstant.START_PAGE_URL)
        self.log.info("Open Page")

        # Try to login using incorrect credentials
        login_helper.login(username="user", password="pass1234567890")

        # Verify error message
        login_helper.verify_message(text=LoginPageConstant.INVALID_LOGIN_MESSAGE_TEXT)
        self.log.info("Error message")

    def test_negative_register_username(self, driver):
        """
        - Open page
        - Enter restricted symbols in the 'Username' field
        - Verify error message
        """
        # Open page
        driver.get(BaseConstant.START_PAGE_URL)
        self.log.info("Open Page")

        # Try to register user using restricted symbols in the 'Username' field
        login_helper = LoginHelpers(driver)
        login_helper.register_user(username="!@#$%%^^&&*%#", email="", password="")

        # Verify error message
        login_helper.verify_message(text=LoginPageConstant.INCORRECT_USERNAME_MESSAGE_TEXT)
        self.log.info("Error message")

    def test_negative_register_mail(self, driver):
        """
        - Open page
        - Enter incorrect e-mail (without "@")
        - Verify error message
        """

        # Open page
        driver.get(BaseConstant.START_PAGE_URL)
        self.log.info("Open Page")

        # Try to register user using restricted e-mail (without "@")
        login_helper = LoginHelpers(driver)
        login_helper.register_user(username="", email="test.test.com", password="")

        # Verify error message
        login_helper.verify_message(text=LoginPageConstant.INCORRECT_EMAIL_MESSAGE_TEXT)
        self.log.info("Error message")

    def test_negative_register_pass(self, driver):
        """
        - Open page
        - Enter incorrect Password
        - Verify error message
        """

        # Open page
        driver.get(BaseConstant.START_PAGE_URL)
        self.log.info("Open Page")

        # Try to register user using incorrect password
        login_helper = LoginHelpers(driver)
        login_helper.register_user(username="", email="", password="123")

        # Verify error message
        login_helper.verify_message(text=LoginPageConstant.INCORRECT_PASSWORD_MESSAGE_TEXT)
        self.log.info("Error message")

    def test_negative_register_existing_mail(self, driver):
        """
        - Open page
        - Enter existing e-mail
        - Verify error message
        """

        # Open page
        driver.get(BaseConstant.START_PAGE_URL)
        self.log.info("Open Page")

        # Try to register user using existing e-mail
        login_helper = LoginHelpers(driver)
        login_helper.register_user(username="", email="test@test.com", password="")

        # Verify error message
        login_helper.verify_message(text=LoginPageConstant.EXISTING_EMAIL_TEXT)
        self.log.info("Error message")

    def test_negative_register_existing_name(self, driver):
        """
        - Open page
        - Enter existing name
        - Verify error message
        """

        # Open page
        driver.get(BaseConstant.START_PAGE_URL)
        self.log.info("Open Page")
        login_helper = LoginHelpers(driver)

        # Try to register user using existing username
        login_helper.register_user(username="testuser", email="", password="")

        # Verify error message
        login_helper.verify_message(text=LoginPageConstant.EXISTING_USERNAME_TEXT)
        self.log.info("Error message")

    def test_positive_register(self, driver, logout):
        """
        - Open page
        - Enter values in the 'Username' field
        - Enter e-mail
        - Enter Password
        - Click the button
        - Verify successfully registration
        """
        # Register user
        login_helper = LoginHelpers(driver)
        profile_helper = ProfileHelpers(driver)
        username_value = login_helper.register_user(username=f"user{self.variety}", email=f"user{self.variety}@mail.com", password=f"Passw0rd{self.variety}")[0]

        # Verify successfully registration
        profile_helper.verify_success_login(username=username_value)
        self.log.info("Success")

    def test_login(self, registration, driver, logout):
        """
        - Open page
        - Enter correct values
        - Click the button
        - Verify, that the user logged in successfully
        """

        # Open page
        driver.get(BaseConstant.START_PAGE_URL)
        self.log.info("Open Page")

        username_value, _, password_value, = registration

        # Login as user
        login_helper = LoginHelpers(driver)
        profile_helper = ProfileHelpers(driver)
        login_helper.login(username=username_value, password=password_value)

        # Verify, that the user logged in successfully
        profile_helper.verify_success_login(username=username_value)
        self.log.info("Success")
