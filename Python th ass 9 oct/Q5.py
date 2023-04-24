def arrlist(n:"int", l:"list"):
    l1 = []
    l2 = []
    for i in range(0,n):
        if(i%2 == 0):
            l2.append(l[i])
            l2.sort(reverse = True)
        else:
            l1.append(l[i])
            l1.sort()
    l = []
    j = 0
    k = 0
    for i in range(0,n):
        if(i%2 == 0):
            l.append(l2[j])
            j += 1
        else:
            l.append(l1[k])
            k += 1
    print("\nList is- ",l)


def input_list():
    n = int(input("Enter no. of elements in the list- "))
    l = []
    for j in range(0,n):
        el = int(input("Enter element- "))
        l.append(el)
    arrlist(n,l)

input_list()
