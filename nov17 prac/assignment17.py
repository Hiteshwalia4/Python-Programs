# Question 1
f = lambda s:sorted([int(i) for i in s.split() if i.isdigit() and int(i)>len(s.split())])

def fxn():
    s = input("Enter a string : ")
    print(f(s))

fxn()


# Question 2
def is_prime(x):
    flag = True
    for i in range(2,int(x/2)):
        if(x%i==0):
            flag = False
            break
    return flag

def fxn():
    with open("file1.txt",'w') as f1,open("file2.txt",'w') as f2:
        f1.write("2\n")
        l1 = [str(i)+"\n" for i in range(3,1000) if is_prime(i)]
        l2 = [str(i)+"\n" for i in range(1,1000,2)]
        f1.writelines(l1)
        f2.writelines(l2)
    with open("file1.txt",'r') as f1,open("file2.txt",'r') as f2:
        p=f1.readlines()
        t=f2.readlines()
        for x in p:
            if x in t:
                print(x)
fxn()

# Question 3
f = lambda l:max(l)-min(l)

def fxn():
    l = [int(i) for i in input("Enter numbers in list : ").split() if i.isdigit]
    print(f(l))

fxn()


# Question 4
def inp():
    x = int(input("Enter value for x : "))
    y = int(input("Enter value for y : "))
    z = int(input("Enter value for z : "))
    n = int(input("Enter value for n : "))
    return x,y,z,n
    
def fxn():
    x,y,z,n = inp()
    l = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if(i+j+k)!=n]
    print(l)

fxn()
