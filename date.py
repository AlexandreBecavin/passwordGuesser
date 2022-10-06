import datetime

class Date:
    def __init__(self):
        self._date = None

    ## getter setter
    def get_word(self):
        return self._date

    def set_word(self, date):
        self._date = date

    ## Method
    def getOnlyDay(self):
        return self._date.day

    def getOnlyMonth(self):
        return self._date.month

    def getOnlyYear(self):
        return self._date.year
    
    def transformNumberToMonth(self):
        month = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
        

date = Date()
date._date = datetime.date(2020, 5, 17)
print(date.getOnlyDay())
print(date.getOnlyMonth())
print(date.getOnlyYear())

