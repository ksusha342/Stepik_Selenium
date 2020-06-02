import time
from math import log, sin

from selenium import webdriver


def calc(x):
    return log(abs(12 * sin(x)))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    value_x = int(browser.find_element_by_id("input_value").text)
    result = str(calc(value_x))
    input_result = browser.find_element_by_id("answer")
    input_result.send_keys(result)
    browser.find_element_by_css_selector('[for = "robotCheckbox"]').click()
    browser.execute_script("window.scrollBy(0, 120);")
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_tag_name("button").click()
    answer = browser.switch_to.alert.text
    print(answer.split()[-1])

finally:
    time.sleep(6)
    browser.quit()
