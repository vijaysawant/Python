from selenium import webdriver
url = "https://appstore.seagate.com/"
driver = webdriver.Chrome()
driver.get(url)
driver.implicite_wait(30)

username = driver.find_element_by_class_name("field CredentialTypeusername")


print("Opening browser")
print("Hit "+url)

driver.close()
print("closing browser")
