from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    site = "http://suninjuly.github.io/huge_form.html"
    browser = webdriver.Chrome()
    browser.get(site)
    elements = browser.find_elements(By.CSS_SELECTOR, "input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()