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
driver.get("file://"+os.getcwd()+"//Q3.html")
time.sleep(1)
# Wait for the specific button in the dialog
if(EC.element_to_be_clickable((By.ID,"btnSpecific"))):
    driver.execute_script("document.getElementById('getResult').innerHTML='The Specific Element is found'")
time.sleep(10)
driver.quit()

print("Execution Completed")
