from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.Fujifilm_Page import Fujifilm_Page


class Basket_Page(Base):
    basket_name_lens_25mm = "//h2[@class='basket-item-info-name']/a[@class='basket-item-info-name-link']/span[\
            @data-entity='basket-item-name']"
    basket_price_lens_25mm = "//td[contains(@class, 'basket-items-list-item-price') and contains(@class, " \
                             "'basket-items-list-item-price-for-one')]/div[@class='basket-item-block-price']/div[" \
                             "@class='basket-item-price-current']/span[@class='basket-item-price-current-text']"

    """Getters"""

    def get_basket_name_lens_25mm(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.basket_name_lens_25mm)))

    def get_basket_price_lens_25mm(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH,
                                                                                    self.basket_price_lens_25mm)))

    """Methods"""

    def assert_values_25mm(self):
        self.get_current_url()
        # self.assert_values(self.get_basket_name_lens_25mm, Fujifilm_Page.get_name_lens_25mm)
        self.assert_word(self.get_basket_name_lens_25mm(), 'Объектив TTartisan 25 мм F2 APS-C для Fuji')
        self.assert_word(self.get_basket_price_lens_25mm(), "5 500 ₽")

