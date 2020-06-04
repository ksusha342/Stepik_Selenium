import pytest
import time
import math

from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


class TestParametrize():
    @pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
                                      "https://stepik.org/lesson/236896/step/1",
                                      "https://stepik.org/lesson/236897/step/1",
                                      "https://stepik.org/lesson/236898/step/1",
                                      "https://stepik.org/lesson/236899/step/1",
                                      "https://stepik.org/lesson/236903/step/1",
                                      "https://stepik.org/lesson/236904/step/1",
                                      "https://stepik.org/lesson/236905/step/1"])
    def test_input_answer(self, browser, link):
        browser.get(link)
        browser.implicitly_wait(10)
        function_result = str(math.log(int(time.time())))
        browser.find_element_by_class_name("textarea").send_keys(function_result)
        browser.find_element_by_class_name("submit-submission").click()
        result_text = browser.find_element_by_class_name("smart-hints__feedback").text
        assert result_text == "Correct!", 'Should be text "Correct!"'