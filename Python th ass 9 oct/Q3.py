def sum67(l):
    t=0
    k=0
    for i in l:
        if i==6:
            k=6
        if k==6:
            while i!=7:
                break;
            if i==7:
                k=1
        else:
            t=t+1
    return t


list=[]
n=int(input("Enter no of elements in list- "))
for i in range(n):
    b=int(input("Enter number- "))
    list.append(b)

t=sum67(list)
print("Sum is- ",t)
