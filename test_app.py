from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import BaseTest
from constant.base import BaseConstant
from constant.login_page import LoginPageConstant
from constant.profile_page import ProfilePage
from helpers.base import BaseHelpers


class TestLoginPage(BaseTest):

    @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome(executable_path=BaseConstant.DRIVER_PATH)
        yield driver
        driver.close()

    @pytest.fixture(scope="function")
    def logout(self, driver):
        yield
        base_helper = BaseHelpers(driver)
        base_helper.find_by_text(ProfilePage.SIGN_OUT_BUTTON_TEXT, "button").click()
        sleep(0.5)

    @pytest.fixture(scope="function")
    def registration(self, driver):
        base_helper = BaseHelpers(driver)
        registered_user = self.register_user(driver)
        base_helper.find_by_text(ProfilePage.SIGN_OUT_BUTTON_TEXT, "button").click()

        sleep(0.5)
        return registered_user

    def register_user(self, driver):
        """Fill required fields"""
        base_helper = BaseHelpers(driver)

        # Open start page
        driver.get(BaseConstant.START_PAGE_URL)
        sleep(0.2)

        # Enter values in the 'Username' field
        username_value = f"Testuser{self.variety}"
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstant.SIGN_UP_USERNAME_XPATH, value=username_value)

        # Enter Password
        password_value = f"Passw0rd{self.variety}"
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstant.SIGN_UP_PASSWORD_XPATH, value=password_value)

        # Enter e-mail
        email_value = f"test{self.variety}@mail.com"
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstant.SIGN_UP_EMAIL_XPATH, value=email_value)
        sleep(1)

        # Click the button
        click = driver.find_element_by_xpath(LoginPageConstant.SIGN_UP_BUTTON_XPATH)
        click.click()
        sleep(2)
        self.log.info("User was successfully registered")

        return username_value, email_value, password_value

    def test_empty_fields_login(self, driver):
        """
        - Open start page
        - Clear pass and login fields
        - Click on Sign In button
        - Verify error message
        """

        # Open start page
        driver.get(BaseConstant.START_PAGE_URL)
        sleep(0.2)
        self.log.info("Open Page")

        # Clear pass and login fields
        base_helper = BaseHelpers(driver)
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstant.SIGN_IN_USERNAME_XPATH, value="")
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstant.SIGN_IN_PASSWORD_XPATH, value="")
        self.log.info("Clear all fields")

        # Click on Sign In button
        sign_in_button = base_helper.find_by_text(text=LoginPageConstant.SIGN_IN_BUTTON_TEXT, element_tag="button")
        sign_in_button.click()
        sleep(0.2)
        self.log.info("Click on the button")

        # Verify error message
        error_message = base_helper.find_by_text(text=LoginPageConstant.INVALID_LOGIN_MESSAGE_TEXT)
        assert error_message.text == LoginPageConstant.INVALID_LOGIN_MESSAGE_TEXT
        sleep(0.2)
        self.log.info("Error message")

    def test_incorrect_values(self, driver):
        """
        - Open start page
        - Enter incorrect values
        - Click on Sign In button
        - Verify error message
        """
        # Open start page
        driver.get(BaseConstant.START_PAGE_URL)
        sleep(0.2)
        self.log.info("Open Page")

        # Enter incorrect values
        base_helper = BaseHelpers(driver)
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstant.SIGN_IN_USERNAME_XPATH, value="user")
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstant.SIGN_IN_PASSWORD_XPATH, value="pass1234567890")

        self.log.info("Enter incorrect values")

        # Click on Sign In button
        sign_in_button = base_helper.find_by_text(text=LoginPageConstant.SIGN_IN_BUTTON_TEXT, element_tag="button")
        sign_in_button.click()
        self.log.info("Click on the button")

        # Verify error message
        error_message = base_helper.find_by_text(text=LoginPageConstant.INVALID_LOGIN_MESSAGE_TEXT)
        assert error_message.text == LoginPageConstant.INVALID_LOGIN_MESSAGE_TEXT
        sleep(0.2)
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

        # Enter restricted symbols in the 'Username' field
        base_helper = BaseHelpers(driver)
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstant.SIGN_UP_USERNAME_XPATH, value="@#$@^@&")
        sleep(1)
        self.log.info("Negative username values")
        # Verify error message
        message_1 = driver.find_element_by_xpath(LoginPageConstant.INCORRECT_USERNAME_MESSAGE_XPATH)
        assert message_1.text == LoginPageConstant.INCORRECT_USERNAME_MESSAGE_TEXT
        self.log.info("Error message")
        sleep(0.5)

    def test_negative_register_mail(self, driver):
        """
        - Open page
        - Enter incorrect e-mail (without "@")
        - Verify error message
        """

        # Open page
        driver.get(BaseConstant.START_PAGE_URL)
        self.log.info("Open Page")

        # Enter incorrect e-mail (without "@")
        base_helper = BaseHelpers(driver)
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstant.SIGN_UP_EMAIL_XPATH, value="asdfg.hss")
        sleep(1)
        self.log.info("Negative e-mail values")

        # Verify error message
        message_2 = driver.find_element_by_xpath(LoginPageConstant.INCORRECT_EMAIL_MESSAGE_XPATH)
        assert message_2.text == LoginPageConstant.INCORRECT_EMAIL_MESSAGE_TEXT
        self.log.info("Error message")
        sleep(0.5)

    def test_negative_register_pass(self, driver):
        """
        - Open page
        - Enter incorrect Password
        - Verify error message
        """

        # Open page
        driver.get(BaseConstant.START_PAGE_URL)
        self.log.info("Open Page")

        # Enter incorrect Password
        base_helper = BaseHelpers(driver)
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstant.SIGN_UP_PASSWORD_XPATH, value="123")
        sleep(1)
        self.log.info("Negative password values")

        # Verify error message
        message_3 = driver.find_element_by_xpath(LoginPageConstant.INCORRECT_PASSWORD_MESSAGE_XPATH)
        assert message_3.text == LoginPageConstant.INCORRECT_PASSWORD_MESSAGE_TEXT
        self.log.info("Error message")
        sleep(0.5)

    def test_negative_register_existing_mail(self, driver):
        """
        - Open page
        - Enter existing e-mail
        - Verify error message
        """

        # Open page
        driver.get(BaseConstant.START_PAGE_URL)
        self.log.info("Open Page")

        # Enter existing e-mail
        base_helper = BaseHelpers(driver)
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstant.SIGN_UP_EMAIL_XPATH, value="test@test.com")
        sleep(1)
        self.log.info("Enter existing email")

        # Verify error message
        message_4 = driver.find_element_by_xpath(LoginPageConstant.EXISTING_EMAIL_XPATH)
        assert message_4.text == LoginPageConstant.EXISTING_EMAIL_TEXT
        self.log.info("Error message")
        sleep(0.5)

    def test_negative_register_existing_name(self, driver):
        """
        - Open page
        - Enter existing name
        - Verify error message
        """

        # Open page
        driver.get(BaseConstant.START_PAGE_URL)
        self.log.info("Open Page")

        # Enter existing name
        base_helper = BaseHelpers(driver)
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstant.SIGN_UP_USERNAME_XPATH, value="testuser")
        sleep(1)
        self.log.info("Enter existing name")

        # Verify error message
        message_4 = driver.find_element_by_xpath(LoginPageConstant.EXISTING_USERNAME_XPATH)
        assert message_4.text == LoginPageConstant.EXISTING_USERNAME_TEXT
        self.log.info("Error message")
        sleep(0.5)

    def test_positive_register(self, driver, logout):
        username_value = self.register_user(driver)[0]
        sleep(2)
        """
        - Open page
        - Enter values in the 'Username' field
        - Enter e-mail
        - Enter Password
        - Click the button
        - Verify successfully registration
        """

        # Verify successfully registration
        hello_message = driver.find_element_by_xpath(ProfilePage.HELLO_MESSAGE_XPATH)
        assert username_value.lower() in hello_message.text
        assert hello_message.text == ProfilePage.HELLO_MESSAGE_TEXT.format(lower_username=username_value.lower())
        assert driver.find_element_by_xpath(ProfilePage.HELLO_MESSAGE_USERNAME_XPATH).text == username_value.lower()
        self.log.info("Success")
        sleep(0.5)

    def test_login(self, registration, driver, logout):
        """
        - Open page
        - Enter correct values
        - Click the button
        - Verify, that the user logged in successfully
        """

        # Open page
        driver.get(BaseConstant.START_PAGE_URL)
        sleep(0.2)
        self.log.info("Open Page")

        username_value, _, password_value, = registration

        # Enter correct values
        base_helper = BaseHelpers(driver)
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstant.SIGN_IN_USERNAME_XPATH, value=username_value)
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstant.SIGN_IN_PASSWORD_XPATH, value=password_value)
        sleep(2)

        self.log.info("Enter correct values")

        # Click the button
        sign_in_button = base_helper.find_by_text(text=LoginPageConstant.SIGN_IN_BUTTON_TEXT, element_tag="button")
        sign_in_button.click()
        sleep(1)
        self.log.info("Click on the button")

        # Verify, that the user logged in successfully
        hello_message = driver.find_element_by_xpath(ProfilePage.HELLO_MESSAGE_XPATH)
        assert username_value.lower() in hello_message.text
        assert hello_message.text == ProfilePage.HELLO_MESSAGE_TEXT.format(lower_username=username_value.lower())
        assert driver.find_element_by_xpath(ProfilePage.HELLO_MESSAGE_USERNAME_XPATH).text == username_value.lower()
        self.log.info("Success")
        sleep(0.5)
