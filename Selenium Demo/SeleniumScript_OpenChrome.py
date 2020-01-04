
from selenium import webdriver

#browser_URL = "C:\\Python27\\selenium\\webdriver\\Chrome\\chromedriver.exe"
#browser_URL = "C:\Program Files (x86)\Internet Explorer\iexplore.exe"
#browser_URL = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"

twitter_URL = "https://www.twitter.com"

browser = webdriver.Chrome()
#browser = webdriver.Ie(C:\\Program Files (x86)\\Internet Explorer\\iexplore.exe)
#browser = webdriver.Firefox(C:\\Program Files\\Mozilla Firefox\\firefox.exe)

#browser.set_page_load_timeout(20)

browser.get(twitter_URL)
browser.implicitly_wait(30)
browser.maximize_window()

srch_filed_user_name = browser.find_element_by_name("session[username_or_email]")
srch_filed_passwd = browser.find_element_by_name("session[password]")

#get password from file
fd = open("1.txt","r")
passwd = fd.read()
passwd.strip("\n")


srch_filed_user_name.send_keys("firstname.lastname@domain.com")
srch_filed_passwd.send_keys(passwd)

srch_filed_passwd.submit()
print "Logging successful..!"

user_setting = browser.find_element_by_id("user-dropdown-toggle")
user_setting.click()
print "Profile setting."

log_out_btn = browser.find_element_by_id("signout-button")
log_out_btn.click()
print "Log out."

#close file descriptor
fd.close()
