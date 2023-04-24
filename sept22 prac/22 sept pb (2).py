def sub_list(l1):
    sublist = [[]] 
    for i in range(len(l1) + 1):
        for j in range(i + 1, len(l1) + 1): 
            sub = l1[i:j] 
            sublist.append(sub) 
    return sublist

L=['X','Y']
print(sub_list(L)) 
