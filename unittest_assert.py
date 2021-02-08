'''
Попробуйте оформить тесты из первого модуля в стиле unittest.

Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
Создайте новый файл
Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
Запустите получившиеся тесты из файла 
Просмотрите отчёт о запуске и найдите последнюю строчку 
Отправьте эту строчку в качестве ответа на это задание 
'''




from selenium import webdriver
import time
import unittest


class Test_2pages(unittest.TestCase):
    def test_pages1(self):
        link1 = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link1)
        input1 = browser.find_element_by_xpath(
         "//input[@placeholder='Input your first name']")  # поиск по плейсхолдеру
        input1.send_keys("Iv")
        input2 = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
        input2.send_keys("Pe")
        input4 = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
        input4.send_keys("Rus")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(10)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
    def test_pages2(self):
        link1 = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link1)
        input1 = browser.find_element_by_xpath(
        "//input[@placeholder='Input your first name']")  # поиск по плейсхолдеру
        input1.send_keys("Iv")
        input2 = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
        input2.send_keys("Pe")
        input4 = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
        input4.send_keys("Rus")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(10)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()
