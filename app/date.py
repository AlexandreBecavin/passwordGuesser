import datetime

class Date:
    def __init__(self, date):
        self.__date = date
        self.__passwords = []
        self.__methods = [[self.getDay, self.getDayWithZero], [self.getMonth, self.transformNumberToMonth, self.getMonthWithZero], [self.getYear, self.getYearIn2Number]] 


    ## getter setter
    def get_word(self):
        return self.__date

    def set_word(self, date):
        self.__date = date

     # getter  _passwords
    def get_word(self):
         return self.__passwords

    ## Method
    def getDay(self):
        return self.__date.day

    def getDayWithZero(self):
        return self.addZeroToNumber(self.__date.day)

    def getMonth(self):
        return self.__date.month

    def getMonthWithZero(self):
        return self.addZeroToNumber(self.__date.month)

    def getYear(self):
        return self.__date.year

    def getYearIn2Number(self):
        year = self.__date.year
        return year % 100
    
    def transformNumberToMonth(self):
        listMonths = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
        month = listMonths[self.getMonth() - 1]
        return month

    def addZeroToNumber(self, number):
        if int(number) < 10: 
            return '0' + str(number)
        else: 
            return None

    def allPasswordsWithOneElement(self):
        password = []
        for i in range(3):
            for nameMethod in self.__methods[i] :
                if(nameMethod() is not None): 
                    password.append(str(nameMethod()))
        return password
    
    def allPasswordsWithTwoElement(self):
        password = []
        for i in range(3):
            if i + 1 < len(self.__methods) :
                secondMethod = self.__methods[i + 1]
            else :
                secondMethod = self.__methods[0]

            for nameMethod1 in self.__methods[i] :
                for nameMethod2 in secondMethod :
                    if (nameMethod1() is not None and nameMethod2() is not None):
                        password.append(str(nameMethod1()) + str(nameMethod2()))
                        password.append(str(nameMethod2()) + str(nameMethod1()))
        return password

    def allPasswordsWithThreeElement(self):
        password = []
        for i in range(3):
            if i + 1 < len(self.__methods) and i + 2 < len(self.__methods):
                secondMethod = self.__methods[i + 1]
                thirdMethod = self.__methods[i + 2]
            elif i + 1 < len(self.__methods) :
                secondMethod = self.__methods[i + 1]
                thirdMethod = self.__methods[0]
            else :
                secondMethod = self.__methods[0]
                thirdMethod = self.__methods[1]

            for nameMethod1 in self.__methods[i] :
                for nameMethod2 in secondMethod :
                    for nameMethod3 in thirdMethod :
                        if (nameMethod1() is not None and nameMethod2() is not None and nameMethod3() is not None):
                            password.append(str(nameMethod1()) + str(nameMethod2()) + str(nameMethod3()))
                            password.append(str(nameMethod2()) + str(nameMethod1()) + str(nameMethod3()))
        return password
        


    def pushInArray(self, value):
        if not (value is None):
            self.__passwords.append(value)

    def allPasswords(self):          
        self.pushInArray(self.allPasswordsWithOneElement())
        self.pushInArray(self.allPasswordsWithTwoElement())
        self.pushInArray(self.allPasswordsWithThreeElement())

        return self.__passwords
        

# date = Date(datetime.date(2020, 12, 12))
# print(date.allPasswords())
