from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
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

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text, 'Text doesnt match' 
    # ожидание чтобы визуально оценить результаты прохождения скрипта

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()