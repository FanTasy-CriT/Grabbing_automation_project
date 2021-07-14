import random
def fullnamegen():
    f = open(r'C:\Users\Fantasy-CriT\Documents\project\male_names.txt', 'r') 
    f1 = open(r'C:\Users\Fantasy-CriT\Documents\project\surnames.txt','r')
    temp = f.readlines()
    name = temp[random.randint(0,len(temp))]
    temp = f1.readlines()
    surname = temp[random.randint(0,len(temp))]
    result= name + surname
    result = result.replace('\n',' ')
    f.close()
    f1.close()
    return result