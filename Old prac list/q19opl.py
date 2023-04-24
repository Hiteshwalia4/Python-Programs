n=int(input("Enter number of words- "))
def inverted_dic():
    x=dict([])
    y=dict([])
    for i in range(n):
        a=input("Enter the word-  ")
        b=input("Enter the meaning- ")
        x[a]=b
        y[b]=list(a)
    print("Before Inversion- ",x)
    print("After Inversion- ",y)

inverted_dic()
