import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.kinopoisk.ru/")
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div/div/header/div/span/span/a[1]").click()
time.sleep(1)
frame = driver.find_element_by_class_name('kp2-authapi-iframe')
driver.switch_to.frame(frame)
auth1 = driver.find_element_by_name('login').send_keys('ololo@mail.ru')
auth2 = driver.find_element_by_name('password').send_keys('ololo@mail.ru')
driver.find_element_by_class_name('button button_type_action button_size_xxl button_block auth__signin i-bem button_js_inited').click()
time.sleep(2)
driver.quit()