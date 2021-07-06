from random import choice
def adressgen():
    f = open(r'C:\Users\Fantasy-CriT\Documents\project\adresses.txt','r')
    return choice(f.readlines())
