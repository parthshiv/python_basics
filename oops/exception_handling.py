try:
    a = int(input("Enter number: "))
    print(a)

except Exception as e:
    print("Not a valid num.", e)