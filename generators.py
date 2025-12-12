def squares(n):
    for i in range(n):
        yield i**2  # produces values one by one


# for loop over a generator → taking one slice at a time
for num in squares(100):
    print(num)

# for loop over a list → eating the whole pizza at once
for i in range(100):
        print(i**2)

# generators are 'lazy' in python. So its use is good to save memory. For loops are saving memory when iterations are more.       
