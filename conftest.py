import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def set_up():
    print("Start test")
    # op = webdriver.ChromeOptions()
    # op.add_experimental_option("detach", True)
    # op.add_experimental_option('excludeSwitches', ['enable-logging'])
    # ser = Service('C:\\Users\\kazyaba.a\\Рабочее\\PycharmProjects\\python_selenium(not git)\\chromedriver.exe')
    # driver = webdriver.Chrome(service=ser, options=op)

    yield
    print("End test")
    # driver.quit()


@pytest.fixture(scope="module")
def set_group():
    print("Enter system")
    yield
    print("Exit system")
