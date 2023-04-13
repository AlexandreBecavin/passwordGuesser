# import required module
import unidecode

class Word:
    def __init__(self, _word):
        self._word = _word
        self._passwords = []
       
    # getter setter _word
    def get_word(self):
         return self._word

    def set_word(self, word):
         self._word = word

    # getter  _passwords
    def get_passwords(self):
         return self._passwords

    ## Methode
    def removeAccent(self):
        if(unidecode.unidecode(self._word) != self._word): 
            return unidecode.unidecode(self._word) 
        return None

    def toLowerCase(self, withoutAccent=None):
        if withoutAccent is None:
            return self._word.lower()
        return withoutAccent.lower()

    def toUpperCase(self, withoutAccent=None):
        if withoutAccent is None:
            return self._word.upper()
        return withoutAccent.upper()

    def toCapitalize(self, withoutAccent=None):
        if withoutAccent is None:
            return self._word.capitalize()
        return withoutAccent.capitalize()

    ## Concat Methode
    def concatLowerAccent(self):
        withoutAccent = self.removeAccent()
        if not (withoutAccent is None): 
            return self.toLowerCase(withoutAccent)
        return None

    def concatUpperAccent(self):
        withoutAccent = self.removeAccent()
        if not (withoutAccent is None): 
            return self.toUpperCase(withoutAccent)
        return None

    def concatCapitalizeAccent(self):
        withoutAccent = self.removeAccent()
        if not (withoutAccent is None): 
            return self.toCapitalize(withoutAccent)
        return None

    def pushInArray(self, value):
        if not (value is None):
            self._passwords.append(value)

    def allPasswords(self):
        self.pushInArray(self.removeAccent())
        self.pushInArray(self.toLowerCase())
        self.pushInArray(self.toUpperCase())
        self.pushInArray(self.toCapitalize())
        self.pushInArray(self.concatLowerAccent())
        self.pushInArray(self.concatUpperAccent())
        self.pushInArray(self.concatCapitalizeAccent())
        return self._passwords

    word = property(get_word, set_word) 
  

# word = Word('jbsjéééùùHBSVfb')
# print(word.allPasswords())