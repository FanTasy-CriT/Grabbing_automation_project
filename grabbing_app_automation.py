import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

database = open(r'C:\Users\Fantasy-CriT\Documents\project\accounts.txt', 'r')
database2 = open(r'C:\Users\Fantasy-CriT\Documents\project\accounts_details.txt',"r")
driver = webdriver.Firefox(executable_path=r'C:\Users\Fantasy-CriT\Documents\geckodriver.exe')
wait = WebDriverWait(driver,100)


def grabbing_account(user,password):
    driver.get("http://szt6688.com/index/user/login.html")
    code = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li[1]/input')
    code.click()
    code.send_keys(user)
    passwords = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li[2]/input')
    passwords.click()
    passwords.send_keys(password)
    button = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/button')
    button.click()
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="tanchuangClose"]'))).click()
    for i in range(6):
        wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="orderDetail"]/div/div/div[3]/div[2]'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="autoStart"]'))).click()
    # driver.switch_to_default_content()  for switching back to main frame
    driver.quit()
    os.system('cmd /k ipconfig /release')
    os.system('cmd /k ipconfig /renew')

#opening every account one by one  and using it inside of this function

for line in database:
    if 'account number: ' in line:
        number = line[line.find(" ",13):]
        line1 =database.readline()
        password =line1[line1.find(" ")+1:]
        grabbing_account(number,password)


