list1 = []
print("Enter no. of elements in list-  ")
n = int(input())
for i in range(n):
    a = input("Enter element no. " + str(i + 1) + " -  ")
    list1.append(a)
print("The list entered is-  ", list1)

while True:
    print("1. Check if all elements in list are numbers or not ")
    print("2. Count odd values(Only if the list is numeric)  ")
    print("3. Display largest string ")
    print("4. Reverse the list ")
    print("5. Find a specific list element  ")
    print("6. Find common numbers between two lists ")
    print("7. Exit")
    print("Enter your choice-  ")
    c=int(input())
    if(c>=7):
        exit(0)
    if(c==1):
        k=0
        for i in list1:
            if i.isdigit()==1:
                k+=1
        if k==len(list1):
            print("All elements of list are numbers")
        else:
            print("All elements of list are not numbers")

    if(c==2):
        k = 0
        for i in list1:
            if i.isdigit() == 1:
                k += 1
        if k == len(list1):
            s=0
            for i in list1:
                if int(i)%2!=0:
                    s+=1
            print("No. of odd values- ",s)
        else:
            print("Unavailable!!! List is not numeric")

    if(c==3):
        k = 0
        for i in list1:
            if i.isdigit() == 1:
                k += 1
        if k == len(list1):
            print("Unavailable!!! List is fully numeric")
        else:
            l=0
            for i in list1:
                if(len(i)>l):
                    ls=i
                    l=len(i)
            print("Largest string-  ",ls,"  with size of ",l)

    if(c==4):
        h=list1.copy()
        h.reverse()
        print("Reversed list is-  ",h)


    if(c==5):
        print("Enter value to be searched-  ")
        find=input()
        for i in list1:
            if i==find:
                print("Element Found ")
                break
        else:
            print("Element not found")

    if(c==6):
        print("Enter number of elements in 2nd list-  ")
        num=int(input())
        y=[]
        final=[]
        for i in range(num):
              k=input("Enter element no. "+str(i+1)+" of list 2-  ")
              y.append(k)
              if (k in list1):
                 final.append(k)
        print("Common values in both lists are-  ",final)
