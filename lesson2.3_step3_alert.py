import time
from math import log, sin

from selenium import webdriver

link1 = "http://suninjuly.github.io/alert_accept.html"
link2 = "https://stepik.org/lesson/184253/step/4?unit=158843"
try:
    browser = webdriver.Chrome()
    browser.get(link1)
    button = browser.find_element_by_class_name("btn")
    button.click()

    #alert = browser.switch_to.alert
    #alert.accept

    confirm = browser.switch_to.alert # confirm-окно
    confirm.accept() # согласие
    #confirm.dismiss() # отклонение

    #prompt = browser.switch_to.alert # модальное окно
    #prompt.send_keys("My answer")
    #prompt.accept()

    x = browser.find_element_by_id("input_value").text
    y = log(abs(12*sin(int(x))))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(y))
    browser.find_element_by_class_name("btn").click()
    result = print(browser.switch_to.alert.text.split(': ')[-1])

finally:
    time.sleep(5)
    browser.quit()