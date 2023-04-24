
def conc_file():
    print("file1 data-  ")
    with open('abc.txt' ) as rr1 , open('abc2.txt') as rr2:
   
        l1 = rr1.readlines()
        l2 = rr2.readlines()
        
        for i in range(len(l1)):
            if i!= len(l1)-1:
                l1[i] = l1[i][:-1]
        for i in range(len(l2)):
            if i!= len(l2)-1:
                l2[i] = l2[i][:-1]
        while l1 or l2:
            if l1 and l2:
                   print(l1.pop(0)," ",l2.pop(0))
            elif l1:
                print(l1.pop(0))
            elif l2:
                print(l2.pop(0))

        
    print("\n")

conc_file()
    
