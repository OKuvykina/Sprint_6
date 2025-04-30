import allure
import pytest
from tests.conftest import main_page
from data import Parameters
from locators.order_page_locators import OrderLocators
from pages.order_page import OrderPage


class TestOrderPage:

    @pytest.mark.parametrize(
        'locator, order_data',
        [
            (OrderLocators.BUTTON_ORDER_UP, Parameters.ORDER_DATA_1),
            (OrderLocators.BUTTON_ORDER_DOWN, Parameters.ORDER_DATA_2)

        ]
    )

    @allure.title('Тесты на создание заказа с разных кнопок и разными данными')
    @allure.description('Запускаем тест по кнопкам свехру и снизу с 2мя разными входыми данными'
                        ' и проверяем, что заказ успешно оформлен')
    def test_check_create_order(self, main_page, driver, locator, order_data):

        main_page.scroll_to_the_end_question(locator)
        main_page.click_to_element(locator)
        order_page = OrderPage(driver)
        order_page.set_order(order_data)
        assert 'Заказ оформлен' in order_page.check_order()



