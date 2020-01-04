

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# set webdriver path of web browser
browser = webdriver.Chrome(executable_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

website_URL = "https://www.google.com"
twitter_URL = "https://www.twitter.com"
browser.get(twitter_URL)

time.sleep(2)

browser.close()