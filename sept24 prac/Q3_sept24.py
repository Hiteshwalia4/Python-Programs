def permutaion(l):
    if len(l)==0:
        return []
    if len(l)==1:
        return [l]

    list1=[]
    for i in range(len(l)):
        m=l[i]
        remlist=l[:i] + l[i+1:]

        for p in permutaion(remlist):
            list1.append([m] + p)

    return list1

X=list()
n = int(input("Enter number of elements in list-  "))
print("Enter elements of List-  ")
for i in range(n):
    v = int(input())
    X.append(v)

for p in permutaion(X):
    print(p)