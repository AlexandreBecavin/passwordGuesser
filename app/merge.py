from word import Word
from date import Date
from l33t import L33t
import re
from datetime import datetime

class Merge:
    def __init__(self, _entriesUser, _hasLeet, _hasSpecialChar):
        self._entriesUser = _entriesUser
        self._hasLeet = _hasLeet
        self._hasSpecialChar = _hasSpecialChar
        self._passwords = []
        self._listDatePasswords = []
        self._listWordPasswords = []
        self._specialChars = ['.', '$', '?', '!', '*']
        
        self.getAllElement()
        self.addpasswordInVariable()
        self.mergePassword()
         

    def pushInArray(self, value, array):
        if not (value is None):
            array.append(value)
       
    ## Methode
    def getAllElement(self):
        date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
        for entryUser in self._entriesUser: 
            if (date_pattern.match(entryUser)):
                date_object = datetime.strptime(entryUser, '%Y-%m-%d').date()
                date = Date(date_object)
                self.pushInArray(date.allPasswords(), self._listDatePasswords)
            else: 
                word = Word(entryUser)
                self.pushInArray(word.allPasswords(), self._listWordPasswords)
                if (self._hasLeet):
                    l33t = L33t(entryUser)
                    self.pushInArray(l33t.getAllL33tWord(), self._listWordPasswords)
    
    def mergePassword(self): 
        if (self._listDatePasswords and self._listWordPasswords):
            for wordPasswords in self._listWordPasswords:
                for wordPassword in wordPasswords: 
                    for datePasswords in self._listDatePasswords: 
                        for datePassword in datePasswords: 
                            for date in datePassword: 
                                self.pushInArray(wordPassword+str(date), self._passwords)
                                self.pushInArray(str(date)+wordPassword, self._passwords)
                                if(self._hasSpecialChar): 
                                    self.addSpecialChar(date, wordPassword)
    

    def addpasswordInVariable(self): 
        ## [[Alexandre, ALEXANDRE, alexandre], [Noé, NOÉ, noé]]
        ## should return [Alexandre, ALEXANDRE, alexandre, Noé, NOÉ, noé]
        for wordPasswords in self._listWordPasswords:
            for wordPassword in wordPasswords: 
                self.pushInArray(wordPassword, self._passwords)

        ## [[[5, 05, ... 1 element], ['5juin', 65, ... 2 element], [0520juin, 5juin2020, ...3 element]], ..other date]
        ## should return [5, 05, 5juin, 65, 0520juin, 5juin2020]
        for datePasswords in self._listDatePasswords: 
            for datePassword in datePasswords: 
                for date in datePassword: 
                    self.pushInArray(str(date), self._passwords)

    def addSpecialChar(self, date, word):
        for specialChar in self._specialChars: 
            self.pushInArray(str(date)+specialChar+word, self._passwords)
            self.pushInArray(str(date)+word+specialChar, self._passwords)
            self.pushInArray(specialChar+str(date)+word, self._passwords)


# merge = Merge(['Chien', '2023-03-05'], True, True)
# print(len(merge._passwords))