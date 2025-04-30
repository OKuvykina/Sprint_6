# локаторы страницы заказов
from selenium.webdriver.common.by import By


class OrderLocators:

    # кнопка Заказа сверху
    BUTTON_ORDER_UP = (By.XPATH, "//*[contains(@class, 'Button_Button') and text()='Заказать']")
    # кнопка Заказа снизу
    BUTTON_ORDER_DOWN = (By.XPATH, "//*[contains(@class, 'Button_Middle') and text()='Заказать']")

    #первая форма заполнения
    # заголовок Для кого самокат
    TITLE_ON_ORDER_PAGE = (By.XPATH, "//*[contains(@class, 'Order_Header') and text()='Для кого самокат']")
    # поле для заполнения имени
    NAME = (By.XPATH, "//*[contains(@placeholder, '* Имя')]")
    #поле для заполнения фамилии
    SURNAME = (By.XPATH, "//*[contains(@placeholder, '* Фамилия')]")
    # поле для заполнения адреса
    ADDRESS = (By.XPATH, "//*[contains(@placeholder, '* Адрес: куда привезти заказ')]")
    #поле для заполнения станции метро
    METRO = (By.XPATH, "//*[contains(@placeholder, '* Станция метро')]")
    STATION = (By.XPATH, "//*[text()='{}']")
    STATION_LOCATOR_TO_SCROLL = (By.XPATH, "//*[text()='Лихоборы']")
    # поле для заполнения телефона
    TELEPHONE = (By.XPATH, "//*[contains(@placeholder, '* Телефон: на него позвонит курьер')]")
    BUTTON_NEXT = (By.XPATH, "//*[contains(@class, 'Button_Middle') and text()='Далее']")

    #вторая форма заполнения
    TIME = (By.XPATH, "//*[contains(@placeholder, '* Когда привезти самокат')]")

    #локаторы для заполнения из выпадающего списка период
    RENTAL_PERIOD = (By.XPATH, "//*[contains(@class, 'Dropdown-placeholder')]")
    CHECK_RENTAL_PERIOD = (By.XPATH, "//*[text()='{}']")
    RENTAL_PERIOD_LOCATOR_TO_SCROLL = (By.XPATH, "//*[text()='семеро суток']")

    #локатор чекбокса
    COLOUR_BLACK = (By.XPATH, "//*[contains(@id, 'black')]")

    COMMENT = (By.XPATH, "//*[contains(@placeholder, 'Комментарий для курьера')]")
    BUTTON_ORDER = (By.XPATH, "//*[contains(@class, 'Button_Middle') and text()='Заказать']")
    BUTTON_YES = (By.XPATH, "//*[contains(@class, 'Button_Middle') and text()='Да']")

    #форма "заказ создан"
    ORDER_SUCCESS = (By.XPATH, "//*[contains(@class, 'Order_ModalHeader') and text()='Заказ оформлен']")




