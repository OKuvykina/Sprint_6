import allure
from locators.main_page_locators import MainLocators
from locators.traffic_page_locators import TrafficLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# класс страницы заказов
class TrafficPage(BasePage):

    @allure.step('переходим по кнопке заказа и нажимаем лого Яндекса')
    def click_to_logo_yandex(self):
        self.click_to_element(MainLocators.BUTTON_UP)
        self.click_to_element(TrafficLocators.LOGO_YANDEX)
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])
        (WebDriverWait(self.driver, 3).until(
            expected_conditions.presence_of_element_located(TrafficLocators.MAIN_DZEN)))


    @allure.step('переходим по кнопке заказа и нажимаем лого Самоката')
    def click_to_logo_scooter(self):
        self.click_to_element(MainLocators.BUTTON_UP)
        self.click_to_element(TrafficLocators.LOGO_SCOOTER)
        (WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(TrafficLocators.MAIN_TITLE)))