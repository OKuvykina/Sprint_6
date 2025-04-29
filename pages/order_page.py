import allure
from locators.order_page_locators import OrderLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

# класс страницы заказов
class OrderPage(BasePage):

    @allure.step('делаем заказ')
    def set_order(self, data):

        self.add_text_to_element(OrderLocators.NAME, data['name'])
        self.add_text_to_element(OrderLocators.SURNAME, data['surname'])
        self.add_text_to_element(OrderLocators.ADDRESS, data['address'])
        self.click_to_station(data['station'])
        self.add_text_to_element(OrderLocators.TELEPHONE, data['telephone'])

        self.click_to_element(OrderLocators.BUTTON_NEXT)

        self.add_text_to_element(OrderLocators.TIME, data['time'])
        self.find_element_with_wait(OrderLocators.TIME).send_keys(Keys.RETURN)
        self.click_to_element(OrderLocators.COLOUR_BLACK)
        self.add_text_to_element(OrderLocators.COMMENT, data['comment'])
        self.click_to_rental_period(data['period'])

        self.click_to_element(OrderLocators.BUTTON_ORDER)
        self.find_element_with_wait(OrderLocators.BUTTON_YES).click()

    @allure.step('проверяем создание заказа')
    def check_order(self):
        return self.get_text_from_element(OrderLocators.ORDER_SUCCESS)

    @allure.step('выбираем станцию')
    def click_to_station(self, station):
        self.click_to_element(OrderLocators.METRO)
        formatted_locator = self.format_locators(OrderLocators.STATION, station)
        self.scroll_to_the_end_question(OrderLocators.STATION_LOCATOR_TO_SCROLL)
        self.click_to_element(formatted_locator)
        (WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(OrderLocators.TELEPHONE)))

    def click_to_rental_period(self, period):
        self.click_to_element(OrderLocators.RENTAL_PERIOD)
        # self.click_to_element(OrderLocators.RENTAL_PERIOD_LOCATOR_TO_SCROLL)   то работает если передавать конкретное значение
        formatted_locator = self.format_locators(OrderLocators.CHECK_RENTAL_PERIOD, period)
        self.scroll_to_the_end_question(OrderLocators.RENTAL_PERIOD_LOCATOR_TO_SCROLL)
        self.click_to_element(formatted_locator)








