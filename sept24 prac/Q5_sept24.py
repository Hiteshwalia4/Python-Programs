def eve_odd():
    list1 = []
    print("Enter no. of elements in list-  ")
    n = int(input())
    for i in range(n):
        a = int(input("Enter element no. " + str(i + 1) + " -  "))
        list1.append(a)
    print("The list entered is-  ", list1)
    print()

    a=[i*2 if i%2==0 else -i for i in list1]
    print("New modified list is-  ",a)


eve_odd()