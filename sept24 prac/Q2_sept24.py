def sublist(l,s1):
    k=0
    for x in s1:
        if x not in l:
            k=1
            break
        else:
            if(l.count(x)!=s1.count(x)):
                k=1
                break
    if k==1:
        print("It is not sublist of given list!!")
    else:
        print("It is a sublist")

l=[]
n=int(input("Enter number of elements in list-  "))
print("Enter elements of list-  ")
for i in range(n):
    a=input()
    l.append(a)
l2=[]
m=int(input("Enter number of elements in sublist-  "))
print("Enter elements of sublist-  ")
for i in range(m):
    v=input()
    l2.append(v)

sublist(l,l2)
