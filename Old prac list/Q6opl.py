def factorial(n):
 """Calculates factorial of a number"""
 if n==1:
    return n
 else:
    return n*factorial(n-1)
a=int(input("Enter a number- "))
if a<0:
 print("Invalid!!")
elif a==0:
 print("Factorial of 0 is 1")
else:
 print("Factorial of",a,"is",factorial(a))
