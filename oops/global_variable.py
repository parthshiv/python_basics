a = 50

def num():
    global a # this will change value of global variable a = 50 to a = 5 as below line
    a = 5
    print(a)

num() # this will print function's variable a = 5
print(a) #this will print global variable a = 50

# num() function should be called before print(a) then only you can see changed global variable value, if you can call it after print(a), it will still consider it as a = 50 before changed in function call


