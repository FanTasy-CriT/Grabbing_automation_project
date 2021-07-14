import random
def nicknamegen():
    test = False
    while(test == False):
        names = open(r'C:\Users\Fantasy-CriT\Documents\project\male_names.txt', 'r')
        content = names.readlines()
        nickname = content[random.randint(1, len(content))-1]
        result = nickname + str(random.randint(10, 999)) #eliminate \n
        result = result.replace('\n',"")
        names.close()
        if(len(result)<=13):
            test = True
        return result