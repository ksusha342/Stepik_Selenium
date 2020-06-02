from selenium.webdriver.support.ui import Select

from selenium import webdriver
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)
    summa = str(num1 + num2)
    select = Select(browser.find_element_by_xpath("//select"))
    select.select_by_value(summa)
    browser.find_element_by_class_name("btn").click()

finally:
    time.sleep(5)
    browser.quit()