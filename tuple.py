a = (1, 2, "Test", 3.5, "Hello", "Parth", "Test")
#print(type(a))
no = a.count("Test")
print(no) # prints number of occurance of the element in tuple 
index = a.index("Hello")
print(index) # prints index of the element in tuple 
print(a.__contains__("Hello1")) #checks whether the element availabe in tuple of not
print(len(a))

