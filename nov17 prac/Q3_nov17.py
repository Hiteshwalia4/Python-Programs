l= lambda t:max(t)-min(t)

def difference():
    list1 = [int(i) for i in input("Enter numbers in list-  ").split() if i.isdigit]
    print(l(list1))

difference()

