from time import sleep

import pytest
from selenium import webdriver

from conftest import BaseTest


class TestLoginPage(BaseTest):

    @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome(executable_path=r"C:\Users\Sergey\PycharmProjects\QAAuto\drivers\chromedriver.exe")
        yield driver
        driver.close()

    @pytest.fixture(scope="function")
    def logout(self, driver):
        yield
        driver.find_element_by_xpath(".//button[contains(text(), 'Sign Out')]").click()
        sleep(0.5)

    @pytest.fixture(scope="function")
    def registration(self, driver):
        registered_user = self.register_user(driver)
        driver.find_element_by_xpath(".//button[contains(text(), 'Sign Out')]").click()
        sleep(0.5)
        return registered_user

    def register_user(self, driver):
        """Fill required fields"""
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        sleep(0.2)
        # Enter values in the 'Username' field
        username_value = f"Testuser{self.variety}"
        reg_username = driver.find_element_by_xpath(".//input[@placeholder='Pick a username']")
        reg_username.clear()
        reg_username.send_keys(username_value)
        sleep(2)
        # Enter Password
        password_value = f"Passw0rd{self.variety}"
        reg_password = driver.find_element_by_xpath(".//input[@placeholder='Create a password']")
        reg_password.clear()
        reg_password.send_keys(password_value)
        sleep(2)
        # Enter e-mail
        email_value = f"test{self.variety}@mail.com"
        reg_mail = driver.find_element_by_xpath(".//input[@placeholder='you@example.com']")
        reg_mail.clear()
        reg_mail.send_keys(email_value)
        sleep(2)
        # Click the button
        reg_button = driver.find_element_by_xpath(".//div[@class='container py-md-5']//button[@type='submit']")
        reg_button.click()
        sleep(0.2)
        self.log.info("User was successfully registered")

        return username_value, password_value, email_value

    def test_empty_fields_login(self, driver):
        """
        - Open start page
        - Clear pass and login fields
        - Click on Sign In button
        - Verify error message
        """

        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        sleep(0.2)
        self.log.info("Open Page")

        # Clear pass and login fields
        username = driver.find_element_by_xpath(".//input[@placeholder='Username']")
        username.clear()
        password = driver.find_element_by_xpath(".//input[@placeholder='Password']")
        password.clear()
        sleep(0.2)
        self.log.info("Clear all fields")

        # Click on Sign In button
        click = driver.find_element_by_xpath(".//button[contains(text(), 'Sign In')]")
        click.click()
        sleep(0.2)
        self.log.info("Click on the button")

        # Verify error message
        message = driver.find_element_by_xpath(".//div[contains(text(), 'Invalid username / password')]")
        assert message.text == 'Invalid username / password'
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
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        sleep(0.2)
        self.log.info("Open Page")

        # Enter incorrect values
        username = driver.find_element_by_xpath(".//input[@placeholder='Username']")
        username.clear()
        username.send_keys("user")
        password = driver.find_element_by_xpath(".//input[@placeholder='Password']")
        password.clear()
        password.send_keys("pass1234567890")
        sleep(0.2)
        self.log.info("Enter incorrect values")

        # Click on Sign In button
        click = driver.find_element_by_xpath(".//button[contains(text(), 'Sign In')]")
        click.click()
        sleep(0.2)
        self.log.info("Click on the button")

        # Verify error message
        message = driver.find_element_by_xpath(".//div[contains(text(), 'Invalid username / password')]")
        assert message.text == 'Invalid username / password'
        sleep(0.2)
        self.log.info("Error message")

    def test_positive_register(self, driver):
        """
        - Open page
        - Enter values in the 'Username' field
        - Enter e-mail
        - Enter Password
        - Click the button
        - Verify successfully registration
        """
        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        sleep(0.2)
        self.log.info("Open Page")
        sleep(0.5)

        # Enter values in the 'Username' field
        reg_username = driver.find_element_by_xpath(".//div[@class='container py-md-5']//form[@action='/register']//input[@placeholder='Pick a username']")
        reg_username.clear()
        reg_username.send_keys("testuser")
        self.log.info("Enter Username")
        sleep(0.2)

        # Enter Password
        reg_password = driver.find_element_by_xpath(".//div[@class='container py-md-5']//form[@action='/register']//input[@placeholder='Create a password']")
        reg_password.clear()
        reg_password.send_keys("123123123123")
        self.log.info("Enter a pass")
        sleep(0.2)

        # Enter e-mail
        reg_mail = driver.find_element_by_xpath(".//div[@class='container py-md-5']//form[@action='/register']//input[@placeholder='you@example.com']")
        reg_mail.clear()
        reg_mail.send_keys("test2@test.com")
        self.log.info("Enter a mail")
        sleep(0.2)

        # Click the button
        reg_button = driver.find_element_by_xpath(".//button[@type='submit']")
        reg_button.click()
        self.log.info("Submit")
        sleep(0.2)

        # Verify successfully registration
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/profile/testuser")
        sleep(0.2)
        self.log.info("Click on profile")
        profile_user = driver.find_element_by_xpath(".//div[@class ='container py-md-5 container--narrow']//h2[contains(text(), 'testuser')]")
        assert profile_user.text == 'testuser'
        sleep(0.5)

    def test_negative_register_username(self, driver):
        """
        - Open page
        - Enter restricted symbols in the 'Username' field
        - Verify error message
        """
        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        sleep(0.5)
        self.log.info("Open Page")
        sleep(0.2)

        # Enter restricted symbols in the 'Username' field
        negative_username = driver.find_element_by_xpath(".//input[@placeholder='Pick a username']")
        negative_username.clear()
        negative_username.send_keys("@#$@^@&")
        sleep(1)
        self.log.info("Negative username values")
        # Verify error message
        message_1 = driver.find_element_by_xpath(".//div//div[contains(text(), 'Username can only contain letters and numbers.')]")
        assert message_1.text == "Username can only contain letters and numbers."
        self.log.info("Error message")
        sleep(0.5)

    def test_negative_register_mail(self, driver):
        """
        - Open page
        - Enter incorrect e-mail (without "@")
        - Verify error message
        """

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        sleep(0.5)
        self.log.info("Open Page")
        sleep(0.2)

        # Enter incorrect e-mail (without "@")
        negative_mail = driver.find_element_by_xpath(".//input[@placeholder='you@example.com']")
        negative_mail.clear()
        negative_mail.send_keys("asdfg.hss")
        sleep(1)
        self.log.info("Negative e-mail values")

        # Verify error message
        message_2 = driver.find_element_by_xpath(".//div//div[contains(text(), 'You must provide a valid email address.')]")
        assert message_2.text == "You must provide a valid email address."
        self.log.info("Error message")
        sleep(0.5)

    def test_negative_register_pass(self, driver):
        """
        - Open page
        - Enter incorrect Password
        - Verify error message
        """

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        sleep(0.5)
        self.log.info("Open Page")
        sleep(0.2)
        # Enter incorrect Password
        negative_password = driver.find_element_by_xpath(".//input[@placeholder='Create a password']")
        negative_password.clear()
        negative_password.send_keys("123")
        sleep(1)
        self.log.info("Negative password values")

        # Verify error message
        message_3 = driver.find_element_by_xpath(".//div//div[contains(text(), 'Password must be at least 12 characters.')]")
        assert message_3.text == "Password must be at least 12 characters."
        self.log.info("Error message")
        sleep(0.5)

    def test_negative_register_existing_mail(self, driver):
        """
        - Open page
        - Enter existing e-mail
        - Verify error message
        """

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        sleep(0.5)
        self.log.info("Open Page")
        sleep(0.2)

        # Enter existing e-mail
        negative_existing_mail = driver.find_element_by_xpath(".//div[@class='container py-md-5']//form[@action='/register']//input[@placeholder='you@example.com']")
        negative_existing_mail.clear()
        negative_existing_mail.send_keys("test@test.com")
        sleep(1)
        self.log.info("Enter existing email")

        # Verify error message
        message_4 = driver.find_element_by_xpath(".//div//div[contains(text(), 'That email is already being used.')]")
        assert message_4.text == "That email is already being used."
        self.log.info("Error message")
        sleep(0.5)

    def test_negative_register_existing_name(self, driver):
        """
        - Open page
        - Enter existing name
        - Verify error message
        """

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        sleep(0.5)
        self.log.info("Open Page")
        sleep(0.2)

        # Enter existing name
        negative_existing_name = driver.find_element_by_xpath(".//div[@class='container py-md-5']//form[@action='/register']//input[@placeholder='Pick a username']")
        negative_existing_name.clear()
        negative_existing_name.send_keys("testuser")
        sleep(1)
        self.log.info("Enter existing name")

        # Verify error message
        message_4 = driver.find_element_by_xpath(".//div//div[contains(text(), 'That username is already taken.')]")
        assert message_4.text == "That username is already taken."
        self.log.info("Error message")
        sleep(0.5)

    def test_positive_register_2(self, driver, logout):
        username_value = self.register_user(driver)[0]
        self.log.info("User was registered")
        """
        - Open page
        - Enter values in the 'Username' field
        - Enter e-mail
        - Enter Password
        - Click the button
        - Verify successfully registration
        """
        # # Open page
        # driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # self.log.info("Open Page")
        # sleep(0.5)
        #
        # # Enter values in the 'Username' field
        # reg_username = driver.find_element_by_xpath(".//input[@placeholder='Pick a username']")
        # reg_username.clear()
        # reg_username.send_keys(f"Testuser{self.variety}")
        # self.log.info("Enter Username")
        # sleep(2)
        #
        # # Enter Password
        # reg_password = driver.find_element_by_xpath(".//input[@placeholder='Create a password']")
        # reg_password.clear()
        # reg_password.send_keys(f"Passw0rd{self.variety}")
        # self.log.info("Enter a pass")
        # sleep(2)
        #
        # # Enter e-mail
        # reg_mail = driver.find_element_by_xpath(".//input[@placeholder='you@example.com']")
        # reg_mail.clear()
        # reg_mail.send_keys(f"test{self.variety}@mail.com")
        # self.log.info("Enter a mail")
        # sleep(2)
        #
        # # Click the button
        # reg_button = driver.find_element_by_xpath(".//div[@class='container py-md-5']//button[@type='submit']")
        # reg_button.click()
        # self.log.info("Submit")
        # # sleep(0.2)
        # self.register_user(driver)
        # self.log.info("User was successfully registered")

        # Verify successfully registration
        hello_message = driver.find_element_by_xpath(".//h2")
        assert username_value.lower() in hello_message.text
        assert hello_message.text == f"Hello {username_value.lower()}, your feed is empty."
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
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        sleep(0.2)
        self.log.info("Open Page")

        username_value, _, password_value = registration

        # Enter correct values
        username = driver.find_element_by_xpath(".//input[@placeholder='Username']")
        username.clear()
        username.send_keys(username_value)
        password = driver.find_element_by_xpath(".//input[@placeholder='Password']")
        password.clear()
        password.send_keys(password_value)
        sleep(0.2)
        self.log.info("Enter correct values")

        # Click the button
        click = driver.find_element_by_xpath(".//button[contains(text(), 'Sign In')]")
        click.click()
        sleep(0.2)
        self.log.info("Click on the button")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/profile/testuser")
        sleep(0.2)

        # Verify, that the user logged in successfully
        hello_message = driver.find_element_by_xpath(".//h2")
        assert username_value.lower() in hello_message.text
        assert hello_message.text == f"Hello {username_value.lower()}, your feed is empty."
        assert driver.find_element_by_xpath(".//strong").text == username_value.lower()
        self.log.info("Success")
        sleep(0.5)
