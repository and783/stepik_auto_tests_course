import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

@pytest.mark.parametrize('address', ["236895", "236896", "236897", "236898", "236899", "236903","236904","236905"])

def test_address(browser, address):
        link = f"https://stepik.org/lesson/{address}/step/1"
        browser.get(link)
        time.sleep(5)
        button1 = browser.find_element(By.ID, "ember458")
        button1.click()
        input1 = browser.find_element(By.ID, "id_login_email")
        input1.send_keys("andrei.mamedov@yandex.ru")
        input2 = browser.find_element(By.ID, "id_login_password")
        input2.send_keys("Trv453695")
        button2 = browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader")
        button2.click()
        time.sleep(10)
        
        try:
                decide_again = browser.find_element(By.CLASS_NAME, "again-btn.white")
                decide_again.click()
        except:
                print('Кнопка "решить снова" не найдена')
                
        time.sleep(5)
        input3 = browser.find_element(By.CSS_SELECTOR, "textarea")
        input3.click()
        time.sleep(5)
        answer = str(math.log(int(time.time())))
        time.sleep(5) 
        input3.send_keys(answer)
        button3 = browser.find_element(By.CLASS_NAME, "submit-submission")
        button3.click()
        time.sleep(7)
        result = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
        print(result)
        time.sleep(5)
        
      
        

