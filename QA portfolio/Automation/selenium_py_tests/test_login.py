from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://example.com/login')
driver.find_element(By.ID,'username').send_keys('test')
driver.find_element(By.ID,'password').send_keys('123456')
driver.find_element(By.ID,'login-button').click()
driver.quit()
