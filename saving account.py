from account_maker import account_creator
import random
import os
import time
from adressgenerator import adressgen
from fullnamegenerator import fullnamegen
from nicknamegenerator import nicknamegen
from passwordmaker1 import password_maker
from stem.control import Controller
from stem import Signal
import requests
database = open(r'C:\Users\Fantasy-CriT\Documents\project\accounts.txt', 'a')
database2 = open(r'C:\Users\Fantasy-CriT\Documents\project\accounts_details.txt',"a")
session = requests.session()
string =session.get('https://httpbin.org/ip').text
result1 =string[string.find('"',13)+1:string.find('"',15)]+ '\n'
print(result1)
session.proxies={'http':'socks5://127.0.0.1:9050',
                'https':'socks5://127.0.0.1:9050'}
i=120
temp =('{:04d}'.format(i))
number = str(temp)
phonenumber1= str(random.randint(10000000,99999999))
country1 = 'France' # might make it random later and enhace further
realname = str(fullnamegen())
adress1 = str(adressgen())
password= str(password_maker(15))
nickname1= str(nicknamegen())
with Controller.from_port(port = 9051) as controller:
    controller.authenticate(password = 'ghhmmss123*')
    controller.signal(Signal.NEWNYM)
    controller.close()
string =session.get('https://httpbin.org/ip').text
result2 =string[string.find('"',13)+1:string.find('"',15)]+ '\n'
print(result2)
if(result1!=result2):
    print('Your IP is protected')
account_creator(number,password,nickname1,realname,phonenumber1,country1,adress1)  
database2.write(f'\nNickname: {nickname1}\n')
database2.write(f'Real name: {realname}\n')
database2.write(f'Phone number: {phonenumber1}\n')
database2.write(f'Country: {country1}\n')
database2.write(f'Adress: {adress1}\n')
database2.write(f'Account number: {number}\n')
database2.write(f"Password: {password}\n")
database2.write('--------------------------------------------------------------------------------------------------------------------')
database.write(f'\naccount number: {number}\n')
database.write(f"password: {password}\n")
database.write('--------------------------------------------------------------------------------------------------------------------')
