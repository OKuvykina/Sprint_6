import allure
from tests.conftest import main_page
from data import Parameters
from pages.traffic_page import TrafficPage
from locators.traffic_page_locators import TrafficLocators


class TestTrafficPage:

    @allure.title('Тест на переход по кнопке Яндекс на страницу Дзен')
    def test_traffic_dzen(self, main_page, driver):

        traffic_page = TrafficPage(driver)
        traffic_page.click_to_logo_yandex()
        dzen_current = traffic_page.find_element_with_wait(TrafficLocators.MAIN_DZEN).text
        assert dzen_current == 'Главная'

    @allure.title('Тест на переход по кнопке Самокат на главную страницу Самокат')
    def test_traffic_scooter(self, main_page, driver):

        traffic_page = TrafficPage(driver)
        traffic_page.click_to_logo_scooter()
        title_current = traffic_page.find_element_with_wait(TrafficLocators.MAIN_TITLE).text
        assert title_current == Parameters.TITLE_EXPECTED