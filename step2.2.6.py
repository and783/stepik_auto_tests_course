from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
     
    x_element = browser.find_element(By.ID, "input_value").text
    y = calc(x_element)

    
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    
    input2 = browser.find_element(By.ID, "robotCheckbox")
    input2.click()

    input3 = browser.find_element(By.ID, "robotsRule")
    input3.click()
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
