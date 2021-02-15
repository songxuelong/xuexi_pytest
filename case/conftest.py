from pages.login_page import LoginPage
from selenium import webdriver
import pytest
import time

@pytest.fixture(scope="session")
def driver(request):
    """定义全局driver fixture，给其它地方作参数调用"""
    _driver = webdriver.Chrome()
    # 窗口最大化
    _driver.maximize_window()


    def end():
        print("全部用例执行完后 teardown quit dirver")
        time.sleep(5)
        _driver.quit()

    request.addfinalizer(end)
    return _driver


@pytest.fixture(scope="session")
def login(driver):
    web = LoginPage(driver)
    web.login()
    return driver

