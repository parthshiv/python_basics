"""
Super method is a method by which you can inherit parent method's methods/attributes
"""
class Company:
    company = "TCS"
    location = "India"
    def showCompany(self):
        print(f"Company name is {self.company}")
    
    @staticmethod
    def companyDomain():
        print("TCS is an IT Company!")

class Employee(Company): #inherits Company class. Now Company becomes parent for this class
    name = "Parth"
    
    #loc = super().location  or super().companyDomain() --> if you write here (outside of function), this will return an error because super method must be called inside a method/function instead of at class level
    def showInfo(self):
        loc = super().location # this will work
        super().companyDomain() # this will work
        print(f"Employee name is {self.name}! He is working at {loc}")



employeeDetails = Employee() # this inherits Employee and Employee inherits Company
employeeDetails.showCompany()
employeeDetails.showInfo()



