from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://10.30.9.245/dashboard")
print "opening page URL"
#driver.maximize_window()

User_Name = "qa@qa.com"
Passwd = "Tomahawk6!"

try:
	driver.implicitly_wait(30)

	search_field_username = driver.find_element_by_name("username")
	search_field_passwd = driver.find_element_by_name("password")

	search_field_username.send_keys(User_Name)
	search_field_passwd.send_keys(Passwd)
	search_field_passwd.submit()
	print "Login successful..!"


	#xpath_string = "//a[@class='item jv-configuration current-section']/span[@class='item-content']/i[@class='settings icon']"
	#new_xpath = "//div/a[@class='jv-configuration']"
	
	driver.implicitly_wait(30)
	#Search_conf_icon = driver.find_element_by_class_name("jv-configuration")
	#Search_conf_icon = driver.find_element_by_class_name("settings icon")
	#Search_conf_icon = driver.find_element_by_css_selector("i.settings icon")
	#Search_conf_icon = driver.find_element_by_xpath(new_xpath)
	Search_conf_icon = driver.find_element_by_link_text("Configuration")
	Search_conf_icon.click()
	print "Configuration icon selected."
	
	# Now find for Storage Tab
	search_storage_tab = driver.find_element_by_link_text("Storage")
	search_storage_tab.click()
	print "Storage tab selected"
	
	# find delete button
	Remove_Icon = driver.find_elements_by_xpath("//i[@title='Remove']")
	if len(Remove_Icon):
		Remove_Icon[0].click()
		print "Delete button click"
	else:
		print "Delete Button not found"
	time.sleep(10)

except Exception as e:
	print "Exception due to:",e
	
finally:
	
	driver.close()
	print "browser close"