try:
    a = int(input("Enter number: "))
    print(a)

except Exception as e:
    print("Not a valid num.", e)

finally: # this will anyway execute.
    print("i am inside else")

def sum():
    try:
        a = int(input("Enter number of function input: "))
        return a

    except Exception as e:
        print("Not a valid num.", e)

    finally: # this will anyway execute even if function has return
        print("i am inside else of function")

sum()