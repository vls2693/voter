import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.kinopoisk.ru/")
time.sleep(1)
driver.find_element_by_class_name("header-fresh-user-partial-component__login-button").click()
time.sleep(1)
frame = driver.find_element_by_class_name('kp2-authapi-iframe')
driver.switch_to.frame(frame)
auth1 = driver.find_element_by_name('login').send_keys('ololo@mail.ru')
auth2 = driver.find_element_by_name('password').send_keys('ololo@mail.ru')
time.sleep(3)
driver.find_element_by_class_name('button__label').click()
time.sleep(2)
#driver.quit()