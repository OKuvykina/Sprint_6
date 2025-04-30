import pytest
from selenium import webdriver
from data import Parameters
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture # открываем бразер, ждем выполнеия логики и закрываем
def driver():

    driver = webdriver.Firefox()
    driver.set_window_size(1521, 1000)

    yield driver
    driver.quit()

@pytest.fixture #заходим на главную страницу сайта
def main_page(driver):

    page = MainPage(driver)
    page.open_url(Parameters.URL_MAIN_PAGES)
    return page

@pytest.fixture #заходим на страницу заказа
def order_page(driver):
    page = OrderPage(driver)
    page.open_url(Parameters.URL_ORDER_PAGES)
    return page