def sublist(A):  
   B = [[ ]]   
   for i in range(len(A) + 1):   
      for j in range(i + 1, len(A) + 1):           
         sub = A[i:j] 
         B.append(sub) 
   return B 
A=list()
n=(input("Enter the size of List- "))
print("Enter the Element-  ")
for i in range(int(n)):
   k=(input(""))
   A.append(k)
print("Sublist of the entered list is- ",sublist(A)) 
