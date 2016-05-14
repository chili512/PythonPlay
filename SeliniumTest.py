import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

try:
    browser = webdriver.Firefox()
    browser.get("http://www.smartrack.rct.net.au")
    assert "Welcome to Smartrack Fleet Management" in browser.title
    username = browser.find_element_by_name("Username")
    username.send_keys("username")
    password = browser.find_element_by_name("Password")
    password.send_keys("password")
    button = browser.find_element_by_xpath("//*[@id=\"form\"]//input[@type=\"submit\"]")
    button.send_keys(Keys.RETURN)
    time.sleep(10.2)

except NoSuchElementException:
    print("An exception occured")
finally:
    browser.close()
