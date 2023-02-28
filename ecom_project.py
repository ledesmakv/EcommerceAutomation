import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Webdriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Open URL and maximize window
driver.get('http://www.tutorialsninja.com/demo/')
driver.maximize_window()

# Phone's button
phones = driver.find_element("xpath", '//a[text()="Phones & PDAs"]')
phones.click()

# iPhone
iphones = driver.find_element("xpath", '//a[text()="iPhone"]')
iphones.click()
time.sleep(1)

# First picture
first_pick = driver.find_element("xpath", '//ul[@class="thumbnails"]/li[1]')
first_pick.click()
time.sleep(2)

# Next picture
next_click = driver.find_element("xpath", '//button[@title="Next (Right arrow key)"]')

# We click five times on the arrow to get to the desired picture
for i in range(0, 5):
    next_click.click()
    time.sleep(2)

# Save screenshot
driver.save_screenshot('screenshot#' + str(random.randint(0, 101)) + '.png')

x_button = driver.find_element("xpath", '//button[@title="Close (Esc)"]')
x_button.click()
time.sleep(1)
