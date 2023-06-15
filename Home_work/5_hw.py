from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# поиск элемента
icon = driver.find_element(By.CSS_SELECTOR, '#user-name')
icon = driver.find_element(By.CSS_SELECTOR, '#password')
icon = driver.find_element(By.CSS_SELECTOR, '#login-button')

if icon is None:
    print('Элемент не найден')
else:
    print('Элементы найдены')