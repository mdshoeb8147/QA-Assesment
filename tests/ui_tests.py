from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    #  Check website loads
    driver.get("https://www.iamdave.ai")
    time.sleep(3)
    
    # Check title contains "Dave"
    page_title = driver.title
    if "Dave" in page_title:
        print("Title is correct.")
    else:
        print("Title is incorrect.")
    
    # Look for logo
    try:
        logo = driver.find_element(By.TAG_NAME, "img")
        print("Logo  is present ")
    except:
        print("Logo  is present not found")
    
    #  Check for headings
    headings = driver.find_elements(By.TAG_NAME, "h1")
    if len(headings) > 0:
        print("Headings is present ")
    
    # Test 4: Look for buttons
    buttons = driver.find_elements(By.TAG_NAME, "button")
    links = driver.find_elements(By.TAG_NAME, "a")
    
    if len(buttons) > 0 or len(links) > 0:
        print(" Clickable elements is present ")
        
        if len(links) > 0:
            links[0].click()
            print("Clicked a link")
    

finally:

    time.sleep(2)
    driver.quit()