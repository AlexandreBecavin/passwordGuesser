from word import Word

class L33t(Word): 
    def __init__(self, _word):
        self._word = _word
        self._passwordsL33t = []
        self._dicoL33t = {
            "a": "4",
            "e": "3",
            "i": "1",
            "o": "0",
            "l": "1",
            "s": "5",
            "b": "8",
            "t": "7",
            "z": "2",
            "g": "6"
        }
        super().__init__(_word)
        self.getAllL33tWord()

     # getter setter _word
    def get_word(self):
         return self._word

    def set_word(self, word):
         self._word = word

    # getter  _passwordsL33t
    def get_passwords(self):
         return self._passwordsL33t

    def pushInArrayL33t(self, value):
        if not (value is None):
            self._passwordsL33t.append(value)

    def getAllL33tWord(self): 
        allWord = self._passwords
        for word in allWord:
            self.getL33tWord(word)

    # Methods
    def getL33tWord(self, word):
        CombinaisonsL33t = self.getAllCombinaisons(self.getAllIndex(word))
        for CombinaisonL33t in CombinaisonsL33t:
            if(CombinaisonL33t): 
                wordL33t = word
                for letterL33t in CombinaisonL33t: 
                    numberToReplace = self._dicoL33t[wordL33t[letterL33t]]
                    wordL33t = wordL33t[:letterL33t] + numberToReplace + wordL33t[letterL33t +1:]
                self.pushInArrayL33t(wordL33t)


    ## surcharge methode
    def getAllIndex(self, word): 
        ListIndicesByLetter = []
        finalIndicies = [] 
        for letterL33t in self._dicoL33t.keys(): 
            indices = [i for i, c in enumerate(word) if c == letterL33t]
            ListIndicesByLetter.append(indices)

        for indices in ListIndicesByLetter:
            finalIndicies += indices

        return finalIndicies

    def getAllCombinaisons(self, indexes):
        if len(indexes) == 0:
            return [[]]
        cs = []
        for c in self.getAllCombinaisons(indexes[1:]):
            cs += [c, c+[indexes[0]]]
        return cs

# l33t = L33t('Alexandre')
# print(l33t._passwordsL33t)
