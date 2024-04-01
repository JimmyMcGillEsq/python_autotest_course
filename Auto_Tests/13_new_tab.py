from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def funk(x):
	return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
	link = 'http://suninjuly.github.io/redirect_accept.html'
	browser.get(link)

	button1 = browser.find_element(By.CSS_SELECTOR, 'button.trollface')
	button1.click()
	time.sleep(5)

	new_tub = browser.window_handles[1]
	browser.switch_to.window(new_tub)

	input_value = browser.find_element(By.CSS_SELECTOR, '#input_value')
	y = input_value.text
	result = funk(y)

	answer = browser.find_element(By.CSS_SELECTOR, '#answer')
	answer.send_keys(result)

	button2 = browser.find_element(By.CSS_SELECTOR, 'button')
	button2.click()

	time.sleep(10)
	browser.quit()

