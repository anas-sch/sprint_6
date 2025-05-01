import pytest
import allure
from data import answers



@allure.title('Тесты на проверку вопросов')

class TestMainPage:

    @pytest.mark.parametrize("num", list(answers.keys()))

    def test_questions_and_answers (self, main_page, num):
        main_page.click_to_question(num)
        assert main_page.get_answer_text(num) == answers[num]
