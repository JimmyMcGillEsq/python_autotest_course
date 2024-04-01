from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
import time
import math

def funk(x):
    return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
	link = 'http://suninjuly.github.io/explicit_wait2.html'
	browser.get(link)

	price = wait(browser, 5).until(ec.text_to_be_present_in_element((By.CSS_SELECTOR,'#price'), '$100'))
	button = browser.find_element(By.CSS_SELECTOR, '#book')
	button.click()
	
	input_value = browser.find_element(By.CSS_SELECTOR, '#input_value')
	y = input_value.text
	result = funk(y)

	answer = browser.find_element(By.CSS_SELECTOR, '#answer')
	answer.send_keys(result)

	button2 = browser.find_element(By.CSS_SELECTOR, '#solve')
	button2.click()

	time.sleep(7)
	browser.quit()