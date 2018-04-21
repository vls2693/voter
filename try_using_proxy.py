from selenium import webdriver
import time


"Define Both ProxyHost and ProxyPort as String"
ProxyHost = "36.67.142.53"
ProxyPort = "8080"



def ChangeProxy(ProxyHost ,ProxyPort):
    "Define Firefox Profile with you ProxyHost and ProxyPort"
    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", ProxyHost )
    profile.set_preference("network.proxy.http_port", int(ProxyPort))
    profile.update_preferences()
    return webdriver.Firefox(firefox_profile=profile)


def FixProxy():
    '"Reset Firefox Profile"'
    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 0)
    return webdriver.Firefox(firefox_profile=profile)


driver = ChangeProxy(ProxyHost ,ProxyPort)
driver.get("http://2ip.ru")

time.sleep(5)

driver = FixProxy()
driver.get("http://2ip.ru")