def unzip_tuple():
    list1=[]
    n=int(input("Enter number of elements in list- "))
    for i in range(n):
        print("Want string tuple elements or Int??   (Press S for string and I for int)")
        ch=input()
        if ch=="S":
            a=(input("Enter 1st part of element-  "),input("Enter 2nd part of element-  "))
            list1.append(a)
        if ch=="I":
            b = (int(input("Enter 1st part of element-  ")), int(input("Enter 2nd part of element-  ")))
            list1.append(b)
    print("Entered list is-  ",list1)
    print()
    print("Unzipped list of tuples-  ")
    for i in list1:
        print(list(i))


unzip_tuple()