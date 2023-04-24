
n = int(input("Enter lines : "))

r=1
g=n-1

for j in range(1 , n+1):
    print()
    r=j
    for i in range(1, g+1):
        print(" ", end="")
    g = g-1
    for i in range(1 ,j+1):
        print(r , end="")
        r+=1
    r -= 2
    for i in range(1,j):
        print(r, end="")
        r -= 1

