

def rem_tuple():
    n = int(input("Enter number of tuples- "))
    ls = []
    ls2 = []
    for i in range(n):
        n2 = int(input("Enter length of tuple-  "))
        for i in range(n2):
            el = input("Element "+str(i)+" -  ")
            if not el :
                el = None
            ls2.append(el)
        ls.append(tuple(ls2))
        ls2=[]
    f = 0
    print(ls)
    for t in ls:
        for i in t:
            if i:
                f = 1
        if f == 0:
            ls.remove(t)
        f = 0
    print(ls)

            
rem_tuple()
