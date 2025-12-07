try:
    a = float(input("Enter number: "))
    b = float(input("Enter division number: "))
    if b == 0:
        raise ZeroDivisionError("0 is not a division number")
        print("thanks you") # this line wont be print becoz raise will stop exceution after it
    else:
        result = a / b
        print(result)

except ValueError as e:
    print("Not a valid number.", e)

except Exception as e:
    print("Not a valid input.", e)




