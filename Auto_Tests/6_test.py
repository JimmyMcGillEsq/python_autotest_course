from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    link = 'https://suninjuly.github.io/registration2.html'
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_required = browser.find_elements(By.TAG_NAME, 'input')
    labels = browser.find_elements(By.TAG_NAME, 'label')
    index = 0
    for label in labels:
        if label.text[-1] == "*": 
            input_required[index].send_keys("required")
        index += 1
    print('Required fields filled')     

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    print('Form send')

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    print('Element found')

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text, 'Text doesnt match' 
    print('Element compared succesfully')
    
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()