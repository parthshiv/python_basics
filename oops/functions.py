class Employeee:
    department = "Account"
    role = "Accountant"

    # dunder/magic methods in python. the inbuilt methods starts/ends with __ (double underscore)    
    def __init__(self):
        self.name = "Shivansh"

    # if a function dont need any dynamic values and if we dont need to pass 'self' unneccessorily, then convert that method/function to @staticmethod in python, above the function declaration. 
        
    @staticmethod     
    def greet():
        print("Hello, Good Morning!")

    # in python, method needs to be declared with 'self'
    def getInfo(self): 
        print(f"My name is {self.name}. I am working in {self.department} department. My role is {self.role}.")
        
employee = Employeee()

# It is an instance attribute 
employee.name = "Parth" 

# this isntance attribute will overwrite class attribute because same name 
employee.role = "Software Engineer"

# print(employee.name, employee.department, employee.role)

employee.department = "IT" 
employee.greet()
employee.getInfo()
