abbrDict = {
    "AKA":"also known as",
    "LOL":"laughing out loud",
    "BFF":"best friends forever",
    "IMHO":"in my humble opinion",
    "TMI":"too much information",
    "IDC":"I don't care",
    "IDK":"I don't know",
    "ILY":"I love you",
    "OMG":"oh my God",
}

def search(word):

    keyList = list(abbrDict.keys())

    for item in keyList:
        if word == item:
            print(word, "means", abbrDict[item])
        else:
            print("Key word does not exist")
            break

key = input("Input an abbreviation: ")
search(key)


