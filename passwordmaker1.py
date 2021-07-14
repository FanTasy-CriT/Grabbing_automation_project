import random
def password_maker(long):
    words1 = ["a","z","e","r","t","y","u","i","o","p","q","s","d","f","g","h","j","k","l","m","w","x","c","v","b","n"]
    words2 = ["A","Z","E","R","T","Y","U","I","O","P","Q","S","D","F","G","H","J","K","L","M","W","X","C","V","B","N"]
    words3 = ['0','1','2','3','4','5','6','7','8','9']
    words4 = ['~','#','{','[','|','.','?',';',':','!','§','/','.','ù','%','^','$','¨','£','`',']','}']
    strong_password = ''
    for i in range(long):
        chosen = 'words' + str(random.randint(1, 4))
        if chosen == 'words1':
            strong_password = strong_password + words1[random.randint(0, 25)]
        if chosen == 'words2':
            strong_password = strong_password + words2[random.randint(0, 25)]
        if chosen == 'words3':
            strong_password = strong_password + words3[random.randint(0, 9)]
        if chosen == 'words4':
            strong_password = strong_password + words4[random.randint(0, 21)]
    return strong_password