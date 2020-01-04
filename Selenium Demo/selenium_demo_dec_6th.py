from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://www.google.com"
browser = webdriver.Chrome()
browser.get(url)
print("Opening browser")
print("Hit "+url)
CSS_ELEMENT_SRCH_BOX = "input[type=text][name='q']"

try:
	#srch_box = browser.find_element_by_name("q")
	srch_box = browser.find_element_by_css_selector(CSS_ELEMENT_SRCH_BOX)
	srch_box.clear()
	srch_box.send_keys("linked in")
	srch_box.send_keys(Keys.RETURN)
	print("srching for linked in")
except Exception as e:
	print("Exception occures : {}".format(e))
	
browser.close()
print("Closing browser")
