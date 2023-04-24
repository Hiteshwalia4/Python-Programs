def wordcount(str):
    c=0
    str = str.split()
    s=[]
    for i in str:
        if i not in s:
            s.append(i)
    for i in range(0,len(s)):
        print("The word",s[i],"is prsent ",str.count(s[i])," times")
            

a = input("Enter the String- ")
print(wordcount(a))
