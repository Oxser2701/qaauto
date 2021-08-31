import pytest

from conftest import BaseTest
from constant.login_page import LoginPageConstant
from helpers.base import UserData


class TestLoginPage(BaseTest):

    @pytest.fixture(scope="function")
    def registered_user(self, start_page, user):
        profile_page = start_page.register_user(user)
        profile_page.logout()

        return user

    def test_empty_fields_login(self, start_page, user):
        """
        - Open start page
        - Clear pass and login fields
        - Click on Sign In button
        - Verify error message
        """

        # Try to login using empty values in the username/password fields
        start_page.login(user)

        # Verify error message
        start_page.verify_message(text=LoginPageConstant.INVALID_LOGIN_MESSAGE_TEXT)
        self.log.info("Error message")

    def test_incorrect_values(self, start_page):
        """
        - Open start page
        - Enter incorrect values
        - Click on Sign In button
        - Verify error message
        """

        # Try to login using incorrect credentials
        user = UserData(username="user", password="pass1234567890")
        start_page.login(user)

        # Verify error message
        start_page.verify_message(text=LoginPageConstant.INVALID_LOGIN_MESSAGE_TEXT)
        self.log.info("Error message")

    def test_negative_register_username(self, start_page):
        """
        - Open page
        - Enter restricted symbols in the 'Username' field
        - Verify error message
        """

        # Try to register user using restricted symbols in the 'Username' field

        user = UserData(username="!@#$%%^^&&*%#")
        start_page.register_user(user)

        # Verify error message
        start_page.verify_message(text=LoginPageConstant.INCORRECT_USERNAME_MESSAGE_TEXT)
        self.log.info("Error message")

    def test_negative_register_mail(self, start_page):
        """
        - Open page
        - Enter incorrect e-mail (without "@")
        - Verify error message
        """

        # Try to register user using restricted e-mail (without "@")
        user = UserData(email="test.test.com")
        start_page.register_user(user)

        # Verify error message
        start_page.verify_message(text=LoginPageConstant.INCORRECT_EMAIL_MESSAGE_TEXT)
        self.log.info("Error message")

    def test_negative_register_pass(self, start_page):
        """
        - Open page
        - Enter incorrect Password
        - Verify error message
        """

        # Try to register user using incorrect password

        user = UserData(password="123")
        start_page.register_user(user)

        # Verify error message
        start_page.verify_message(text=LoginPageConstant.INCORRECT_PASSWORD_MESSAGE_TEXT)
        self.log.info("Error message")

    def test_negative_register_existing_mail(self, start_page):
        """
        - Open page
        - Enter existing e-mail
        - Verify error message
        """

        # Try to register user using existing e-mail

        user = UserData(email="test@test.com")
        start_page.register_user(user)

        # Verify error message
        start_page.verify_message(text=LoginPageConstant.EXISTING_EMAIL_TEXT)
        self.log.info("Error message")

    def test_negative_register_existing_name(self, start_page):
        """
        - Open page
        - Enter existing name
        - Verify error message
        """

        # Try to register user using existing username
        user = UserData(username="testuser")
        start_page.register_user(user)

        # Verify error message
        start_page.verify_message(text=LoginPageConstant.EXISTING_USERNAME_TEXT)
        self.log.info("Error message")

    def test_positive_register(self, start_page, user, logout):
        """
        - Open page
        - Enter values in the 'Username' field
        - Enter e-mail
        - Enter Password
        - Click the button
        - Verify successfully registration
        """
        # Register user
        # user = UserData(username=f"user{self.variety}",
        #                 email=f"user{self.variety}@mail.com",
        #                 password=f"Passw0rd{self.variety}")
        profile_page = start_page.register_user(user)

        # Verify successfully registration
        profile_page.verify_success_login(user.username)
        self.log.info("Success")

    def test_login(self, registered_user, start_page, logout):
        """
        - Open page
        - Enter correct values
        - Click the button
        - Verify, that the user logged in successfully
        """

        # Login as user

        profile_page = start_page.login(registered_user)

        # Verify, that the user logged in successfully
        profile_page.verify_success_login(registered_user.username)
        self.log.info("Success")
