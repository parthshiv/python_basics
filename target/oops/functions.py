class Employeee:
    department = "IT"
    role = "Developer"

    def getInfo(self): # in python, method needs to be declared with 'self'
        print(f"Hello, My name is  {self.name}. I am working in {self.department} department. My role is {self.role}.")
        

employee = Employeee()
employee.name = "Parth" # It is an instance attribute 
employee.department = "Account" # this isntance attribute will overwrite class attribute because same name
# print(employee.name, employee.department, employee.role)
employee.getInfo()
