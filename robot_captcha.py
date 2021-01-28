# кликаем по checkboxes и radiobuttons (капча для роботов)


from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_class_name("form-control")
    input1.send_keys(y)

    option1 = browser.find_element_by_class_name("form-check-label")
    option1.click()
    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
