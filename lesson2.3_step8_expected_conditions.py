from math import log, sin

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try:
    #browser.implicitly_wait(5)
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # говорим Selenium проверять в течение 12 секунд появление текста
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    browser.find_element_by_class_name("btn").click()

    # решаем математическую задачу
    browser.find_element_by_id("answer").send_keys(str(log(abs(12 * sin(int(browser.find_element_by_id("input_value").text))))))
    browser.find_element_by_class_name("form-group .btn").click()
    result = print(browser.switch_to.alert.text.split(': ')[-1])

finally:
    browser.quit()
