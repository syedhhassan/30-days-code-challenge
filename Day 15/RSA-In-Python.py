import math
m=int(input("Enter Plain text: ")) 

p = 11
q = 7
e = 3
n = p*q
 
def encrypt(me):
    en=math.pow(me,e)
    c=en%n
    print("Encrypted Message is: ",c)
    return c

print("Original Message is: ",m)
c=encrypt(m)