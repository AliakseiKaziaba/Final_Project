from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from retry import retry

from base.base_class import Base


class Fujifilm_Page(Base):
    filter = "//span[@class='font_upper_md font-bold darken dotted']"
    sort_dropdown = "//div[@class='bx_filter_select_arrow']"
    sort_by_price_ASC = "//span[@class='sort_btn js-load-link  asc PRICE']"
    max_price_field = "//input[@id='MAX_SMART_FILTER_P1_MAX']"
    set_filter_button = "//button[@id='set_filter1']"
    suggestions_dropdown = "//div[@class=@class='bx_filter_parameters_box set active' and " \
                           "@data-property_id='408']/div[@class='bx_filter_block  '] /div[" \
                           "@class='bx_filter_parameters_box_container  '] /div[" \
                           "@class='bx_filter_select_container']/div[@class='bx_filter_select_block'] /div[" \
                           "@class='bx_filter_select_text']"
    free_delivery = "//label[@data-role='label_MAX_SMART_FILTER_408_1990796034']"
    menu = "//div[@class='filter-panel__view controls-view pull-right']/a[@class='controls-view__link controls-view__link--table muted js-load-link']"
    add_to_basket = "//span[@data-value='5500']"
    basket = "//div[@id='bx_3966226736_957_basket_actions']/a[@href='/basket/' and @data-item='957']"

    max_price = "10000"

    """Getters"""

    def get_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter)))

    def get_sort_dropdown(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sort_dropdown)))

    def get_sort_by_price_ASC(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sort_by_price_ASC)))

    def get_max_price_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.max_price_field)))

    def get_set_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.set_filter_button)))

    def get_suggestions_dropdown(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.suggestions_dropdown)))

    def get_free_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.free_delivery)))

    @retry(WebDriverException, tries=3, delay=0.3)
    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_add_to_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_basket)))

    def get_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket)))

    """Actions"""

    def click_get_filter(self):
        self.get_filter().click()
        print("Click filter")

    def click_sort_dropdown(self):
        self.get_sort_dropdown().click()
        print("Click sort dropdown")

    def click_sort_by_price_ASC(self):
        self.get_sort_by_price_ASC().click()
        print("Click sort by price AS")

    def set_max_price(self):
        self.get_max_price_field().send_keys(self.max_price)
        print("Click set max price")

    def set_filter(self):
        self.get_set_filter().click()
        print("Click set filter")

    def click_suggestions_dropdown(self):
        self.get_suggestions_dropdown().click()
        print("Click suggestions dropdown")

    def set_free_delivery(self):
        self.get_free_delivery().click()
        print("Click free delivery")

    def click_menu(self):
        self.get_menu().click()
        print("Click menu")

    def click_add_to_basket(self):
        self.get_add_to_basket().click()
        print("Click add to basket")

    def click_basket(self):
        self.get_basket().click()
        print("Click basket")

    """Methods"""

    def set_filter_1(self):
        self.click_get_filter()
        self.click_sort_dropdown()
        self.click_sort_by_price_ASC()
        self.set_max_price()
        self.click_suggestions_dropdown()
        self.set_free_delivery()
        self.set_filter()

    def select_25mm(self):
        self.get_current_url()
        self.click_menu()
        self.click_add_to_basket()
        self.click_basket()
