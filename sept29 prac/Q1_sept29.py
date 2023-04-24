t1=(1,2,5,7,9,2,4,6,8,10)
def Even_tuple():
    t=tuple([i for i in t1 if i%2==0])
    print("Tuple with even values- ",t)

def concat():
    t2=(11,13,15)
    t=t1+t2
    print("Concatenated t1 with t2- ", t)

def max_min():
    print("Maximum value from tuple t1-  ",max(t1))
    print("Minimum value from tuple t1-  ", min(t1))

while True:
    print("Given tuple t1=(1,2,5,7,9,2,4,6,8,10)")
    print()
    print("1.Print another tuple with even values from t1 ")
    print("2.Concatenate tuple t2=(11,13,15) with t1")
    print("3.Maximum and Minimum value from tuple t1")
    print("4.Exit")
    print()
    c=int(input("Enter your choice- "))
    if c==1:
        Even_tuple()
        print()
    if c==2:
        concat()
        print()
    if c==3:
        max_min()
        print()
    if c==4:
        exit(0)


