class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Number(self.num + other.num)
    
    def __sub__(self, other):
        return Number(self.num - other.num)
    
    def __mul__(self, other):
        return Number(self.num * other.num)
    
    def __truediv__(self, other):
        return Number(self.num / other.num)
    
    def __floordiv__(self, other):
        return Number(self.num // other.num)
    
    def __str__(self):
        return str(self.num)

n1 = Number(10.52)
n2 = Number(20.25)
n3 = Number(10)
n4 = Number(100)
result = (((n1 + n2) - n3) * n2) / n4
print(result) 

floorDiv = (((n1 + n2) - n3) * n2) // n4
print(floorDiv) #floorDiv is nothing but the roundOff of float number
