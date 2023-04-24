def Distinct():
    list=[]
    print("Enter no. of elements in list-  ")
    n=int(input())
    for i in range(n):
        a=int(input("Enter element no. "+ str(i+1)+" -  "))
        list.append(a)
    print("The list entered is-  ",list)

    l=[]
    start=int(input("Enter the starting index-  "))
    end=int(input("Enter the end index-  "))
    for i in range(start,end):
        if i not in list:
            l.append(i)
    print("Elements that are not present in list in range you have entered are-   ",l)

Distinct()