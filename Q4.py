from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import TimeoutException 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait as wait
import time
from time import sleep
import os
from selenium.webdriver.support.ui import Select

def click_dropdown(driver, dropdown_name, select_option):
    try:
        select = Select(driver.find_element_by_name(dropdown_name))
        select.select_by_value(select_option)
    except TimeoutException:
        element = None
        return element


print("Execution Started")
driver=webdriver.Chrome(executable_path="./chromedriver")
driver.maximize_window()
driver.get("file://"+os.getcwd()+"//Q4.html")
time.sleep(1)
# Click the Cancel Button
click_dropdown(driver,"Names","Beta")
time.sleep(2)
click_dropdown(driver,"Animals","Lion")
time.sleep(2)
click_dropdown(driver,"Cities","Delhi")
time.sleep(2)
driver.quit()

print("Execution Completed")
