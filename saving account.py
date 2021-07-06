from account_maker import account_creator
import random
from adressgenerator import adressgen
from fullnamegenerator import fullnamegen
from nicknamegenerator import nicknamegen
from passwordmaker1 import password_maker
database = open(r'C:\Users\Fantasy-CriT\Documents\project\accounts.txt', 'a')
database2 = open(r'C:\Users\Fantasy-CriT\Documents\project\accounts_details.txt',"a")

for i in range(37,9999):
    temp =('{:04d}'.format(i))
    number = str(temp)
    phonenumber1= str(random.randint(10000000,99999999))
    country1 = 'France' # might make it random later and enhace further
    realname = str(fullnamegen())
    adress1 = str(adressgen())
    password= str(password_maker(15))
    nickname1= str(nicknamegen())
    """
    try:
        """
    account_creator(number,password,nickname1,realname,phonenumber1,country1,adress1)
    """
     finally:
        database2.write('\n')
        database2.write(f'Nickname: {nickname1}\n')
        database2.write(f'Real name: {realname}\n')
        database2.write(f'Phone number: {phonenumber1}\n')
        database2.write(f'Country: {country1}\n')
        database2.write(f'Adress: {adress1}\n')
        database2.write(f'Account number: {number}\n')
        database2.write(f"Password: {password}\n")
        database2.write('--------------------------------------------------------------------------------------------------------------------')
        database.write(f'account number: {number}\n')
        database.write(f"password: {password}\n")
        database.write('--------------------------------------------------------------------------------------------------------------------')
         """