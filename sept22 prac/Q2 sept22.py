def dupl(d):
   list = []
   for n in d:
      if n not in list:
         list.append(n)
   return list
d=list()
n=int(input("Enter the size of the List- "))
print("Enter the elements of List-")
for i in range(int(n)):
    
    k=int(input(""))
    d.append(int(k))
print("List after removing duplicates- ",dupl(d))
