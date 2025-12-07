class Employee:
    name = "Parth"
    def showInfo(self):
        print(f"Employee name is {self.name}!")

#below is the example of 'single inheritance' class
class Programmer(Employee):
    language = "Python"
    def showLanguage(self):
        print(f"He is master in {self.language} language.")

employeeDetails = Programmer()
employeeDetails.showInfo()
employeeDetails.showLanguage()


