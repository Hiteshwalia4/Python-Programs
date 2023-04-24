def diff(L1,L2):
    S=[]
    L = []
    l = []
    for i in L1:
        if i not in L:
            L.append(i)
    for j in L2:
        if j not in l:
            l.append(j)
            
    for i in L:
        if i not in l:
            S.append(i)
    print(S)
    
L1 = ['Prabhjeet','Singh']
L2 = ['Singh']

diff(L1,L2)
