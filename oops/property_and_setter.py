class Employee:
    name = "Parth Parmar"
    
    def showInfo(self):
        print(f"Employee name is {self.name}! His Salary is {self.salaryValue}")
    
    @property #this is nothing but a getter
    def salary(self):
        return self.salaryValue

    @salary.setter # this is nothing but a setter
    def salary(self, value):
        if value < 0:            
            self.salaryValue = 0
        else:
            self.salaryValue = value     
        

empl = Employee()
empl.salary = -500
empl.showInfo()