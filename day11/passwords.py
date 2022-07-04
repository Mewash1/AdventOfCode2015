import string

def genPassword(oldPassword):
    currentPassword = list(oldPassword)
    for _ in range(10):
        print(currentPassword)
        i = len(currentPassword) - 1
        while i >= 0:
            if currentPassword[i] != 'z':
                currentPassword[i] = string.ascii_lowercase[string.ascii_lowercase.find(currentPassword[i])+1]
                break
            else:
                currentPassword[i] = 'a'
            i -= 1


genPassword("abcdefgz")
        