"""TODO: Make the generator save the passwords to a file, so that they can be more quickly accessed later"""


class Test:
    passwordDictionary = []
    charList = "abcdefghijklmnopqrstuwxkyz"
    #charlist2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self):
        self.generatePasswords()
        self.printPasswords()

    def generatePasswords(self):
        for current in range(8):
        #for current in range(6):
            self.passwordDictionary = [i for i in self.charList]
            for y in range(current):
                self.passwordDictionary = [current + i for i in self.charList for current in self.passwordDictionary]

    def printPasswords(self):
        file = open("tekst.txt", "w+")
        for i in self.passwordDictionary:
            file.write(i)+file.write("\n")
            print(i)


Test()