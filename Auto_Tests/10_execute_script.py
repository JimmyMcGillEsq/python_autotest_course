from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def funk(x):
    return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
	link = 'https://SunInJuly.github.io/execute_script.html'
	browser.get(link)

	x_el = browser.find_element(By.CSS_SELECTOR, 'label span:nth-child(2)')
	x = x_el.text
	result = funk(x)

	answer = browser.find_element(By.CSS_SELECTOR, '#answer')
	answer.send_keys(result)

	check = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
	browser.execute_script("return arguments[0].scrollIntoView(true);", check)
	check.click()

	radio = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
	radio.click()

	button = browser.find_element(By.CSS_SELECTOR, 'button')
	button.click()

	time.sleep(10)
	browser.quit()

