import time
from selenium import webdriver
import numpy

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
links = driver.find_elements_by_class_name('item_link')
print(links[0])
print(links[1])
print(len(links))
x = numpy.random.choice(links)
print(x)
x.click()

