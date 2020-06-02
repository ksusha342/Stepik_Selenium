import unittest
from selenium import webdriver


class TestSearchFields(unittest.TestCase):
    RESULT_TEXT = "Congratulations! You have successfully registered!"

    def test_link1_search_field(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.assertEqual(self.RESULT_TEXT, self.find_elements(link), 'Should be element, where selector is '
                                                                     '".first_block .second"')

    def test_link2_search_field(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.assertEqual(self.RESULT_TEXT, self.find_elements(link), 'Should be element, where selector is '
                                                                     '".first_block .second"')

    @staticmethod
    def find_elements(link):
        browser = webdriver.Chrome()
        browser.get(link)
        browser.implicitly_wait(2)
        browser.find_element_by_css_selector(".first_block .first").send_keys("Ivan")
        browser.find_element_by_css_selector(".first_block .second").send_keys("Ivanov")
        browser.find_element_by_css_selector(".first_block .third").send_keys("IvanovI@yandex.ru")
        browser.find_element_by_css_selector("button.btn").click()
        result = browser.find_element_by_tag_name("h1").text
        browser.quit()
        return result


if __name__ == "__main__":
    unittest.main()
