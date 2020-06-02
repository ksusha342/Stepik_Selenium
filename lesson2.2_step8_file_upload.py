import os
import time

from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"

try:
    with open("test.txt", "w") as file:
        content = file.write("automationbypython")  # create test.txt file
    browser = webdriver.Chrome()
    browser.get(link)
    name = browser.find_element_by_css_selector('[name="firstname"]')
    name.send_keys("Ivan")
    lastname = browser.find_element_by_css_selector('[name="lastname"]')
    lastname.send_keys("Ivanov")
    email = browser.find_element_by_css_selector('[name="email"]')
    email.send_keys("Ivanov@ya.ru")
    file_upload = browser.find_element_by_css_selector('[name="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла
    file_upload.send_keys(file_path)
    browser.find_element_by_class_name("btn").click()

finally:
    time.sleep(5)
    browser.quit()