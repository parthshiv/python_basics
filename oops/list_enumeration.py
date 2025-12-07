list = [5, 25, 50, 60]

index  = 0

for item in list:
    print(f"The {item} is at index {index}")
    index += 1;

# same of above we can do easily by using enumerate function 

for index, item in enumerate(list):
    print(f"The {item} is at index {index}")

