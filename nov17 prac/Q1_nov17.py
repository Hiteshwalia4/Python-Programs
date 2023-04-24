l = lambda s:sorted([int(i) for i in s.split() if i.isdigit() and int(i)>len(s.split())])

def lamdaQ1():
    a = input("Enter a string-  ")
    print(l(a))

lamdaQ1()
