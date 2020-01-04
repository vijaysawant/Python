from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# create a new Firefox session
#driver = webdriver.Firefox()
driver = webdriver.Chrome()

driver.maximize_window()

# navigate to the application home page
#driver.get("http://www.google.com")
driver.get("https://10.30.9.245/dashboard")
driver.implicitly_wait(90)
time.sleep(10)
username = "qa@qa.com"
password = "Tomahawk6!"
print "page opened"
name_field= driver.find_elements_by_name("username")
pass_field= driver.find_elements_by_name("password")
print "got elements"
name_field.send_keys(username)
pass_field.send_keys(password)
print "entered user n password"
# get the search textbox
search_field = driver.find_element_by_id("lst-ib")
search_field.clear()

# enter search keyword and submit
search_field.send_keys("Selenium WebDriver Interview questions")
search_field.submit()

# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name  method
lists= driver.find_elements_by_class_name("_Rm")

# get the number of elements found
print ("Found " + str(len(lists)) + "searches:")

# iterate through each element and print the text that is
# name of the search

i=0
for listitem in lists:
   print (listitem)
   i=i+1
   if(i>10):
      break

# close the browser window
driver.quit()