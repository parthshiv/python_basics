"""
Multi-level inheritance classes means a child class becomes parent class of another class.
i.e 
Class A is parent class 
Class B is child class of A, 
Class C is child of B (which is already Child of A but now becomes parent of C)
"""
class Company:
    company = "TCS"
    def showCompany(self):
        print(f"Company name is {self.company}")

class Employee(Company): #inherits Company class. Now Company becomes parent for this class
    name = "Parth"
    def showInfo(self):
        print(f"Employee name is {self.name}!")


class Programmer(Employee): #inherit Employee class. Now Employee becomes parent for this class
    language = "Python"
    def showLanguage(self):
        print(f"He is master in {self.language} language.")

print("Below inherits Company")
print("______________________")
employeeDetails = Employee() # this inherits Company 
employeeDetails.showCompany()
employeeDetails.showInfo()

print("Below inherits Employee and Employee inherits Company")
print("______________________")
employeeDetails = Programmer() # this inherits Employee and Employee inherits Company
employeeDetails.showCompany()
employeeDetails.showInfo()
employeeDetails.showLanguage()


