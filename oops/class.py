class Employeee:
    department = "IT"
    role = "Developer"

employee = Employeee()
employee.name = "Parth" # It is an instance attribute 
employee.department = "Account" # this isntance attribute will overwrite class attribute because same name
print(employee.name, employee.department, employee.role)
