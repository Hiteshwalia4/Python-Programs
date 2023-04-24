def Duplicates(L):
    L1 = []
    for i in L:
        if i not in L1:
            L1.append(i)
    print(L1)


L = ['Prabhjeet','Singh','Prabhjeet','Singh']
Duplicates(L)    
