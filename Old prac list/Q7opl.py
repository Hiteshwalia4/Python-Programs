def fibonacci(n):
  """Shows fibonacci sequence till n terms"""  
  if n<=1:
     return n
  else:
     return(fibonacci(n-1) + fibonacci(n-2))
a=int(input("Enter number of terms- "))
print("Fibonacci series till",a,"terms is- ")
for i in range(a):
    print(fibonacci(i))
