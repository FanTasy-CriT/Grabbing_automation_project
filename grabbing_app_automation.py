import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import switch_to
from stem.control import Controller
from stem import Signal
import requests
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

database = open(r'C:\Users\Fantasy-CriT\Documents\project\accounts.txt', 'r')
database2 = open(r'C:\Users\Fantasy-CriT\Documents\project\accounts_details.txt',"r")
driver = webdriver.Firefox(executable_path=r'C:\Users\Fantasy-CriT\Documents\geckodriver.exe')
wait = WebDriverWait(driver,100)

session = requests.session()
session.proxies= {'http':'socks5://127.0.0.1:9050','https':'socks5://127.0.0.1:9050'}
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
    grabbing = driver.find_element_by_xpath('/html/body/div/div/div[9]/ul/li[3]/div/img')
    grabbing.click()
    for i in range(10):
        wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="autoStart"]'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/div[3]/div/div/div[3]/div[2]")))
        submit = driver.find_element_by_xpath('/html/body/div/div/div[3]/div/div/div[3]/div[2]')
        submit.click()
    time.sleep(8)
    driver.quit()
#opening every account one by one  and using it inside of this function
for line in database:
        if 'account number: ' in line:
            string =session.get('https://httpbin.org/ip').text
        result1 =string[string.find('"',13)+1:string.find('"',15)]+ '\n'
        with Controller.from_port(port = 9051) as controller:
            controller.authenticate(password = 'ghhmmss123*')
            controller.signal(Signal.NEWNYM)
        string =session.get('https://httpbin.org/ip').text
        result2 =string[string.find('"',13)+1:string.find('"',15)]+ '\n'
        if(result1!=result2):
            print(result1)
            print(result2)
            print('Your IP is protected')
        number = line[line.find(" ",13):]
        line1 =database.readline()
        password =line1[line1.find(" ")+1:]
        grabbing_account(number,password)


