n = int(input("Enter n- "))

print("file1 data- ")
with open('abc.txt') as rr:
    line_ls = rr.readlines()
    for l in line_ls:
        print(l , end = "")
        
with open('abc_n.txt' , 'w') as wr:
    i = -n;
    while i!=0:
        wr.write(line_ls[i])
        i+=1

print("\n")
print("file2 data- ")
with open('abc_n.txt' , 'r') as rr:
    line_ls = rr.readlines()
    for l in line_ls:
        print(l , end = "")
        
print("\n")
