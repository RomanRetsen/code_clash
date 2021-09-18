# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome("./chromedriver")
# driver.get(" https://www.facebook.com ")
#
# username = driver.find_element_by_id("email")
# password = driver.find_element_by_id("pass")
# username.clear()
# username.send_keys("rshyn2@gmail.com")
# password.clear()
# password.send_keys("Nikita123!@#Roman@")
# password.send_keys(Keys.RETURN)
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/usr/local/bin/chromedriver"
# driver = webdriver.Chrome(PATH)

# Deny Popup Notification
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("start-maximized")
driver: WebDriver = webdriver.Chrome(chrome_options=chrome_options, executable_path=PATH)

# open the webpage

driver.get("https://www.facebook.com")

# enter credentials

username = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")

# enter username and password

username.clear()
username.send_keys("email")
password.clear()
password.send_keys("password")
password.send_keys(Keys.RETURN)

# go to Profile and Photos
# All Images URL https://www.facebook.com/$link/photos_by

for i in ['photos_by']:
    driver.get("https://www.facebook.com/$link/" + i + "/")
    time.sleep(5)

    n_scrolls = 2
    for j in range(1, n_scrolls):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(5)

    anchors = driver.find_elements_by_tag_name('img')
    anchors = [a.get_attribute('href') for a in anchors]
    anchors = [a for a in anchors if str(a).startswith("https:www.//facebook.com/photo")]
    print(anchors)
