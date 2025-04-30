import allure
import pytest
from tests.conftest import main_page
from data import Parameters


class TestMainPage:

    @pytest.mark.parametrize(
        'number',
        [0,1,2,3,4,5,6,7]
    )

    @allure.title('Тесты на проверку ответов на вопросы')
    @allure.description('Запускаем тест с параметризацией, находим вопрос с определенным номером'
                        ' и проверяем, что текст ответа совпадает с исходными данными из файла data')
    def test_checking_responses (self, main_page, number):

        main_page.click_to_question(number)
        assert main_page.get_answer(number) == Parameters.ANSWERS[number]

