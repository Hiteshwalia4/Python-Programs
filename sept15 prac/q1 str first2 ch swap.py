def swap(x,y):
    s1=y[:2] + x[2:]
    s2=x[:2] + y[2:]
    print( s1 , " " , s2)


str1 = input("Enter the First String- ")
str2 = input("Enter the Second String- ")
swap(str1,str2)
