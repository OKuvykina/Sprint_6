import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainLocators


# класс главной страницы
class MainPage(BasePage):

    @allure.step('Клик на вопрос')
    def click_to_question(self, num):
        formatted_locator = self.format_locators(MainLocators.QUESTIONS, num)
        self.scroll_to_the_end_question(MainLocators.QUESTION_LOCATOR_TO_SCROLL)
        self.click_to_element(formatted_locator)

    @allure.step('получаем ответ')
    def get_answer(self, num):
        formatted_locator = self.format_locators(MainLocators.ANSWERS, num)
        return self.get_text_from_element(formatted_locator)





