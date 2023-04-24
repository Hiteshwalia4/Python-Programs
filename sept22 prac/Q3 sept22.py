def diff(x,y):
    l = []
    for ele in x:
        if not ele in y:
            l.append(ele)
    return l
x=list()
n1=int(input("Enter the size of the first List- "))

print("Enter the Element of first List- ")
for i in range(int(n1)):
   k=int(input(""))
   x.append(k)
y=list()
n2=int(input("Enter the size of the second List- "))
print("Enter the Element of second List- ")
for i in range(int(n2)):
   k=int(input(""))
   y.append(k)
print(diff(x, y)) 
