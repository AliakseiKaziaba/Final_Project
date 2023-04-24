from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_Page(Base):
    base_url = "https://ttartisan.ru/"

    log_in = "//div[@class='wrap_icon inner-table-block1 person']"
    user_name = "//input[@name='USER_LOGIN']"
    password = "//input[@name='USER_PASSWORD']"
    login_button = "//button[@name='Login1']"
    success_auth = "//div[@class='notice__title switcher-title font-bold']"
    lens_fujifilm = "//li[contains(@class, 'full')]/a[contains(@href, '/store/obektivy_dlya_fujifilm/') and span[" \
                    "contains(text(), 'Объективы для Fujifilm')]]"
    main_word_fuji = "//div[@class='topic__heading']/h1[@id='pagetitle']"

    login_standart = "aleksejpetrov@gmail.com"
    password_all = "aleksejpetrov123"

    """Getters"""

    def get_log_in(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.log_in)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_success_auth(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.success_auth)))

    def get_lens_fujifilm(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.lens_fujifilm)))

    def get_main_word_fuji(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word_fuji)))

    """Actions"""

    def click_log_in(self):
        self.get_log_in().click()
        print("Click log in")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    def click_lens_fujifilm(self):
        self.get_lens_fujifilm().click()
        print("Click lens fujifilm")

    """Methods"""

    def authorization(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_log_in()
        self.input_user_name(self.login_standart)
        self.input_password(self.password_all)
        self.click_login_button()
        self.assert_word(self.get_success_auth(), 'Вы успешно авторизовались')

    def menu_lens_fujifilm(self):
        self.click_lens_fujifilm()
        self.assert_word(self.get_main_word_fuji(), 'Объективы для Fujifilm')
