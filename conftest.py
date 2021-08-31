import logging
import random

import pytest
from selenium import webdriver

from Pages.login_page import LoginPage
from Pages.profile_page import ProfilePage
from constant.base import BaseConstant
from helpers.base import UserData


def pytest_runtest_setup(item):
    item.cls.log = logging.getLogger(item.name)
    item.cls.variety = random.choice(range(100000, 999999))


class BaseTest:
    log = logging.getLogger(__name__)
    variety = random.choice(range(100000, 999999))


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome(executable_path=BaseConstant.DRIVER_PATH)
    yield driver
    driver.close()


@pytest.fixture(scope="function")
def start_page(driver):
    driver.get(BaseConstant.START_PAGE_URL)
    return LoginPage(driver)


@pytest.fixture(scope="function")
def logout(driver):
    yield
    ProfilePage(driver).logout()


@pytest.fixture(scope="function")
def user():
    variety = random.choice(range(100000, 999999))
    return UserData(username=f"user{variety}",
                    email=f"user{variety}@mail.com",
                    password=f"Passw0rd{variety}")
