def list_to_dict(n:"int", m:"int", l:"list of list"):
    d = {}
    j = 0
    for i in range(0,m):
        d[l[0][i]] = [l[k][j] for k in range(1,n)]
        j += 1
    print("\nDictionary is- ",d)


def input_list():

    l = []
    n = int(input("\nEnter no. of lists in the list- "))
    m = int(input("Enter no. of elements in sublist- "))
    for i in range(0,n):
        l2 = []
        print("Enter",m,"integers in sublist",i+1,"- ")
        for j in range(0,m):
            b = int(input("Enter element- "))
            l2.append(b)
        l.append(l2)
    list_to_dict(n,m,l)


input_list()    
