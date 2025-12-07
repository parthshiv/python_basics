def http_status(statusCode):
    match statusCode:
        case 200:
            return "OK"
        
        case 404:
            return "Not found"
        
        case _: # it is a default condition
            return "Unknown status"



print(http_status(4014))

def calculate(a, b, operator):
    match operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b
        case _:
            return "Invalid operator"


# calling function
result = calculate(10, 5, "+")
print("Result:", result)