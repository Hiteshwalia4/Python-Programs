n = int(input("Enter the number of elements- "))
list = []
e = 1

for i in range(1,n+1):
    list1 = []
    list.append(list1)

    for j in range(1,6):
        e = j*i
        list1.append(e)

print(list)
