import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.Main_Page import Main_Page
from pages.Fujifilm_Page import Fujifilm_Page


@pytest.mark.run(order=1)
def test_buy_product_1(set_up, set_group):
    op = webdriver.ChromeOptions()
    op.add_experimental_option("detach", True)
    op.add_experimental_option('excludeSwitches', ['enable-logging'])
    ser = Service('C:\\Users\\Tom\\PycharmProjects\\python_selenium\\chromedriver.exe')
    driver = webdriver.Chrome(service=ser, options=op)

    login = Main_Page(driver)
    login.authorization()
    login.menu_lens_fujifilm()

    filter = Fujifilm_Page(driver)
    filter.set_filter_1()
