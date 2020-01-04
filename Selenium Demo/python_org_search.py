from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# instance of Firefox WebDriver is created.
driver = webdriver.Chrome()
driver.implicitly_wait(30)


driver.get("http://www.python.org")

srch_box = driver.find_element_by_name("q")
srch_box.clear()

srch_box.send_keys("pycon")
srch_box.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source

driver.quit()