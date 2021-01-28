'''
Для этой задачи мы придумали еще один вариант капчи для роботов. Придется немного переобучить нашего робота, чтобы он справился с новым заданием.

Напишите код, который реализует следующий сценарий:

-Открыть страницу http://suninjuly.github.io/selects1.html
-Посчитать сумму заданных чисел
-Выбрать в выпадающем списке значение равное расчитанной сумме
-Нажать кнопку "Submit"
'''


from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"




try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = int(x_element.text)
    y_element = browser.find_element_by_id("num2")
    y = int(y_element.text) # чтобы вытащить текст 24 из строки <span class="nowrap" id="num1">24</span>
    sum = str(x+y)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(sum)

    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
