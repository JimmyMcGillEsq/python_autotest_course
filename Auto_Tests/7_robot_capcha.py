from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
	link = 'https://suninjuly.github.io/math.html'
	browser.get(link)
	x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
	x = x_element.text
	f = calc(x)    
	answer = browser.find_element(By.CSS_SELECTOR, '#answer')
	answer.send_keys(f)
	check = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
	check.click()
	radio = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
	radio.click()
	button = browser.find_element(By.CSS_SELECTOR, 'button')
	button.click()
	time.sleep(10)
	browser.quit()
