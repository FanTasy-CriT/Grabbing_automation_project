import random
names = open(r'C:\Users\Fantasy-CriT\Documents\project\male_names.txt', 'r')
def nicknamegen():
    content = names.readlines()
    nickname = content[random.randint(1, len(content))]
    result = nickname + str(random.randint(10, 9999)) #eliminate \n
    result = result.replace('\n',"")
    return result
