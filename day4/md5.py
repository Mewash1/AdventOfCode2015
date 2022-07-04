import hashlib

def generateMD5key(publicKey):
    i = 1
    while True:
        key = publicKey + str(i)
        md5 = hashlib.md5(key.encode('utf-8'))
        if md5.hexdigest()[0:6] == "000000":
            return i
        i += 1

if __name__ == "__main__":
    print(generateMD5key("bgvyzdsv"))