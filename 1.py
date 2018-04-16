import time
from selenium import webdriver
import numpy
from selenium.webdriver.common.by import By

driver = webdriver.Firefox() #открываем браузер
driver.get("https://www.kinopoisk.ru/") #заходим на кинопоиск
'''
time.sleep(1) #ждём 1 секунду
driver.find_element_by_class_name("header-fresh-user-partial-component__login-button").click() #нажимаем кнопку войти
time.sleep(1) #ждём 1 секунду
frame = driver.find_element_by_class_name('kp2-authapi-iframe') #находим окно регистрации/аутентификации
driver.switch_to.frame(frame) #заходим в окно регистрации/аутентификации
auth1 = driver.find_element_by_name('login').send_keys('ololo@mail.ru') #вводим логин/почту
auth2 = driver.find_element_by_name('password').send_keys('ololo@mail.ru') #вводим пароль
time.sleep(3) #ждём 3 секунды
driver.find_element_by_class_name('button__label').click() #нажимаем кнопку войти
time.sleep(2) #ждём 2 секунды
#driver.quit() #завершаем работу
'''
#links = driver.find_element(By.CSS_SELECTOR, '#index_news > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
links = driver.find_elements_by_css_selector('#index_news > div:nth-child(1) > div:nth-child(1) > div:nth-child')
print(links)
links[2].click()
#index_news > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)
#index_news > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)