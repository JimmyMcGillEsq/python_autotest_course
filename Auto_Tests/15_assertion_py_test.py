import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link1 = 'https://suninjuly.github.io/registration1.html'
link2 = 'https://suninjuly.github.io/registration2.html'

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser")
    browser.quit()

# 1st test-case
def test_registration1(browser):
    browser.get(link1)

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
    
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    Ex_r = "Congratulations! You have successfully registered!"    

    assert Ex_r == welcome_text, "Text don't match expected one"
    print('Test1 successfully passed')
# 2nd test-case
def test_registration2(browser):
    
    browser.implicitly_wait(3)
    browser.get(link2)

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