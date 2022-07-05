import string

def checkPassword(passwordList : list):
    password = ""
    for char in passwordList:
        password += char

    substringSet = set()
    checkSubstring = False
    checkOverlap = False
    countOverlap = 0
    for j in range(3,len(string.ascii_lowercase)+1):
        for i in range(len(string.ascii_lowercase) - j + 1):
            substringSet.add(string.ascii_lowercase[i:i+j])
    overlapSet = set()
    for char in string.ascii_lowercase:
        overlapSet.add(char+char)
    badLetters = set(['i', 'o', 'l'])

    for letter in badLetters:
        if letter in password:
            return False

    for substring in substringSet:
        if substring in password:
            checkSubstring = True
    
    if not checkSubstring:
        return False

    for overlap in overlapSet:
        if overlap in password:
            while len(overlap) <= len(password):
                overlap += overlap[0]
                if overlap in password:
                    checkOverlap = True
                    break
            if not checkOverlap:
                countOverlap += 1
                checkOverlap = False
    
    if countOverlap < 2:
        return False

    return True

def genPassword(oldPassword):
    currentPassword = list(oldPassword)
    while not checkPassword(currentPassword):
        i = len(currentPassword) - 1
        while i >= 0:
            if currentPassword[i] != 'z':
                currentPassword[i] = string.ascii_lowercase[string.ascii_lowercase.find(currentPassword[i])+1]
                break
            else:
                currentPassword[i] = 'a'
            i -= 1
        # print(currentPassword)
    return currentPassword

if __name__ == "__main__":
    password = genPassword("vzbxxzaa")
    newPassword = ""
    for char in password:
        newPassword += char
    print(newPassword)