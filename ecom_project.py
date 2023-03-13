import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

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

# Close image
x_button = driver.find_element("xpath", '//button[@title="Close (Esc)"]')
x_button.click()
time.sleep(1)

# Click on quantity input
quantity_input = driver.find_element("xpath", '//input[@name="quantity"]')
quantity_input.click()
time.sleep(1)

# Clear Input text and insert number "2"
quantity_input.clear()
quantity_input.send_keys("2")
time.sleep(1)

# Find and click on Add to Cart button
add_to_cart_button = driver.find_element("xpath", '//button[@id="button-cart"]')
add_to_cart_button.click()
time.sleep(3)

# Find and hover on Laptops & Notebooks button
laptops_notebooks_button = driver.find_element("xpath", '//a[text()="Laptops & Notebooks"]')
action = ActionChains(driver)
action.move_to_element(laptops_notebooks_button).perform()
time.sleep(1)

# Click on Show All Laptops & Notebooks option
laptops_notebooks_option = driver.find_element("xpath", '//a[text()="Show All Laptops & Notebooks"]')
laptops_notebooks_option.click()
time.sleep(2)

# Find HP Laptop
hp_laptop = driver.find_element("xpath", '//a[text()="HP LP3065"]')
# Scroll down a little bit
hp_laptop.location_once_scrolled_into_view
# Click on the Laptop HP LP3065
hp_laptop.click()
time.sleep(1)

# Click on the Calendar icon
calendar = driver.find_element("xpath", '//i[@class="fa fa-calendar"]')
calendar.click()
time.sleep(1)

# Click on the Date Picker button
date_picker = driver.find_element("xpath", '//th[@class="picker-switch"]')
calendar_next_button = driver.find_element("xpath", '//th[@class="next"]')

# Click on the Next button until we get December 2022
while date_picker.text != "December 2022":
    calendar_next_button.click()

time.sleep(2)

# Day 31st
calendar_day = driver.find_element("xpath", '//td[text()="31"]')
calendar_day.click()
time.sleep(2)

# Click again on the Add to Cart button