''' 
В данной задаче вам нужно с помощью роботов решить 
ту же математическую задачу, как и в прошлом задании.
Но теперь значение переменной х спрятано в "сундуке", 
точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.
'''


from selenium import webdriver
import time

link = "http://suninjuly.github.io/get_attribute.html"

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_tag_name("img")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
