def avg():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    num3 = int(input("Enter number 3: "))

    avg = (num1 + num2 + num3)/3
    print(avg)

# avg()

def greetings(name):
    #print("Good Morning,",name)
    return "Good Morning, "+ name;

v = greetings("Parth")
print(v)