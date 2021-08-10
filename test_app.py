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

    def test_empty_fields_login(self, driver):
        """
        - Open start page
        - Clear pass and login fields
        - Click on Sign In button
        - Verify error message
        """
        # 1
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        sleep(0.2)
        self.log.info("Open Page")
        # 2
        username = driver.find_element_by_xpath(".//input[@placeholder='Username']")
        username.clear()
        password = driver.find_element_by_xpath(".//input[@placeholder='Password']")
        password.clear()
        sleep(0.2)
        self.log.info("Clear all fields")
        # 3
        click = driver.find_element_by_xpath(".//button[contains(text(), 'Sign In')]")
        click.click()
        sleep(0.2)
        self.log.info("Click on the button")
        # 4
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
        # 1
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        sleep(0.2)
        self.log.info("Open Page")
        # 2
        username = driver.find_element_by_xpath(".//input[@placeholder='Username']")
        username.clear()
        username.send_keys("user")
        password = driver.find_element_by_xpath(".//input[@placeholder='Password']")
        password.clear()
        password.send_keys("pass1234567890")
        sleep(0.2)
        self.log.info("Enter incorrect values")
        # 3
        click = driver.find_element_by_xpath(".//button[contains(text(), 'Sign In')]")
        click.click()
        sleep(0.2)
        self.log.info("Click on the button")
        # 4
        message = driver.find_element_by_xpath(".//div[contains(text(), 'Invalid username / password')]")
        assert message.text == 'Invalid username / password'
        sleep(0.2)
        self.log.info("Error message")

        """
        - Open page
        - Enter values in the 'Username' field
        - Enter e-mail
        - Enter Password
        - Click the button
        - Verify successfully registration
        """
        # 1

    def test_positive_register(self, driver):
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        sleep(0.2)
        self.log.info("Open Page")
        sleep(0.5)
        # 2
        reg_username = driver.find_element_by_xpath(".//div[@class='container py-md-5']//form[@action='/register']//input[@placeholder='Pick a username']")
        reg_username.clear()
        reg_username.send_keys("testuser")
        self.log.info("Enter Username")
        sleep(0.2)
        # 3
        reg_password = driver.find_element_by_xpath(".//div[@class='container py-md-5']//form[@action='/register']//input[@placeholder='Create a password']")
        reg_password.clear()
        reg_password.send_keys("123123123123")
        self.log.info("Enter a pass")
        sleep(0.2)
        # 4
        reg_mail = driver.find_element_by_xpath(".//div[@class='container py-md-5']//form[@action='/register']//input[@placeholder='you@example.com']")
        reg_mail.clear()
        reg_mail.send_keys("test2@test.com")
        self.log.info("Enter a mail")
        sleep(0.2)
        # 5
        reg_button = driver.find_element_by_xpath(".//div[@class='container py-md-5']//button[@type='submit']")
        reg_button.click()
        self.log.info("Submit")
        sleep(0.2)
        # 6
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/profile/testuser")
        sleep(0.2)
        self.log.info("Click on profile")
        profile_user = driver.find_element_by_xpath(".//div[@class ='container py-md-5 container--narrow']//h2[contains(text(), 'testuser')]")
        assert profile_user.text == 'testuser'
        sleep(0.5)

    def test_negative_register_username(self, driver):
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        sleep(0.5)
        self.log.info("Open Page")
        sleep(0.2)
        negative_username = driver.find_element_by_xpath(".//div[@class='container py-md-5']//form[@action='/register']//input[@placeholder='Pick a username']")
        negative_username.clear()
        negative_username.send_keys("@#$@^@&")
        sleep(1)
        self.log.info("Negative username values")
        message_1 = driver.find_element_by_xpath(".//div//div[contains(text(), 'Username can only contain letters and numbers.')]")
        assert message_1.text == "Username can only contain letters and numbers."
        self.log.info("Error message")
        sleep(0.5)

    def test_negative_register_mail(self, driver):
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        sleep(0.5)
        self.log.info("Open Page")
        sleep(0.2)
        negative_mail = driver.find_element_by_xpath(".//div[@class='container py-md-5']//form[@action='/register']//input[@placeholder='you@example.com']")
        negative_mail.clear()
        negative_mail.send_keys("asdfg.hss")
        sleep(1)
        self.log.info("Negative e-mail values")
        message_2 = driver.find_element_by_xpath(".//div//div[contains(text(), 'You must provide a valid email address.')]")
        assert message_2.text == "You must provide a valid email address."
        self.log.info("Error message")
        sleep(0.5)

    def test_negative_register_pass(self, driver):
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        sleep(0.5)
        self.log.info("Open Page")
        sleep(0.2)
        negative_password = driver.find_element_by_xpath(".//div[@class='container py-md-5']//form[@action='/register']//input[@placeholder='Create a password']")
        negative_password.clear()
        negative_password.send_keys("123")
        sleep(1)
        self.log.info("Negative password values")
        message_3 = driver.find_element_by_xpath(".//div//div[contains(text(), 'Password must be at least 12 characters.')]")
        assert message_3.text == "Password must be at least 12 characters."
        self.log.info("Error message")
        sleep(0.5)

    def test_negative_register_existing_mail(self, driver):
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        sleep(0.5)
        self.log.info("Open Page")
        sleep(0.2)
        negative_existing_mail = driver.find_element_by_xpath(".//div[@class='container py-md-5']//form[@action='/register']//input[@placeholder='you@example.com']")
        negative_existing_mail.clear()
        negative_existing_mail.send_keys("test@test.com")
        sleep(1)
        self.log.info("Enter existing email")
        message_4 = driver.find_element_by_xpath(".//div//div[contains(text(), 'That email is already being used.')]")
        assert message_4.text == "That email is already being used."
        self.log.info("Error message")
        sleep(0.5)

    def test_negative_register_existing_name(self, driver):
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        sleep(0.5)
        self.log.info("Open Page")
        sleep(0.2)
        negative_existing_name = driver.find_element_by_xpath(".//div[@class='container py-md-5']//form[@action='/register']//input[@placeholder='Pick a username']")
        negative_existing_name.clear()
        negative_existing_name.send_keys("testuser")
        sleep(1)
        self.log.info("Enter existing name")
        message_4 = driver.find_element_by_xpath(".//div//div[contains(text(), 'That username is already taken.')]")
        assert message_4.text == "That username is already taken."
        self.log.info("Error message")
        sleep(0.5)

    def test_positive_register_2(self, driver):
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        sleep(0.2)
        self.log.info("Open Page")
        sleep(0.5)
        # 2
        reg_username = driver.find_element_by_xpath(".//div[@class='container py-md-5']//form[@action='/register']//input[@placeholder='Pick a username']")
        reg_username.clear()
        reg_username.send_keys("testuser2")
        self.log.info("Enter Username")
        sleep(0.2)
        # 3
        reg_password = driver.find_element_by_xpath(".//div[@class='container py-md-5']//form[@action='/register']//input[@placeholder='Create a password']")
        reg_password.clear()
        reg_password.send_keys("123123123123")
        self.log.info("Enter a pass")
        sleep(0.2)
        # 4
        reg_mail = driver.find_element_by_xpath(".//div[@class='container py-md-5']//form[@action='/register']//input[@placeholder='you@example.com']")
        reg_mail.clear()
        reg_mail.send_keys("test3@test.com")
        self.log.info("Enter a mail")
        sleep(0.2)
        # 5
        reg_button = driver.find_element_by_xpath(".//div[@class='container py-md-5']//button[@type='submit']")
        reg_button.click()
        self.log.info("Submit")
        sleep(0.2)
        # 6
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/profile/testuser2")
        sleep(0.2)
        self.log.info("Click on profile")
        profile_user = driver.find_element_by_xpath(".//div[@class ='container py-md-5 container--narrow']//h2[contains(text(), 'testuser2')]")
        assert profile_user.text == 'testuser2'
        sleep(0.5)

    def test_login(self, driver):
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        sleep(0.2)
        self.log.info("Open Page")
        username = driver.find_element_by_xpath(".//input[@placeholder='Username']")
        username.clear()
        username.send_keys("testuser")
        password = driver.find_element_by_xpath(".//input[@placeholder='Password']")
        password.clear()
        password.send_keys("123123123123")
        sleep(0.2)
        self.log.info("Enter correct values")
        click = driver.find_element_by_xpath(".//button[contains(text(), 'Sign In')]")
        click.click()
        sleep(0.2)
        self.log.info("Click on the button")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/profile/testuser")
        sleep(0.2)
        self.log.info("Click on profile")
        profile_user = driver.find_element_by_xpath(".//div[@class ='container py-md-5 container--narrow']//h2[contains(text(), 'testuser')]")
        assert profile_user.text == 'testuser'
        sleep(0.5)
