import datetime


class Base():

    """Инициализация драйвера"""
    def __init__(self, driver):
        self.driver = driver

    """Получение текущего URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url: " + get_url)

    """Сравнение текущего URL с ожидаемым"""
    def assert_url(self, result_url):
        get_url = self.driver.current_url
        assert get_url == result_url
        print("Good current url")

    """Проверка значения текста на странице"""
    def assert_word(self, word, result_word):
        value_word = word.text
        print(value_word)
        assert value_word == result_word
        print("Good word's value")

    """Получение скриншота"""
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = "screenshot" + now_date + ".png"
        self.driver.save_screenshot('C:\\Users\\Tom\\PycharmProjects\\final_project\\screen\\' + name_screenshot)
