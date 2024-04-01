from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
	link = 'https://suninjuly.github.io/get_attribute.html'
	browser.get(link)

	treasure = browser.find_element(By.CSS_SELECTOR, '#treasure')
	x = treasure.get_attribute('valuex')
	print(x)
	result = calc(x)

	answer = browser.find_element(By.CSS_SELECTOR, '#answer')
	answer.send_keys(result)

	check = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
	check.click()

	radio = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
	radio.click()

	button = browser.find_element(By.CSS_SELECTOR, 'button')
	button.click()

	time.sleep(10)
	browser.quit()