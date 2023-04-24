s1 = int(input("Enter the length of side1: "))
s2 = int(input("Enter the length of side2: "))
s3 = int(input("Enter the length of side3: "))
import math
s = (s1+s2+s3)/2
area = float(math.sqrt(s*(s-s1)*(s-s2)*(s-s3)))
print("Area of Triangle: ",area)
cond = ((s1+s2)>s3)
print("Sum of any two side of triangle is greater than the third side :", bool(cond))
