from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

with webdriver.Chrome() as browser:
	link = 'http://suninjuly.github.io/file_input.html'
	browser.get(link)

	input_first = browser.find_element(By.CSS_SELECTOR, 'div div :nth-child(2)')
	input_first.send_keys('Jimmy')
	input_last = browser.find_element(By.CSS_SELECTOR, 'div div :nth-child(4)')
	input_last.send_keys('McGill')
	input_mail = browser.find_element(By.CSS_SELECTOR, 'div div :nth-child(6)')
	input_mail.send_keys('abc@mail.org')

	upload = browser.find_element(By.CSS_SELECTOR, '#file')
	current_dir = os.path.abspath(os.path.dirname(__file__))
	
	file = os.path.join(current_dir, 'file.txt')
	
	upload.send_keys(file)

	button = browser.find_element(By.CSS_SELECTOR, 'button')
	button.click()

	time.sleep(10)
	browser.quit()