import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:    
    link = 'https://suninjuly.github.io/explicit_wait2.html'
    
    browser = webdriver.Chrome()    
    browser.get(link)   

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )

    option3 = browser.find_element(By.ID, "book")  
    option3.click()

    browser.execute_script("window.scrollBy(0, 200);")

    num1 = browser.find_element(By.ID, "input_value")    
    x = num1.text   

    z = calc(x)
    print('func=', z)
    select = browser.find_element(By.ID, "answer")
    select.send_keys(z)

    option3 = browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button")  
    option3.click()

    time.sleep(15)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)

