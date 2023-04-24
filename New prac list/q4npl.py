n=int(input("Enter any number >=10- "))
a=set()
while(n>0):
    digit=n%10
    n=int(n/10)
    a.add(digit)

print("Digits of number are- ",a)
