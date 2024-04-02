import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_registration1():
    with webdriver.Chrome() as browser:
        browser.implicitly_wait(3)
        link = 'https://suninjuly.github.io/registration1.html'
        browser.get(link)

        #Код, который заполняет обязательные поля
        first_name = browser.find_element(By.CSS_SELECTOR, 'div.first_block div.first_class input')
        first_name.send_keys('Jimmy')
        last_name = browser.find_element(By.CSS_SELECTOR, 'div.first_block div.second_class input')
        last_name.send_keys('McGill')
        mail = browser.find_element(By.CSS_SELECTOR, 'div.first_block div.third_class input')
        mail.send_keys('abc@hmail.org')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
            
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        Ex_r = "Congratulations! You have successfully registered!"    

        assert Ex_r == welcome_text, "Text don't match expected one"
        print('Test1 successfully passed')

def test_registration2():
    with webdriver.Chrome() as browser:
        browser.implicitly_wait(3)
        link = 'https://suninjuly.github.io/registration2.html'
        browser.get(link)

        #Код, который заполняет обязательные поля
        first_name = browser.find_element(By.CSS_SELECTOR, 'div.first_block div.first_class input')
        first_name.send_keys('Jimmy')
        last_name = browser.find_element(By.CSS_SELECTOR, 'div.first_block div.second_class input')
        last_name.send_keys('McGill')
        mail = browser.find_element(By.CSS_SELECTOR, 'div.first_block div.third_class input')
        mail.send_keys('abc@hmail.org')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
            
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        Ex_r = "Congratulations! You have successfully registered!"

        assert Ex_r == welcome_text, "Text don't match expected one"