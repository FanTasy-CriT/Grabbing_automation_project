from random import choice
f = open(r'C:\Users\Fantasy-CriT\Documents\project\male_names.txt', 'r') 
f1 = open(r'C:\Users\Fantasy-CriT\Documents\project\surnames.txt','r')
def fullnamegen():
    name =choice(f.readlines())
    surname = choice(f1.readlines())
    result= name + surname
    result = result.replace('\n',' ')
    return result