import time
from math import log, sin

from selenium import webdriver

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(3)
    browser.find_element_by_class_name("btn").click()
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    x = browser.find_element_by_id("input_value").text
    y = log(abs(12*sin(int(x))))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(y))
    browser.find_element_by_class_name("btn").click()
    print(browser.switch_to.alert.text.split(': ')[-1])

finally:
    time.sleep(5)
    browser.quit()