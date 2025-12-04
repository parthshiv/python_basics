# for i in range(1, 6):
#     print(i)

# i = 6
# while i < 11:
#     print(i)
#     i += 1

inputStart  = int(input("enter the start number to print table From: "))
inputEnd  = int(input("enter the end number to print table To: "))
while inputStart <= inputEnd:
    for i in range(1, 11):
        print(f" {inputStart} X {i} = {inputStart * i}")
    else: 
        print("\n")
    
    inputStart += 1    
