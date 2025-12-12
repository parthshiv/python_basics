from functools import lru_cache
import time

@lru_cache(maxsize=None) #this line will make the function cachable
def factorial(n):    
    if n == 1:
        return 1    
    return factorial(n-1) * n

def mul(n):
    time.sleep(2)
    return n*n;
    
print("done for factorial(7)", factorial(7))# factorial for 7 will come from cached, it wont calculate again for 7


print("done for mul(7)", mul(7))
print("done for mul(7)", mul(5))
print("done for mul(7)", mul(6))
print("done for mul(7)", mul(7)) #if you observer, this line will run faster becoz it will not calculate again and prints from cached output before.





