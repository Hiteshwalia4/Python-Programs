def get():
    x = int(input("Enter value for x-  "))
    y = int(input("Enter value for y-  "))
    z = int(input("Enter value for z-  "))
    n = int(input("Enter value for n-  "))
    return x, y, z, n


def coordinates():
    x, y, z, n = get()
    list1 = [[i, j, k] for i in range(0, x + 1) for j in range(0, y + 1) for k in range(0, z + 1) if (i + j + k) != n]
    print(list1)


coordinates()
