import math

from selenium import webdriver
import time

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    value_x = int(browser.find_element_by_xpath('//*[@id="treasure"]').get_attribute("valuex"))
    input_value = browser.find_element_by_xpath('//*[@id="answer"]')
    input_value.send_keys(calc(value_x))
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(5)
    browser.quit()