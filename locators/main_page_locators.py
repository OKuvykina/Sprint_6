from selenium.webdriver.common.by import By


# локаторы главной страницы
class MainLocators:

    # кнопка Заказа сверху
    BUTTON_UP = (By.XPATH, "//*[contains(@class, 'Button_Button') and text()='Заказать']")
    # кнопка Заказа снизу
    BUTTON_DOWN = (By.XPATH, "//*[contains(@class, 'Button_Middle') and text()='Заказать']")
        #(By.XPATH, "//a[text()='Зарегистрироваться']")
    # #надпись "Вопросы о главном"
    # TITLE_QUESTIONS_ABOUT_MAIN = (By.XPATH, "//*[contains(@class, 'Home_SubHeader') and text()='Вопросы о важном']")
    #шаблон для всех вопросов
    QUESTIONS = (By.XPATH, '//*[@id="accordion__heading-{}"]')
    #шаблон для всех ответов
    ANSWERS = (By.XPATH, '//*[@id="accordion__panel-{}"]')
    #локатор последнего вопроса для скролла
    QUESTION_LOCATOR_TO_SCROLL = (By.XPATH, '//*[@id="accordion__heading-7"]')
