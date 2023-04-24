def highest():
    record=dict([])
    temp=dict([])
    n=int(input("Enter number of students- "))
    for i in range(n):
        print()
        key=input("Enter the name- ")
        value=dict([])
        total=0
        for y in range(4):
            marks=float(input("Enter marks- "))
            value["subject"+str(y+1)]=marks
            total=total+marks

        per=(total/40)*100
        temp[key]=per
        record[key]=value

    maxi=max(temp,key=temp.get)
    print()
    print("Names and marks- ",record)
    print("student with maximum % -",maxi)

highest()
