from selenium.webdriver.common.by import By


# локаторы главной страницы
class MainLocators:

    #шаблон для всех вопросов
    QUESTIONS = (By.XPATH, '//*[@id="accordion__heading-{}"]')
    #шаблон для всех ответов
    ANSWERS = (By.XPATH, '//*[@id="accordion__panel-{}"]')
    #локатор последнего вопроса для скролла
    QUESTION_LOCATOR_TO_SCROLL = (By.XPATH, '//*[@id="accordion__heading-7"]')
