def sort_list():
    list=[]
    n=int(input("Enter no. of elements in list-  "))
    print("Enter elements of list(only 0,1,2 in random order)-  ")
    for i in range(n):
        a=int(input())
        list.append(a)
    print("The list entered is-  ",list)
    list.sort()
    print("Sorted list is- ",list)

sort_list()