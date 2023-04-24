str=input("Enter a string- ")
freq=dict([])
for i in str:
    if (i not in freq and i not in " "):
        k=0
        for y in str:
            if y==i:
                k=k+1
        freq[i]=k

print(freq)
