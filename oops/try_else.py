try:
    a = int(input("Enter number: "))
    print(a)

except Exception as e:
    print("Not a valid num.", e)

else: # this will only execure if we got successfull from try, if not then else wont execute
    print("i am inside else")