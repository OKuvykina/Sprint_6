import allure
from locators.traffic_page_locators import TrafficLocators
from pages.base_page import BasePage


# класс страницы заказов
class TrafficPage(BasePage):

    @allure.step('переходим по кнопке заказа и нажимаем лого Яндекса')
    def click_to_logo_yandex(self):
        self.click_to_element(TrafficLocators.BUTTON_UP)
        self.click_to_element(TrafficLocators.LOGO_YANDEX)
        self.focus_on_the_tab(TrafficLocators.MAIN_DZEN)
        return self.find_element_with_wait(TrafficLocators.MAIN_DZEN).text


    @allure.step('переходим по кнопке заказа и нажимаем лого Самоката')
    def click_to_logo_scooter(self):
        self.click_to_element(TrafficLocators.BUTTON_UP)
        self.click_to_element(TrafficLocators.LOGO_SCOOTER)
        self.wait_element(TrafficLocators.MAIN_TITLE)
        return self.find_element_with_wait(TrafficLocators.MAIN_TITLE).text