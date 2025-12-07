class Employee:
    name = "Parth"
    language = "Python"
    
    @classmethod
    def showInfo(cls): # class method use 'cls' as default argument
        print(f"My name from class attribute is {cls.name}")

    def showInfo2(self): # instane method use 'self' as default argument
        print(f"My name from instance attribute is {self.name}")
    
    def showLanguage(self):
        print(f"Language is an instance attribute {self.language}")


empl = Employee()
empl.name = "Shivansh Parmar"
empl.showInfo() # it will not show Shivansh as this is class method, it will use variable from class level
empl.showInfo2() # it will show Shivansh because its not class method but instance method
empl.showLanguage()
