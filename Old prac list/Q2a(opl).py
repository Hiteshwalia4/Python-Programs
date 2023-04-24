

for i in range(1,6):
    print("\n", end="")
    if i<=3:
        for j in range(i,3):
            print(" ", end="")
        for j in range(1,i+1):
            print("*", end ="")
        for j in range(2,i+1):
            print("*", end ="")
    else:
        for j in range(3,i):
            print(" ", end="")
        for j in range(i,6):
            print("*", end ="")
        for j in range(i,5):
            print("*", end ="") 