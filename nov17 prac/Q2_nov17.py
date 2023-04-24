def is_prime(x):
    k = True
    for i in range(2,int(x/2)):
        if(x%i==0):
            k = False
            break
    return k

def mainfunc():
    with open("abc.txt",'w') as f1,open("xyz.txt",'w') as f2:
        f1.write("2\n")
        list1 = [str(i)+"\n" for i in range(3,1000) if is_prime(i)]
        list2 = [str(i)+"\n" for i in range(1,1000,2)]
        f1.writelines(list1)
        f2.writelines(list2)
    with open("abc.txt",'r') as f1,open("xyz.txt",'r') as f2:
        a=f1.readlines()
        b=f2.readlines()
        for x in a:
            if x in b:
                print(x)
mainfunc()
