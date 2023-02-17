from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import TimeoutException 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait as wait
import time
from time import sleep
import os

def click_by_xpath(driver, path):
    try:
        driver.execute_script("document.getElementById('getResult').innerHTML='Waiting 10 seconds for user to click on Enable Button'")
        element = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path)))
        element.click()
        alert = driver.switch_to.alert
        assert 'I am an alert box!' in alert.text
        alert.accept()
    except TimeoutException:
        element = None
        return element


print("Execution Started")
driver=webdriver.Chrome(executable_path="./chromedriver")
driver.maximize_window()
driver.get("file://"+os.getcwd()+"//Q1.html")
driver.find_element(By.ID, "btnEnable").click()
time.sleep(1)
click_by_xpath(driver,"//*[@id='btnMain']")
time.sleep(1)
driver.find_element(By.ID, "btnDisable").click()
time.sleep(1)
click_by_xpath(driver,"//*[@id='btnMain']")
time.sleep(1)
driver.quit()

print("Execution Completed")
