import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()

# open website
driver.get("https://www.saucedemo.com/")
time.sleep(2)

# LOGIN
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
time.sleep(2)

# verify login
title = driver.find_element(By.CLASS_NAME,"title").text
print("Page Title:", title)

# SORT PRODUCT
sort = Select(driver.find_element(By.CLASS_NAME,"product_sort_container"))
sort.select_by_visible_text("Price (low to high)")
time.sleep(2)

#  ADD PRODUCTS
driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()

# open cart
driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
time.sleep(5)

#  CHECKOUT
checkout_btn = driver.find_element(By.ID,"checkout")
checkout_btn.click()

driver.find_element(By.ID,"first-name").send_keys("Test")
driver.find_element(By.ID,"last-name").send_keys("User")
driver.find_element(By.ID,"postal-code").send_keys("560001")

driver.find_element(By.ID,"continue").click()
time.sleep(2)

driver.find_element(By.ID,"finish").click()

# verify order
msg = driver.find_element(By.CLASS_NAME,"complete-header").text
print("Message:", msg)

time.sleep(3)

#  LOGOUT
driver.find_element(By.ID,"react-burger-menu-btn").click()
time.sleep(2)
driver.find_element(By.ID,"logout_sidebar_link").click()
time.sleep(2)

#validation: check login page
login_button = driver.find_element(By.ID,"login-button")

if login_button.is_displayed():
    print("Logout successful - user returned to login page")
else:
    print("Logout failed")

