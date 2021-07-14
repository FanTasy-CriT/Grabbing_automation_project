from passwordmaker1 import password_maker
import random
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def account_creator(number, account_password,nickname1,realname,phonenumber1,country1,adress1):
    driver = webdriver.Firefox(executable_path=r'C:\Users\Fantasy-CriT\Documents\geckodriver.exe')
    wait = WebDriverWait(driver,100)
    wait1 = WebDriverWait(driver,20)
    driver.get('http://szt6688.com/index/user/register/invite_code/928174.html') #invite link
    nickname = driver.find_element_by_xpath('//*[@id="forgetpwd-form"]/ul/li[1]/input')
    nickname.click()
    nickname.send_keys(nickname1)
    account_number=driver.find_element_by_xpath('//*[@id="forgetpwd-form"]/ul/li[2]/input')
    account_number.click()
    account_number.send_keys(number)
    password = driver.find_element_by_xpath('//*[@id="forgetpwd-form"]/ul/li[3]/input')
    password.click()
    password.send_keys(account_password)
    password2 = driver.find_element_by_xpath('//*[@id="forgetpwd-form"]/ul/li[4]/input')
    password2.click()
    password2.send_keys(account_password)
    register_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/button')
    register_button.click()
    wait1.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[2]/ul/li[1]/input'))).click()
    loginnumber= driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li[1]/input')
    loginnumber.send_keys(number)
    loginpassword = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li[2]/input')
    loginpassword.send_keys(account_password)
    login = driver.find_element_by_xpath(('/html/body/div[1]/div/div[2]/div[1]/button'))
    login.click()
    wait1.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="tanchuangClose"]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/div[9]/ul/li[5]/div[1]')))
    my = driver.find_element_by_xpath('/html/body/div/div/div[9]/ul/li[5]/div[1]')
    my.click()
    wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/ul/li[1]/a/p'))).click()
    receivingadressbutton = driver.find_element_by_xpath('/html/body/div/div/ul/a[5]/li/h3')
    receivingadressbutton.click()
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/form/div/div[2]/ul[1]/li[1]/input')))
    realname1 = driver.find_element_by_xpath('/html/body/div/form/div/div[2]/ul[1]/li[1]/input')
    realname1.click()
    realname1.send_keys(realname) #real name generated here
    phonenumber = driver.find_element_by_xpath('/html/body/div/form/div/div[2]/ul[1]/li[2]/input')
    phonenumber.click()
    phonenumber.send_keys(phonenumber1)
    country = driver.find_element_by_xpath('/html/body/div/form/div/div[2]/ul[2]/li[1]/input')
    country.click()
    country.send_keys(country1) #make a generated number with probabilities of a higher to chance to be tunisia later
    adress = driver.find_element_by_xpath('/html/body/div/form/div/div[2]/ul[2]/li[2]/input')
    adress.click()
    adress.send_keys(adress1)# generated an adress 
    savebutton = driver.find_element_by_xpath('/html/body/div/form/div/p')
    savebutton.click()
    time.sleep(10)
