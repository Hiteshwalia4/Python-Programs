list1=[]
print("Enter no. of elements in list-  ")
n = int(input())
for i in range(n):
    a = int(input("Enter element no. " + str(i + 1) + " -  "))
    list1.append(a)
print("The list entered is-  ", list1)

def Recursive_sort(l,p=0):
    if p==len(l)-1:
        print("List is sorted ")
    elif l[p]<=l[p+1]:
        Recursive_sort(l,p+1)
    else:
        print("List is not sorted ")


Recursive_sort(list1)



