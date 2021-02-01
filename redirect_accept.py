'''
Задание: переход на новую вкладку
В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.

Сценарий для реализации выглядит так:

Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
'''



from selenium import webdriver
import time

link = "http://suninjuly.github.io/redirect_accept.html"

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name("trollface.btn.btn-primary")
    button.click()


    new_window = browser.window_handles[1] # сначала определяем новое окно
    browser.switch_to.window(new_window) # потом на него переключаетесь

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_class_name("form-control")
    input1.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()




finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
