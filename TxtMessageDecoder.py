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
    numOfItems = 0

    for item in keyList:
        if word == item:
            print(word, "means", abbrDict[item])

        else:
            numOfItems = numOfItems + 1

    if numOfItems == len(keyList):
        print("Key word does not exist")


option = input("Input 1 to start searching, 0 to stop: ")

while int(option) == 1:
    key = input("Input an abbreviation: ")
    search(key)
    option = input("Input 1 to start searching, 0 to stop: ")

    


