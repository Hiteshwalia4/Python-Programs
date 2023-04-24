


val = input("Enter the digit : ")
v = list(val)
sum =0
for i in range(len(v)):
    v[i] = int(v[i])

r= len(v)-1

while r >=0:
    print(v[r] , end="")
    r-=1
    
for i in range(len(v)):
    sum+=v[i]
    
print("\nSum of digits : ", sum)
