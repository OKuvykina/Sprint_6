import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# класс с базовыми методами для всех страниц
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('скролл к последнему элементу')
    def scroll_to_the_end_question(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('находим элемент после загрузки страницы')
    def find_element_with_wait(self, locator):

        (WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locator)))
        return self.driver.find_element(*locator)

    @allure.step('клик по элементу')
    def click_to_element(self, locator):
        (WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(locator)))
        self.driver.find_element(*locator).click()

    @allure.step('ожидание')
    def wait_element(self, locator):
        (WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)))

    @allure.step('переходим по ссылке')
    def open_url(self, url):
        self.driver.get(url)

    @allure.step('заполняем элемент данными')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('получаем текст элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('распаковываем локатор')
    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return (method, locator)

    @allure.step('фокуссируем селениум на новой вкладке с ожиданием')
    def focus_on_the_tab(self, locator):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])
        (WebDriverWait(self.driver, 3).until(
            expected_conditions.presence_of_element_located(locator)))

