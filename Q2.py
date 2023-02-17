from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import TimeoutException 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait as wait
import time
from time import sleep
import os

print("Execution Started")
driver=webdriver.Chrome(executable_path="./chromedriver")
driver.maximize_window()
driver.get("file://"+os.getcwd()+"//Q2.html")
time.sleep(1)
# Click the Cancel Button
driver.find_element(By.CSS_SELECTOR, ".big.button[name='cancel']").click()
time.sleep(3)
driver.quit()

print("Execution Completed")
