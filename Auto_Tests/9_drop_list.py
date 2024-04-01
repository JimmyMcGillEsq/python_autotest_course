from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

with webdriver.Chrome() as browser:
	link = 'https://suninjuly.github.io/selects1.html'
	browser.get(link)

	num1 = browser.find_element(By.CSS_SELECTOR, '#num1')
	x = int(num1.text)

	print('num1 found')

	num2 = browser.find_element(By.CSS_SELECTOR, '#num2')
	y = int(num2.text)

	print('num2 found')

	result = str(x + y)

	print(result)

	select = Select(browser.find_element(By.CSS_SELECTOR, 'select'))
	select.select_by_visible_text(result)

	browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

	time.sleep(7)
	browser.quit()




