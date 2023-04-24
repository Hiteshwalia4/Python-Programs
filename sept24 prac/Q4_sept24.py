def transpose(l):
    l=list(l)
    l2=[]
    l3=""
    i=0
    l2=[(chr(ord(x)+1)) if(x.isalpha()) else x for x in l]
    for i in l2:
        l3=l3+i
    print(l3)

l=input("Enter any sentence-  ")
transpose(l)
