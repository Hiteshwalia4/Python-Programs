def sort_tup():
    list = []
    n = int(input("Enter number of elements in tuple- "))
    for i in range(n):
            a = (input("Enter 1st part of element(In char or str)-  "), int(input("Enter 2nd part of element(In int)-  ")))
            list.append(a)
    t=tuple(list)
    print("The tuple is- ",t)

    l1=list.copy()
    l=len(l1)
    for i in range(l):
        for j in range(l-i-1):
            if(l1[j][1] > l1[j+1][1]):
                b=l1[j]
                l1[j]=l1[j+1]
                l1[j+1]=b
    print("Sorted tuple on the basis of second int element is-  ",tuple(l1))

sort_tup()