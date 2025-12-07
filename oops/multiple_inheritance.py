class Company:
    company = "TCS"
    def showCompany(self):
        print(f"Company name is {self.company}")

class Employee:
    name = "Parth"
    def showInfo(self):
        print(f"Employee name is {self.name}!")

# below is the example of 'multiple inheritance' class
class Programmer(Company, Employee): #inherit Company and Employee both classes
    language = "Python"
    def showLanguage(self):
        print(f"He is master in {self.language} language.")

employeeDetails = Programmer()
employeeDetails.showCompany()
employeeDetails.showInfo()
employeeDetails.showLanguage()


